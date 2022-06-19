import cv2
from matplotlib import pyplot as plt

img=cv2.imread("img/Sample2.jpg",0)
h,v=img.shape
#Thresholding
for i in range(h):
    for j in range(v):
        if img[i][j]>=150:
            img[i][j]=255
        else:
            img[i][j]=0

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

dirx = [0,1,2,7,3,6,5,4]
drid = dict(zip(dirx, range(len(dirx))))

dy =   [-1,0,1,-1,1,-1,0,1]
dx =   [-1,-1,-1,0,0,1,1,1]

chain = []

start_point=(31,36)

pnt = start_point
for d in dirx:
    idx = drid[d]
    nxtpnt = (start_point[0]+dx[idx], start_point[1]+dy[idx])
    if img[nxtpnt] != 0:
        chain.append(d)
        pnt = nxtpnt
        break

count = 0
while pnt != start_point:
    b_dir = (d + 5) % 8 
    dirs_1 = range(b_dir, 8)
    dirs_2 = range(0, b_dir)
    dirs = []
    dirs.extend(dirs_1)
    dirs.extend(dirs_2)
    for d in dirs:
        idx = drid[d]
        nxtpnt = (pnt[0]+dx[idx], pnt[1]+dy[idx])
        if img[nxtpnt] != 0: 
            chain.append(d)
            pnt = nxtpnt
            break
    if count == 1000: 
        break
    count += 1

print(chain)
plt.imshow(img)

