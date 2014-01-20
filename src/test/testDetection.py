import sys
sys.path.insert(0, "../computerVision/")
import FaceDetection
import VideoStream
import cv2

faceStream = FaceDetection.FaceStream(1)
exit = False
print faceStream.getRes()
while not exit :
	frame =	faceStream.nextFrame()
	faceStream.display()
	key = cv2.waitKey(10)
	#if q key have been press
	if key == ord('q'): 
		exit = True
