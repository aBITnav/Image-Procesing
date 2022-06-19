import cv2
import statistics as st

img=cv2.imread("img/Sample1.jpg",0)


cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
h,v=img.shape

k=4
img2=img.copy()
compressbit=""

##################################################
for i in range(0,h-k,k):
    for j in range(0,v-k,k):
        arr=[]
        for x in range(k):
            for y in range(k):
                arr.append(int(img[i+x][j+y]))
        mb=st.mean(arr)
        sd=st.stdev(arr)**0.5
        q=0
        for x in range(k):
            for y in range(k):
                if img[i+x][j+y]>=mb:
                    q+=1
                    
        high=mb+sd*((k*k-q)/q)**0.5
        low=mb-sd*((k*k-q)/q)**0.5
        
        for x in range(k):
            for y in range(k):
                if img[i+x][j+y]>=mb:
                    img2[i+x][j+y]=high
                    compressbit+='1'
                else:
                    img2[i+x][j+y]=low
                    compressbit+='0'

cv2.imshow("BTC image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(compressbit)