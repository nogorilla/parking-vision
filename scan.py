import numpy as np
import argparse
import cv2
import imutils

# # load the image and compute the ratio of the old height
# # to the new height, clone it, and resize it
# image = cv2.imread("images/test-003.jpg")
# (h, w, d) = image.shape
# print("width={}, height={}, depth={}".format(w, h, d))

# # display the image to our screen -- we will need to click the window
# # open by OpenCV and press a key on our keyboard to continue execution
# cv2.imshow("Image", image)
# cv2.waitKey(0)

car_cascade = cv2.CascadeClassifier('cars.xml')

img = cv2.imread('images/MVIMG_20190501_184644-sm.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect cars
cars = car_cascade.detectMultiScale(gray, 1.1, 1)

# To draw a rectangle in each cars
for (x,y,w,h) in cars:
  cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()