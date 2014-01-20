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

motorSettings = settings.motorSettings()

motorControler = motorControl.MotorControl(motorSettings.get())
motorControler.setAllSpeed(100)
faceStream = FaceDetection.FaceStream(1)

camera = cameraControl.CameraControl(motorControler,faceStream,10,10)

angle = []
modAngle = []
 
exit = False
while not exit:
  frame = faceStream.nextFrame()
  faceStream.display()
  camera.updateControl()
  key = cv2.waitKey(10)
  if key == 'q':
    exit = True 
