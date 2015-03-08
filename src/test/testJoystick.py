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

#Chargement du bras controlé
motorSettings = settings.MotorSettings()
motorControler = motorControl.MotorControl(motorSettings.get())


#Chargement du joystick
joystickSettings = settings.MotorSettings()
joystickControler = motorControl.Control(motorSettings.get())

#Activation de la caméra pour avoir un retour du robot
faceStream = FaceDetection.FaceStream(0)

#Camera 
precision = 0.1
res = [360,240]
apertureAngle = [50.,30.]

exit = False

while not exit :
 #Lecture des informations du joystick
 joystickControler.readAllMotor()
 #Recopie des valeurs sur la lampe
 motorControler.setMotorsByControler(joystickControler)
 #Attente d'un caractère
 key = cv2.waitKey(10)
 if key == ord('f'):
   exit = True

