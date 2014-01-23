import sys
sys.path.insert(0,"../control/")
import motorControl
sys.path.insert(0, "../settings/")
import settings
sys.path.insert(0,"../traj/")
import trajectoryController
import trajPlot
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

trajectoryController = trajectoryController.TrajectoryController(1000,200)
trajectoryPlot = trajPlot.PlotTraj()
i = 0

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
  motorControler.setAllSpeed(int(trajectoryController.speed))
  motorControler.setMotorsByName(valueList(motorName,trajectoryController.position))
  i += 1
#    time.sleep(0.01)
  trajectoryPlot.addNewVal(valMotor,
                         time.time()-trajectoryController.timeInit,
                          [trajectoryController.position[0],trajectoryController.position[1],trajectoryController.position[2]]
                          )
  
print "Le nombre de point est " + str(i)
trajectoryPlot.plot()
  
