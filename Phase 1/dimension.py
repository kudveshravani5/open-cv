import cv2
image = cv2.imread(r"C:\Users\GANESH KUDE\open cv\Phase 1\Python-Logo.png")
if image is not None:
    h , w , c = image.shape
    print(f"Image Loaded : \nHeight: {h}\nWidth: {w}\nChannels: {c}")
else:
    print("Could not load the image")
