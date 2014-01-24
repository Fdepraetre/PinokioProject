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

# Parse the YAML file with motor and communication settings
motorSettings = settings.MotorSettings()

#Scan, detect and open communication with the motor on network
motorControler = motorControl.MotorControl(motorSettings.get())
#Set motor speed to 10 ( the value is between 0 and 1024)
motorControler.setAllSpeed(10)
#Initialise the face detection on camera 1
#If you are using your laptop camera or if you don't have embedded camera on your laptop , change 1 by 0 
faceStream = FaceDetection.FaceStream(1)

#Set motor speed to 100 ( the value is between 0 and 1024)
motorControler.setAllSpeed(100)
precision = 0.1
res = [360,240]
apertureAngle = [50.,30.]

#Initialise the camera control , this is an overlay of motor control which control head
camera = cameraControl.CameraControl(motorControler, faceStream, precision, res, apertureAngle)

angle = []
modAngle = []

# Start the serial communication with the Arduino Board
#This path is only for Linux , window user you might change the path
arduino = python2arduino.Arduino()


exit = False
print faceStream.getRes()
while not exit :
  # Change the frame from camera
  frame =	faceStream.nextFrame()
  #If we detect a face
  if len(faceStream.faceDetection.faces)>0 :
    # Else we light in green the leds
    arduino.greenLight()
  else:
    # Else we light in red the leds
    arduino.redLight()
  #Display the frame from camera on screen
  faceStream.display()
  #Update the camera's control with the value 
  camera.updateControl()
  key = cv2.waitKey(10)
	#if q key have been press
  if key == ord('q'): 
    exit = True
