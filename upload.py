import cv2
import boto3
import datetime
import os
import numpy as np
import types
import os
from dotenv import load_dotenv
load_dotenv()

# check if datetime is a weekday between 7:30 - 5:30
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

today = datetime.datetime.now()

# TODO - add flag for testing: ignore time constraints


def same_image(original, new):
    if original.shape == new.shape:
        print('The images have same size and channels')
        difference = cv2.subtract(original, new)

        b, g, r = cv2.split(difference)

        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print('The images are completely equal')
            return True

    return False


# if today.weekday() <= 4 and 7 < today.hour < 18:
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
        duplicate_image = same_image(cv2.imread(filename), previous_image)


    if duplicate_image is False:
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
