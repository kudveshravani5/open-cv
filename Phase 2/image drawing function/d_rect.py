import cv2
image = cv2.imread("C:\\Users\\GANESH KUDE\\open cv\\Phase 2\\image drawing function\\resized_image.png")
if image is None:
    print("Oops ! Your image is not working")
else: 
    print("Image load successfully")
    pt1 = (50,100)
    pt2 = (200,250)
    color = (255,0,0) # Blue color in BGR
    thickness = 3 
    image_with_rectangle = cv2.rectangle(image, pt1, pt2, color, thickness)
    cv2.imshow("Image with Rectangle", image_with_rectangle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()