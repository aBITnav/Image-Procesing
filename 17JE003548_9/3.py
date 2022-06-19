import cv2
from skimage.measure import euler_number

img=cv2.imread("img/Sample3.png",0)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
h,v=img.shape

ret, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY + 
                                            cv2.THRESH_OTSU)  

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

eulno = euler_number(img, connectivity=8)

print(eulno)