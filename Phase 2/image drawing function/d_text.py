import cv2
image = cv2.imread("C:\\Users\\GANESH KUDE\\open cv\\Phase 2\\image drawing function\\resized_image.png")
if image is None:
    print("Oops ! Your image is not working")
else: 
    print("Image load successfully")
    cv2.putText(image,"Hello Python Programming", (50,300), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 2) #(image,text,org,font, font scale,color,thickness)
    cv2.imshow("Adding text to image ", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()