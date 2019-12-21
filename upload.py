from skimage.metrics import structural_similarity as ssim
import numpy as np
import cv2
import boto3
import datetime
import os
import types
import os
import argparse

# Get command line arguments to force run
parser = argparse.ArgumentParser(description='Take picture and upload')
parser.add_argument('-f', action='store_true', help='Force run image and upload')
args = parser.parse_args()
force = args.f

from dotenv import load_dotenv
load_dotenv()

# check if datetime is a weekday between 7:30 - 5:30
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

today = datetime.datetime.now()

# TODO - add flag for testing: ignore time constraints

def mse(image_a, image_b):
    # the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
    result = np.sum((image_a.astype('float') - image_b.astype('float')) ** 2)
    result /= float(image_a.shape[0] * image_b.shape[1])

    return result


def same_image(original, new):
    mse_result = mse(original, new)
    ssim_result = ssim(original, new)

    # MSE increases the images are less similar
    # SSIM has smaller values, which indicate less similarity.

    return ssim_result >= 0.75 and mse_result <= 1000


if (today.weekday() <= 4 and 7 < today.hour < 18) or force:
    cam = cv2.VideoCapture(0)
    success, img = cam.read()
    success = True
    duplicate_image = False

    if success:
        previous_image = cv2.imread('previous.jpg')

        tstamp = today.strftime('%Y-%m-%d_%H-%M-%S')
        filename = 'parking-vision-01-img_' + tstamp + '.jpg'
        print('Saving Image')
        cv2.imwrite(filename, img)

        if previous_image is not None:
            print('previous image found, comparing')
            is_duplicate = same_image(cv2.imread(filename), previous_image)


        if is_duplicate is False:
            print('Images are different, uploading new image')
            client = boto3.client(
                's3',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                region_name='us-east-2'
            )
            client.upload_file(filename, 'parking-vision', filename)

            print('renaming image to previous')
            os.rename(filename, 'previous.jpg')
