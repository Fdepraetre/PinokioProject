import FaceDetection
import VideoStream
import cv2

faceStream = FaceDetection.FaceStream()
exit = False
while not exit :
	frame =	faceStream.nextFrame()
	faceStream.display()
	key = cv2.waitKey(10)
	#if q key have been press
	if key == ord('q'): 
		exit = True
