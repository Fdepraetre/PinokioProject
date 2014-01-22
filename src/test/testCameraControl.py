import sys
sys.path.insert(0,"../control/")
import motorControl
import cameraControl
sys.path.insert(0,"../computerVision/")
import FaceDetection
import VideoStream
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
 
exit = False
while not exit:
  frame = faceStream.nextFrame()
  faceStream.display()
  camera.updateControl()
  key = cv2.waitKey(10)
  if key == ord('q'):
    exit = True 
