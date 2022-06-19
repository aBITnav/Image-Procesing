import cv2
img=cv2.imread("img/sample1.png",0)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
h,v=img.shape

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
        
cv2.imshow("image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


img2=img.copy()
k=5

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
        
cv2.imshow("image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()