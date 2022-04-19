import cv2
import numpy as np

# Membuat Function
def sketch(image):
    # Mengkonversi gambar menjadi grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Membuat objek blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)
    
    # Mengkonversi gambar ke bentuk binary
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask

# Membuat objek VideoCapture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Our Live Sketcher', sketch(frame))
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break


cap.release()
cv2.destroyAllWindows()    