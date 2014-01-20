import sys
sys.path.insert(0,"../computerVision/")
import FaceDetection
import VideoStream
import math

class CameraControl:
    
  def __init__(self,motorControler,faceStream,precX,precY,centerX=160,centerY=120):

    self.precX = precX
    self.precY = precY
    self.centerX = centerX
    self.centerY = centerY
    self.motorControler = motorControler
    self.faceStream = faceStream

  def positionCamera(self,position,mode=0,distance = 5):
    """ Determine the changing on camera angle """
    angleAddition = []

    if mode == 0 :
       # Initialisation
    
       if position[0] < (self.centerX - self.precX):
         angleAddition += [2]
       elif position[0] > (self.centerX + self.precX) :
         angleAddition += [-2]
       else:
         angleAddition += [0]
  
       if position[1] < (self.centerY - self.precY):
         angleAddition += [2]
       elif position[1] > (self.centerY + self.precY) :
         angleAddition += [-2]
       else:
         angleAddition += [0]
  
    elif mode == 1 :
        distanceToFace = distance

        print position
        #angleAddition +=
        #angleAddition += 
        angleAddition += [ -(180/math.pi)*math.atan2( (position[0] - self.centerX), distanceToFace)]
        angleAddition += [ -(180/math.pi)*math.atan2( (position[1] - self.centerY), distanceToFace)]
        print angleAddition
    return angleAddition


  def readHead(self):
    """ Return the angle of the head """
    angle = self.motorControler.readMotorByName([["head"],["top"]])
    return angle
 
  def moveHead(self,angle):
    """ Move head at angle """ 
    self.motorControler.setAllMotorsByName([["head",angle[0]],["top",angle[1]]])

  def updateControl(self):
    """ Update the head control """
    angle = self.readHead()
    if len(self.faceStream.faceDetection.faces) > 0:
      modAngle = self.positionCamera(self.faceStream.faceDetection.faces[0],1)
      #self.moveHead([angle[0]+modAngle[0],angle[1]+modAngle[1]])
    
