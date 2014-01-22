import sys
sys.path.insert(0,"../control/")
import motorControl
sys.path.insert(0, "../settings/")
import settings
sys.path.insert(0,"../traj/")
import trajectoryController
import time
import cv2
import select

initPosition = [140,50,120]
motorName = ["head","top","bowl"]
finalPosition = [240,150,220]

def valueList(name,position):
  values = []
  for i in range(len(name)):
    values += [[name[i],position[i]]]
  return values

trajectoryController = trajectoryController.TrajectoryController(100,20)

motorSettings = settings.MotorSettings()
motorControler = motorControl.MotorControl(motorSettings.get())

#Go to initial position
print valueList(motorName,initPosition)
motorControler.setMotorsByName(valueList(motorName,initPosition))
time.sleep(5)

trajectoryController.set(initPosition,finalPosition)
while not trajectoryController.update():
  valMotor = motorControler.readMotorByName(motorName)
  print ""
  print "Trajectory : " + str(valMotor)
  print "Position : " + str(trajectoryController.position)
  print "Speed : " + str(trajectoryController.speed)
  motorControler.setAllSpeed(int(trajectoryController.speed)+20)
  motorControler.setMotorsByName(valueList(motorName,trajectoryController.position))
  time.sleep(0.1)
  
