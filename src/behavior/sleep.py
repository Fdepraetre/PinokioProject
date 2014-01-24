import sys
sys.path.insert(0,"../control/")
import motorControl
import time
sys.path.insert(0,"../settings/")
import settings
sys.path.insert(0,"../arduino/")
import python2arduino
import cv2
#import behavior


class Sleep:#(Behavior):

  def __init__(self,motorControl):
    self.motorControl = motorControl
    self.initPosition = [0,150,130,50,207]
    self.movementList = [50,113]
    self.index = 0

  def activate(self):
    self.motorControl.setMotorsByName([["bowl",self.initPosition[0]],["bottom",self.initPosition[1]],["middle",self.initPosition[2]],["top",self.initPosition[3]],["head",self.initPosition[4]]])


  def update(self):
    self.motorControl.setMotorsByName([["top",self.movementList[self.index]]])
    print self.index
    self.index =(self.index+1)%(len(self.movementList))



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
  
