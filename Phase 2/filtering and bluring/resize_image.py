import cv2
image = cv2.imread(r"C:\Users\GANESH KUDE\open cv\Phase 2\filtering and bluring\Nature image.jpg")
if image is None:
    print("Oops ! Your image is not working")
else: 
    print("Image load successfully")
    resized_image = cv2.resize(image, (300, 300)) # Resize to 300x300 pixels
    cv2.imshow("Resized Image", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()