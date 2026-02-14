import cv2
image = cv2.imread("C:\\Users\\GANESH KUDE\\open cv\\Phase 2\\resized_image.png")

if image is not None:
    cropped = image[100:200, 50:150]
    cv2.imshow("Original Image", image)
    cv2.imshow("Cropped Image", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()