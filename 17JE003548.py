import cv2
import statistics as st

img=cv2.imread("img/Sample_image.png",0)

#img=cv2.copyMakeBorder(img.copy(),2,2,2,2,cv2.BORDER_CONSTANT,value=120)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
h,v=img.shape

k=3

##################################################
def denoise(img):
    img2=img.copy()
    for i in range(h-k):
        for j in range(v-k):
            arr=[]
            for x in range(k):
                for y in range(k):
                    arr.append(img[i+x][j+y])
            median=st.median(arr)
            img2[i][j]=median
    return img2

img=denoise(img)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

##################################################
def edges(img):
    img2=img.copy()
    swh=[-1,-2,-1,0,0,0,1,2,1] 
    swv=[-1,0,1,-2,0,2,-1,0,1]
    for i in range(h-k):
        for j in range(v-k):
            gh=0#radient horizontally and vertically
            gv=0
            for x in range(k):
                for y in range(k):
                    gh+=(img[i+x][j+y])*swh[x*k+y];
                    gv+=(img[i+x][j+y])*swv[x*k+y];
            
            img2[i][j]=round((gh**2+gv**2)**0.5) # magnitude of gradient
            
            if img2[i][j]>=45:
                img2[i][j]=255
            else:
                img2[i][j]=0
    return img2
                
img=edges(img)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

##################################################
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
    
def fineseg(img):   #  a
    return dilation(img)

img=fineseg(img)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

def fill(img):      #  b
    return erosion((dilation(img)))

img=fill(img)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

def seg(img):       #  c
    for i in range(h):
        for j in range(v):
            if i+j<100:
                img[i][j]=0
            if i+j>180:
                img[i][j]=0
    return img


img=seg(img)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

def erd(img):       #  d
    return erosion(img)

img=erd(img)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()



