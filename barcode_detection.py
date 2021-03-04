#%% -1-
import numpy as np
import cv2

img = cv2.imread(r"C:\Users\OSMANMERTTOSUN\Desktop\barcode.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#%% -2-
# OpenCV provides three types of gradient filters or High-pass filters, Sobel, Scharr and Laplacian.
# If ksize = -1, a 3x3 Scharr filter is used which gives better results than 3x3 Sobel filter.

gradX = cv2.Sobel(gray, ddepth = cv2.cv2.CV_32F , dx = 1, dy = 0,ksize = -1)
gradY = cv2.Sobel(gray,ddepth = cv2.cv2.CV_32F, dx = 0, dy = 1, ksize= -1)

#%% -3-
#Substracting and converting the image back to grayscale after applying Sobel
gradient = cv2.subtract(gradY, gradX)
gradient = cv2.convertScaleAbs(gradient)


#%% -4-
#Smoothing out high frequency noise and thresholding the image
blurred = cv2.blur(gradient, ksize = (8,8))
(_, thresh) = cv2.threshold(blurred, 210, 255, cv2.THRESH_BINARY)
#cv2.imshow("img", thresh)
#%% -5-
#closing the gaps between the vertical bars of barcode
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
#cv2.imshow("img", closed)
#%% -6-
#Erosion and Dilation processes
#"Dilation adds pixels to the boundaries of objects in an image and erosion removes pixels on object boundaries"
closed = cv2.erode(closed, None, iterations = 1)
closed = cv2.dilate(closed, None, iterations = 10)
#cv2.imshow("img", closed)
#%% -7-
#Finding largest contour area
(cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
c = sorted(cnts, key = cv2.contourArea, reverse = True)
c = c[0]
rect = cv2.minAreaRect(c)
box = np.int0(cv2.boxPoints(rect))
cv2.drawContours(image, [box], -1, (0, 255,255), 3)
#%% -8-
cv2.imshow("img", image)
cv2.waitKey(0)





