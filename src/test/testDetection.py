import sys
sys.path.insert(0, "../computerVision/")
import FaceDetection
import VideoStream
import cv2

# Initialise the face detection on camera 1
# If you are using your laptop camera or if you don't have embedded camera on your laptop , change 1 by 0 
faceStream = FaceDetection.FaceStream(1)

exit = False
print faceStream.getRes()
while not exit :
  # Change the frame from camera
	frame =	faceStream.nextFrame()
  # Display the frame from camera on screen
	faceStream.display()
	key = cv2.waitKey()
	#if q key have been press
	if key == ord('q'): 
		exit = True
