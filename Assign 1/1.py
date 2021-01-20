#Read image and flip
import cv2
img=cv2.imread("img/sample1.png",0)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

h,v=img.shape

flip=img

for x in range(h):
    flip[x]=img[x][::-1]
        
cv2.imshow("image",flip)
cv2.waitKey(0)
cv2.destroyAllWindows()