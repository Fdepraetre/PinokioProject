import sys
sys.path.insert(0,"../computerVision/")
import FaceDetection
import VideoStream
import math

ApertureAngle = [50.,30.]

class CameraControl:
    
  def __init__(self, motorControler, faceStream, precision, res, apertureAngle):
    self.p = 1 #0.25

    assert len(res) == 2, 'res have to be of size 2'
    assert len(apertureAngle) == 2, 'apertureAngle have to be of size 2'

    self.precision = [precision * res[0], precision * res[1]]
    self.res = res
    self.apertureAngle = apertureAngle

    self.motorControler = motorControler
    self.faceStream = faceStream

  def positionCamera(self, position):
    """ Determine the changing on camera angle """
    # Initialisation
    angleAddition = []
    
    print "___"
    for i in range(len(position)):
      if self.precision[i] < (position[i] - self.res[i]/2) :
        angleAddition += [-(self.apertureAngle[i] / self.res[i]) * (position[i] - self.res[i]/2) * self.p]
      else:
        angleAddition += [0]
      print ""
      print "Position :" + str(position[i] - self.res[i]/2)
      print "Angle :" + str(angleAddition[i])
    print "___"
    return angleAddition


  def readHead(self):
    """ Return the angle of the head """
    angle = self.motorControler.readMotorByName([["head"],["top"]])
    return angle
 
  def moveHead(self,angle):
    """ Move head at angle """ 
    self.motorControler.setMotorsByName([["head",angle[0]],["top",angle[1]]])

  def updateControl(self):
    """ Update the head control """
    angle = self.readHead()
    if len(self.faceStream.faceDetection.faces) > 0:
      modAngle = self.positionCamera(self.faceStream.getFacePosition())
      self.moveHead([angle[0]+modAngle[0],angle[1]+modAngle[1]])
    
