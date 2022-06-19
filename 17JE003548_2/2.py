import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("sample2.png",0)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
plt.plot(histr) 
plt.show()

flat = img.flatten()

def cumsum(a):
    a = iter(a)
    b = [next(a)]
    for i in a:
        b.append(b[-1] + i)
    return np.array(b)


#img = cv2.equalizeHist(img) 
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
plt.plot(histr) 
plt.show()