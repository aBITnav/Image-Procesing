import cv2
img=cv2.imread("img/sample2.png",0)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

h,v=img.shape

dx=[1,1,0,-1,-1,-1,0,1]
dy=[0,-1,-1,-1,0,1,1,1]
t=30


def inside(i,j):
    return (i>=0 and j>=0 and i<h and j<v)
    
def dfs(x,y):
    img[x][y]=250
    mean=0
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if inside(nx,ny):
            mean+=img[nx][ny]
    mean/=8
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if inside(nx,ny) and img[nx][ny]!=250 and  abs(img[nx][ny]-mean)<=t:
            dfs(nx,ny)    
    
dfs(100,100)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
