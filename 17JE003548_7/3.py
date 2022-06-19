import cv2

img = cv2.imread('img/sample3.png',0)
h,v=img.shape
imgh=img.copy()
imgv=img.copy()
imgd=img.copy()
k=3
#sobel Horizontal
wh=[-1,-2,-1,0,0,0,1,2,1] 
#sobel Vertical
wv=[-1,0,1,-2,0,2,-1,0,1]

#GAUSS
def gauss(img):
    img2=img.copy()
    for i in range(h-k):
        for j in range(v-k):
            arr=[]
            for x in range(k):
                for y in range(k):
                    arr.append(img[i+x][j+y])
            
            avg=sum(arr)/len(arr)
            mx=max(arr)
            mn=min(arr)
            arr = [i for i in arr if i!=mn and i!=mx]
            if len(arr):
                avg=sum(arr)/len(arr)
            img2[i+k//2][j+k//2]=avg
        return img2
    
    
img=gauss(img)

#Sobel
for i in range(h-k):
    for j in range(v-k):
        gh=0
        gv=0
        for x in range(k):
            for y in range(k):
                gh+=(img[i+x][j+y])*wh[x*k+y];
                gv+=(img[i+x][j+y])*wv[x*k+y];
        
        imgd[i][j]=round((gh**2+gv**2)**0.45)
        
        if imgd[i][j]>=200:
            imgh[i][j]=255
        else:
            imgh[i][j]=0

cv2.imshow("Gradient image using sobel operator",imgd)
cv2.waitKey(0)
cv2.destroyAllWindows()