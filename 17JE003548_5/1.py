import cv2

img=cv2.imread("img/sample1.bmp",0)
h,v=img.shape


cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
k=3

def erosion(img):
    img2=img.copy()
    for i in range(h-k):
        for j in range(v-k):
            c=0
            for x in range(k):
                for y in range(k):
                    if img[i+x][j+y]==255:
                        c+=1
            if c==k*k:
                img2[i+x//2][j+y//2]=255
            else:
                img2[i+x//2][j+y//2]=0
    return img2
    
    
def dilation(img):
    img2=img.copy()
    for i in range(h-k):
        for j in range(v-k):
            c=0
            for x in range(k):
                for y in range(k):
                    if img[i+x][j+y]==255:
                        c+=1
            if c!=0:
                img2[i+x//2][j+y//2]=255
            else:
                img2[i+x//2][j+y//2]=0
    return img2


imgopen=dilation(erosion(img))
cv2.imshow("opening",imgopen)
cv2.waitKey(0)
cv2.destroyAllWindows()

imgclose=erosion(dilation(img))
cv2.imshow("CLosing",imgclose)
cv2.waitKey(0)
cv2.destroyAllWindows()


