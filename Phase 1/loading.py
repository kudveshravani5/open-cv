import cv2
image = cv2.imread(r"C:\Users\GANESH KUDE\open cv\Phase 1\Python-Logo.png")

if image is not None:
    cv2.imshow("Image showing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Could not load the image")
