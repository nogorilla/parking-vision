from cv2 import *
import boto3
import datetime
import os
from dotenv import load_dotenv
load_dotenv()
## check if datetime is a weekday between 7:30 - 5:30
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

today = datetime.datetime.now()

if (today.weekday() <= 4 and today.hour > 7 and today.hour < 18 ):
    cam = cv2.VideoCapture(0)   # 0 -> index of camera
    client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name='us-east-2'
    )

    s, img = cam.read()

    if s:
        tstamp = today.strftime('%Y-%m-%d_%H-%M-%S')
        filename = 'parking-vision-01-img_' + tstamp + '.jpg'
        print('Saving Image');
        cv2.imwrite(filename, img)

        print('Uploading Image')
        client.upload_file(filename, 'parking-vision', filename)