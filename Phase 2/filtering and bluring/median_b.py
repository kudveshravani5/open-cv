import cv2
image = cv2.imread(r"C:\Users\GANESH KUDE\open cv\Phase 2\filtering and bluring\resize_image.py")
median = cv2.medianBlur(image,5)#(image,kernal_size=odd))
cv2.imshow("Original_image",image)
cv2.imshow("Median_blurred_image",median)
cv2.waitKey(0)
cv2.destroyAllWindows()