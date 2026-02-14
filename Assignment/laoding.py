import cv2
location = input("Enter the location: ")
print(location)
image = cv2.imread(location)
user = input("Enter whether showing or saving as output image: ")
if user.strip().lower() == "showing":
    if image is not None:
        cv2.imshow("Image showing", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Could not load the image")
elif user.strip().lower() == "saving":
    if image is not None:
        success = cv2.imwrite("output_images.png", image)
        if success:
            print("Image saved successfully")
        else:
            print("Could not save the image")
if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Could not load the image")
