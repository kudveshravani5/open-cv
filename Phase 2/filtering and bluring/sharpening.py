import cv2
import numpy as np
image = cv2.imread(r"C:\Users\GANESH KUDE\open cv\Phase 2\filtering and bluring\resize_image.py")
kernal_array=np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]]
)
sharpened_image = cv2.filter2D(image,-1,kernal_array)# image,depth,kernal_array 
cv2.imshow("Original_image",image)
cv2.imshow("Sharpened_image",sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()