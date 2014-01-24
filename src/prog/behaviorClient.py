import sys
sys.path.insert(0,"../behavior/")
import searchFaces
import sleep
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


#Initialisation of motor with detection 
motorSettings = settings.MotorSettings()
motorControler = motorControl.MotorControl(motorSettings.get())
faceStream = FaceDetection.FaceStream(1)

# Init Face detection 
faceSearchBehavior = searchFaces.FaceSearch(motorControler,faceStream,15)
# Start Face Search 
faceSearchBehavior.start()

arduino = python2arduino.Arduino()
sleep = sleep.Sleep(motorControler)

#Camera 
precision = 0.1
res = [360,240]
apertureAngle = [50.,30.]

# Time out for loosing 
thresholdFace = 2

# Initialisation for the camera control
camera = cameraControl.CameraControl(motorControler, faceStream, precision, res, apertureAngle)

exit = False


state = "faceSearch"

# Set the light to red value on led circle
arduino.redLight()

while not exit :
  if state == "faceFollow" : 
    # A face is detected
    motorControler.setAllSpeed(100)
    lastTime = time.time()
    timeOut = 0
    # Time out to search a face
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
      # Display the frame
      faceStream.display()
      key = cv2.waitKey(10)
      camera.updateControl()
    state = "faceSearch"     
  elif state == "faceSearch" :
    # Start searching faces
    arduino.redLight()
    detect = faceSearchBehavior.start()
    if detect == True:
      state = "faceFollow"    
    else:
      state = "sleep"
  elif state == "sleep" :
    # Start sleeping
    arduino.blueLight()
    sleep.activate()
    while state == "sleep":
      sleep.update()
      key = cv2.waitKey(1000)
      if key == ord('f'):
        state = "faceSearch"
