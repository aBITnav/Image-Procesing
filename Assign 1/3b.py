#8 path to 4 path

import cv2
img=cv2.imread("img/sample1.png",0)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

h,v=img.shape

for x in range(h-1):
    for y in range(v-1):
        if img[x][y]==255 and img[x+1][y+1]==255 and img[x][y+1]==0:
            img[x][y+1]=255
        if img[x][y]==255 and img[x+1][y+1]==255 and img[x+1][y]==0:
            img[x+1][y]=255
        
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()