import sys
sys.path.insert(0, "../computerVision/")
import FaceDetection
import VideoStream
sys.path.insert(0, "../arduino/")
import python2arduino
import cv2

faceStream = FaceDetection.FaceStream(0)

arduino = python2arduino.Arduino('/dev/ttyACM0')


exit = False
print faceStream.getRes()
while not exit :
  frame =	faceStream.nextFrame()
  if len(faceStream.faceDetection.faces)>0 :
    arduino.greenLight()
  else:
    arduino.redLight()
  faceStream.display()
  key = cv2.waitKey(10)
	#if q key have been press
  if key == ord('q'): 
    exit = True
