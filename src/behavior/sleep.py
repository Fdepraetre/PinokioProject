import sys
sys.path.insert(0,"../control/")
import motorControl
import time
sys.path.insert(0,"../settings/")
import settings
sys.path.insert(0,"../arduino/")
import python2arduino
sys.path.insert(0,"../traj/")
import trajectoryController
import cv2
#import behavior

def valueList(name,position):
  """ Concatenate two lists in one list of couple """
  values = []
  for i in range(len(name)):
    values += [[name[i],position[i]]]
  return values



class Sleep:

  def __init__(self,motorController,arduino):
    self.motorController = motorController
    self.initPosition    = [160,125,113]
    self.movementList    = [[125],[150]]
    self.staticMotor     = ["bottom","bowl","mid","top"]
    self.dynamicMotors   = ["head"]
    self.arduino         = arduino

    self.traj = trajectoryController.TrajectoryController(100,20,1)
    self.index = 0

  def activate(self):
    self.motorController.setMotorsByName([["mid",self.initPosition[0]],["top",self.initPosition[1]],["head",self.initPosition[2]]])
    self.traj.set(self.movementList[self.index],self.movementList[(self.index+1)%(len(self.movementList))])
    self.arduino.fadeLed('b',4000)

  def update(self):
    res = self.traj.update()
      
    if not res :
      self.motorController.setAllSpeed(int(self.traj.speed)+20)
      self.motorController.setMotorsByName([[self.dynamicMotors[0],self.traj.position[0]]])

    else :
      self.traj.set(self.movementList[self.index],self.movementList[(self.index+1)%(len(self.movementList))])
      self.index =(self.index+1)%(len(self.movementList))

    return res

if (__name__)=='__main__':

  motorSettings = settings.MotorSettings()
  motorControler = motorControl.MotorControl(motorSettings.get())


  sleep = Sleep(motorControler)
  sleep.activate()
  exit = False
  while exit == False:

    sleep.update()
    time.sleep(1)
#    key = cv2.waitKey(10)
#    #if q key have been press
#    if key == ord('q'):
#      exit = True
  
