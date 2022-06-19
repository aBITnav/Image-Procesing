import cv2
img=cv2.imread("sample1.png",0)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

h,v=img.shape

mmin=img.min()
mmax=img.max()

for i in range(h):
    for j in range(v):
        img[i][j]=(img[i][j]-mmin)*(256/(mmax-mmin))
    
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()