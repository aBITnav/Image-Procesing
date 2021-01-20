import cv2
img=cv2.imread("img/sample2.png",0)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

h,v=img.shape

    
def dfs( img, i, j):
    if i<0 or j<0 or i>=len(img) or j>=len(img[0]) or img[i][j] != 255:
        return
    img[i][j] = 100
    dfs(img, i+1, j)
    dfs(img, i+1, j-1)
    dfs(img, i, j-1)
    dfs(img, i-1, j-1)
    dfs(img, i-1, j)
    dfs(img, i-1, j+1)
    dfs(img, i, j+1)
    dfs(img, i+1, j+1)

x1=int(input("Enter Source x coordinate\n"))
y1=int(input("Enter Source y coordinate\n"))
x2=int(input("Enter Destination x coordinate\n"))
y2=int(input("Enter Destination y coordinate\n"))

dfs(img,x1,y1)

if img[x2][y2]==100:
    print("Connected")
    
else:
    print("Not Connected")
