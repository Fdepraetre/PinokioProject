import sys
sys.path.insert(0,"../control/")
import motorControl
import cameraControl
sys.path.insert(0, "../computerVision/")
import FaceDetection
import VideoStream
sys.path.insert(0, "../arduino/")
import python2arduino
sys.path.insert(0,"../settings/")
import settings
import cv2

motorSettings = settings.MotorSettings()

motorControler = motorControl.MotorControl(motorSettings.get())
motorControler.setAllSpeed(10)
faceStream = FaceDetection.FaceStream(1)

precision = 0.1
res = [360,240]
apertureAngle = [50.,30.]
camera = cameraControl.CameraControl(motorControler, faceStream, precision, res, apertureAngle)

angle = []
modAngle = []
 
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
  camera.updateControl()
  key = cv2.waitKey(10)
	#if q key have been press
  if key == ord('q'): 
    exit = True
