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

initPosition = [40,150,20]
motorName = ["head","top","bowl"]
finalPosition = [140,250,120]

def valueList(name,position):
  values = []
  for i in range(len(name)):
    values += [[name[i],position[i]]]
  return values

trajectoryController = trajectoryController.TrajectoryController(5,2)

motorSettings = settings.MotorSettings()
motorControler = motorControl.MotorControl(motorSettings.get())

#Go to initial position
motorControler.setMotorsByName(valueList(motorName,initPosition))
time.sleep(5)

trajectoryController.set(initPosition,finalPosition)
while not trajectoryController.update():
  valMotor = motorControler.readMotorByName(motorName)
  motorControler.setAllSpeed(trajectoryController.speed)
  motorControler.setMotorsByName(valueList(motorName,trajectoryController.position))
  print ""
  print "Trajectory : " + str(valMotor)
  print "Position : " + str(trajectoryController.position)

