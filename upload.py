from cv2 import *
import boto3
import datetime
## check if datetime is a weekday between 7:30 - 5:30

today = datetime.datetime.now()

if (today.weekday() <= 4 and today.hour > 7 and today.hour < 18 ):
    cam = cv2.VideoCapture(0)   # 0 -> index of camera
    # client = boto3.client('s3', region_name='us-east-2')

    s, img = cam.read()

    if s:
        print('Saving Image');
        # cv2.imwrite("filename.jpg", img)

        print('Uploading Image')
        # client.upload_file('filename.jpg', 'parking-vision', 'filename.jpg')