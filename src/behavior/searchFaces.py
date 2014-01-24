import sys
sys.path.insert(0,"../control/")
import motorControl
sys.path.insert(0,"../computerVision/")
import FaceDetection
import time
sys.path.insert(0,"../traj/")
import trajectoryController
import random

def valueList(name,position):
  """ Concatenate the two parameter list in on list of tuple"""
  values = []
  for i in range(len(name)):
    values += [[name[i],position[i]]]
  return values


class FaceSearch:
  def __init__(self, motorControler, faceStream, timeOut):
    self.motorControler = motorControler
    self.faceStream = faceStream
    self.timeOut = timeOut
    self.dynamicMotors = ["bowl","mid","head"]
    self.staticMotor = ["bottom","top"]
    self.dynamicRanges = motorControler.getRangeByName(self.dynamicMotors)
    self.staticValues = {"bottom": 150, "top": 175}
    self.traj = trajectoryController.TrajectoryController(100,20)


  def start(self):
    """   """
    self.faceStream.nextFrame()
    timeOut = self.timeOut
    lastTime = time.time()
    self.__initMovement()
    while not self.faceStream.isFaceDetected() and timeOut > 0 :
      # Update face detection
      self.faceStream.nextFrame()

      # Update movement
      self.__updateMovement()

      # Update time
      currentTime = time.time()
      timeOut -= currentTime - lastTime
      lastTime = currentTime

    if self.faceStream.isFaceDetected():
      return True
    else:
      return False


  def __initMovement(self):
    """ Initialisation of value list and random trajectory  """
    valueList = []
    for name in self.staticMotor:
      valueList += [[name,self.staticValues[name]]]
    self.motorControler.setMotorsByName(valueList)

    self.__randomTraj()

  def __updateMovement(self):
    """ Update the coordinates and set the speed and position values  """
    if not self.traj.update() :
      self.motorControler.setAllSpeed(int(self.traj.speed)+20)
      self.motorControler.setMotorsByName(valueList(self.dynamicMotors,self.traj.position))
    else :
      self.__randomTraj()

    
  def __randomTraj(self):
    """ Set trajectory with random coordinates  """
    currentPosition = self.motorControler.readMotorByName(self.dynamicMotors)
    goalPosition = [] 
    for name in self.dynamicMotors:
      angleRange = self.dynamicRanges[name]
      goalPosition += [random.randint(angleRange[0],angleRange[1])]

    self.traj.set(currentPosition,goalPosition)

