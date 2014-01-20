import sys
sys.path.insert(0,"../motorControl/")
import motorControl
sys.path.insert(0,"../computerVision/")
import FaceDetection
import VideoStream
sys.path.insert(0,"../settings/")
import settings
import cv2

class Camera:
    
  def __init__(self,precX,precY):
    self.precX = precX
    self.precY = precY
    self.centerX = 160
    self.centerY = 120

  def PositionCamera(self,position):
    angleAddition = []
    if position[0] < (self.centerX - self.precX):
      angleAddition += [5]
    elif position[0] > (self.centerX + self.precX) :
      angleAddition += [-5]
    else:
      angleAddition += [0]

    if position[1] < (self.centerY - self.precY):
      angleAddition += [5]
    elif position[1] > (self.centerY + self.precY) :
      angleAddition += [-5]
    else:
      angleAddition += [0]

    return angleAddition


if(__name__)=="__main__":


  motorSettings = settings.motorSettings()
  
  motorControler = motorControl.MotorControl(motorSettings.get())
  motorControler.setAllSpeed(100)
  
  camera = Camera(10,10)

  angle = []
  modAngle = []
   
  faceStream = FaceDetection.FaceStream(1)
  exit = False
  while not exit:
   frame = faceStream.nextFrame()
   faceStream.display()
   # Angle Reading
   angle    = motorControler.readMotorByName([["head"],["top"]])
   # Correction by Position for the first detected face
   if len(faceStream.faceDetection.faces) > 0:
     modAngle = camera.PositionCamera(faceStream.faceDetection.faces[0])
     print "Position x " + str(faceStream.faceDetection.faces[0][0]) + "\t" + "Position y " + str(faceStream.faceDetection.faces[0][1]) + "\r\n"
     # Assigning angle
     motorControler.setAllMotorsByName([["head",angle[0]+modAngle[0]],["top",angle[1]+modAngle[1]]])
   key = cv2.waitKey(10)
   if key == 'q':
     exit = True 
