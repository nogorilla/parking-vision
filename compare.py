import cv2
import numpy as np

# original = cv2.imread('images/parking-vision-01-img_2019-12-17_16-26-15.jpg')
# duplicate = cv2.imread('images/parking-vision-01-img_2019-12-18_08-08-14.jpg')

# if original.shape == duplicate.shape:
#   difference = cv2.subtract(original, duplicate)

#   b, g, r = cv2.split(difference)

#   if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
#     return True

# print('The images are different')

# img1 = cv2.imread('./previous.jpg')
# img2 = cv2.imread('./parking-vision-01-img_2019-12-18_22-13-50.jpg')

# diff = cv2.absdiff(img1, img2)
# mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

# th =1
# imask = mask>th

# canvas = np.zeros_like(img2, np.uint8)
# canvas[imask] = img2[imask]

# cv2.imwrite('results.png', canvas)

import cv2
import numpy as np
from skimage.measure import compare_ssim as ssim

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are

def diff_remove_bg(img0, img, img1):
    d1 = diff(img0, img)
    d2 = diff(img, img1)
    return cv2.bitwise_and(d1, d2)

x1 = cv2.imread("parking-vision-01-img_2019-12-18_22-13-50.jpg")
x2 = cv2.imread("previous.jpg")

x1 = cv2.cvtColor(x1, cv2.COLOR_BGR2GRAY)
x2 = cv2.cvtColor(x2, cv2.COLOR_BGR2GRAY)

absdiff = cv2.absdiff(x1, x2)
cv2.imwrite("images/absdiff.png", absdiff)

diff = cv2.subtract(x1, x2)
result = not np.any(diff)

m = mse(x1, x2)
s = ssim(x1, x2)

print("mse: %s, ssim: %s" % (m, s))

if result:
    print("The images are the same")
else:
    cv2.imwrite("images/diff.png", diff)
    print("The images are different")