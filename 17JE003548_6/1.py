import cv2
img=cv2.imread("img/sample1l.png",0)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
h,v=img.shape

img2=img.copy()
k=25

for i in range(0,h-k):
    for j in range(0,v-k):
        arr=[]
        for x in range(k):
            for y in range(k):
                arr.append(img[i+x][j+y])
        mu=sum(arr)/len(arr)
        sd=(sum([((x-mu)**2) for x in arr])/len(arr))**0.5
        T=mu-0.2*sd-10;
        for x in range(k):
            for y in range(k):
                if img[i+x][j+y]<=T:
                    img2[i+x][j+y]=0
                else:
                    img2[i+x][j+y]=255
        
cv2.imshow("image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()