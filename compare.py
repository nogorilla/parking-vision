# import the necessary packages
from skimage.metrics import structural_similarity as ssim
import numpy as np
import cv2

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	result = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	result /= float(imageA.shape[0] * imageA.shape[1])

	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return result

def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)

	print("%s: MSE: %.2f, SSIM: %.2f" % (title, m, s))

# load the images -- the original, the original + contrast,
# and the original + photoshop
different = cv2.imread("images/parking-vision-01-img_2019-12-20_07-53-55.jpg")
repeat = cv2.imread("images/parking-vision-01-img_2019-12-19_10-01-21.jpg")
original = cv2.imread("images/parking-vision-01-img_2019-12-19_10-21-59.jpg")

# convert the images to grayscale
original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
repeat = cv2.cvtColor(repeat, cv2.COLOR_BGR2GRAY)
different = cv2.cvtColor(different, cv2.COLOR_BGR2GRAY)

# compare the images
compare_images(original, original, "Original vs. Original")
compare_images(original, repeat, "Original vs. Repeat")
compare_images(original, different, "Original vs. Different")