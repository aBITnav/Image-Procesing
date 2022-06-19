import cv2

img=cv2.imread("img/sample1.jpeg",0)

cv2.imshow("BW input",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
h,v=img.shape

imgh=img.copy()
imgv=img.copy()
imgd=img.copy()
k=3
#sobel Horizontal
wh=[-1,-2,-1,0,0,0,1,2,1] 
#sobel Vertical
wv=[-1,0,1,-2,0,2,-1,0,1]

for i in range(h-k):
    for j in range(v-k):
        gh=0
        gv=0
        for x in range(k):
            for y in range(k):
                gh+=(img[i+x][j+y])*wh[x*k+y];
                gv+=(img[i+x][j+y])*wv[x*k+y];
        
        imgd[i][j]=round((gh**2+gv**2)**0.45)
        
        if imgd[i][j]>=100:
            imgh[i][j]=255
        else:
            imgh[i][j]=0

cv2.imshow("Gradient image using sobel operator",imgd)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imshow("Detected edges using sobel operator",imgh)
cv2.waitKey(0)
cv2.destroyAllWindows()

############################################################################

#Prewitt weights Horizontal
wh=[-1,-1,-1,0,0,0,1,1,1] 
#Prewitt Vertical
wv=[-1,0,1,-1,0,1,-1,0,1]

for i in range(h-k):
    for j in range(v-k):
        gh=0
        gv=0
        for x in range(k):
            for y in range(k):
                gh+=(img[i+x][j+y])*wh[x*k+y];
                gv+=(img[i+x][j+y])*wv[x*k+y];
        
        imgd[i][j]=round((gh**2+gv**2)**0.48)
        
        if imgd[i][j]>=100:
            imgh[i][j]=255
        else:
            imgh[i][j]=0

cv2.imshow("Gradient image using Prewitt operator",imgd)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imshow("Detected edges using Prewitt operator",imgh)
cv2.waitKey(0)
cv2.destroyAllWindows()
