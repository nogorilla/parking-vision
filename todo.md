# TODO
- [ ] load image
- [ ] find car in image - use test-003.jpg

From the video its not clear exactly what kind of algorithm has been used but if you want to develop it on your own, you can proceed as follows. To make the overall procedure simple, we assume that the camera is fixed i.e., it cannot rotate or zoom.

1. Define background image - Take snapshot of the parking space as background image (without having any car parked in the parking lot and marking lines clearly visible).
1. Initialize parking map as rectangles - Do it manually(as we assumed the camera is fixed) or automatically by detecting white marker lines through color or line detection or any other image processing technique.
1. Continuously check for parking status - For each frame of the camera feed, check if parking spaces(marked rectangular positions) are occupied or not by background subtraction method or any other methods.
1. Update status - Update parking status accordingly (as shown in the right window of the video)

https://stackoverflow.com/questions/42678761/auto-parking-space-detection-how-to-initialize-parking-map-space-with-opencv-a