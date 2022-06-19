import cv2

img=cv2.imread("img/sample2.png",0)


cv2.imshow("BW input",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
h,v=img.shape

def gauss(img):
    img2=img.copy()
    k=3
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

imgh=img.copy()
imgv=img.copy()
imgd=img.copy()
k=5
#sobel Horizontal
wh=[0,0,-1,0,0,0,-1,-2,-1,0,-1,-2,16,-2,-1,0,-1,-2,-1,0,0,0,-1,0,0] 

for i in range(h-k):
    for j in range(v-k):
        gh=0
        for x in range(k):
            for y in range(k):
                gh+=(img[i+x][j+y])*wh[x*k+y];
        
        if gh>50:
            imgh[i][j]=255
        else:
            imgh[i][j]=0
            
            
imgh=gauss(imgh)

cv2.imshow("Gradient image using sobel operator",imgh)
cv2.waitKey(0)
cv2.destroyAllWindows()




