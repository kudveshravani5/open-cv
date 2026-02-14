import cv2
image = cv2.imread("C:\\Users\\GANESH KUDE\\Downloads\\Nature image.jpg")#A clear image of nature
blurred = cv2.GaussianBlur(image,(3,3), 4)#(image_sorce,(kernal_size=it should odd(,)),sigma=blurr quantity in numeric) 
cv2.imshow("Original_image",image)
cv2.imshow("Blurred_image",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()