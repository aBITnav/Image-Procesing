import cv2
img=cv2.imread("img/sample2.png",0)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

h,v=img.shape



def com(img):
    c=0
    for i in range(len(img)):
        for j in range(len(img[0])):
            if img[i][j] == 255:
                dfs(img, i, j)
                c += 1
    return c

    
def dfs( img, i, j):
    if i<0 or j<0 or i>=len(img) or j>=len(img[0]) or img[i][j] != 255:
        return
    img[i][j] = 0
    dfs(img, i+1, j)
    dfs(img, i+1, j-1)
    dfs(img, i, j-1)
    dfs(img, i-1, j-1)
    dfs(img, i-1, j)
    dfs(img, i-1, j+1)
    dfs(img, i, j+1)
    dfs(img, i+1, j+1)

print("NUMBER OF CONNECTED COMPONENTS ARE: ")   
print(com(img))