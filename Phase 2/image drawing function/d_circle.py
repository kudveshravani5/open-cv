import cv2
image = cv2.imread("C:\\Users\\GANESH KUDE\\open cv\\Phase 2\\image drawing function\\resized_image.png")
if image is None:
    print("Oops ! Your image is not working")
else: 
    print("Image load successfully")
    cv2.circle(image, (150,150), 50, (0,255,0), 5) # (image, center, radius, color, thickness)
    cv2.imshow("Circle Drawing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()