import numpy as np
import cv2

print("Particular Color detection by canny edge detector")

img = cv2.imread("flw.jpg",1)
cv2.imshow("Original",img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
res,thresh = cv2.threshold(hsv[:,:,2],25,255,cv2.THRESH_BINARY_INV) 
cv2.imshow("Thresh" , thresh)
edges = cv2.Canny(img,100,70)
cv2.imshow("Canny", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
