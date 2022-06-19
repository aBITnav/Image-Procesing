import cv2
import numpy as np
img=cv2.imread("img/sample1.jpg",0)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


h,w=img.shape
edges = cv2.Canny(img,50,150)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)



cv2.imshow("image",lines)
cv2.waitKey(0)
cv2.destroyAllWindows()