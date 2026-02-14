import cv2
image = cv2.imread("C:\\Users\\GANESH KUDE\\open cv\\Phase 2\\Python-Logo.png")
if image is  None:
    print("Could not load the image")
else:    
    print("Image loaded successfully")
    resized = cv2.resize(image, (300, 300))
    cv2.imshow("Image", image)
    cv2.imshow("Resized Image", resized)
    cv2.imwrite("resized_image.png", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()