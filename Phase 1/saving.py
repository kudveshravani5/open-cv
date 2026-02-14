import cv2
image = cv2.imread(r"C:\Users\GANESH KUDE\open cv\Phase 1\Python-Logo.png")

if image is not None:
    success=cv2.imwrite("output_image.png", image)
    if success:
        print("Image saved successfully as 'output_image.png'")
    else:
        print("Failed to save the image")
else:
    print("Could not load the image")

