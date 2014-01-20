import sys
sys.path.insert(0,"../computerVision/")
import FaceDetection
import VideoStream

class CameraControl:
    
  def __init__(self,motorControler,faceStream,precX,precY,centerX=160,centerY=120):

    self.precX = precX
    self.precY = precY
    self.centerX = centerX
    self.centerY = centerY
    self.motorControler = motorControler
    self.faceStream = faceStream

  def positionCamera(self,position):
    """ Determine the changing on camera angle """

    # Initialisation
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
    modAngle = []
    if len(self.faceStream.faceDetection.faces) > 0:
      modAngle = self.positionCamera(self.faceStream.faceDetection.faces[0])
      self.moveHead([angle[0]+modAngle[0],angle[1]+modAngle[1]])
    
