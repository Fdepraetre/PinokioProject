import sys
sys.path.insert(0,"../behavior/")
import searchFaces
sys.path.insert(0,"../control/")
import motorControl
import cameraControl
sys.path.insert(0,"../computerVision/")
import FaceDetection
sys.path.insert(0,"../settings/")
import settings
import time
sys.path.insert(0, "../arduino/")
import python2arduino
import cv2


motorSettings = settings.MotorSettings()
motorControler = motorControl.MotorControl(motorSettings.get())
faceStream = FaceDetection.FaceStream(1)

faceSearchBehavior = searchFaces.FaceSearch(motorControler,faceStream,60)
faceSearchBehavior.start()

arduino = python2arduino.Arduino('/dev/ttyACM0')

precision = 0.1
res = [360,240]
apertureAngle = [50.,30.]
camera = cameraControl.CameraControl(motorControler, faceStream, precision, res, apertureAngle)

exit = False
thresholdFace = 2
state = "faceSearch"
arduino.redLight()
while not exit :
  if state == "faceFollow" : 
    motorControler.setAllSpeed(100)
    lastTime = time.time()
    timeOut = 0
    while timeOut < thresholdFace :
      frame =	faceStream.nextFrame()
      if faceStream.isFaceDetected():
        arduino.greenLight()
        timeOut = 0
        lastTime = time.time()
      else:
        currentTime = time.time()
        timeOut += currentTime - lastTime
        lastTime = currentTime
        arduino.redLight()
      faceStream.display()
      key = cv2.waitKey(10)
      camera.updateControl()
    state = "faceSearch"     
  elif state == "faceSearch" :
    faceSearchBehavior.start()
    state = "faceFollow"     
