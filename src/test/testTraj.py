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


trajectoryController = trajectoryController.TrajectoryController(5,2)

motorSettings = settings.MotorSettings()
motorControler = motorControl.MotorControl(motorSettings.get())
motorControler.setAllSpeed(100)
valMotor = motorControler.readMotorByName([["head"],["top"],["bowl"]])


trajectoryController.set(valMotor,[40,150,20])
while time.time()- trajectoryController.timeInit < trajectoryController.timef :
  valMotor = motorControler.readMotorByName([["head"],["top"],["bowl"]])
  motorControler.setMotorsByName([["head",trajectoryController.position[0]],["top",trajectoryController.position[1]],["bowl",trajectoryController.position[2]]])
  trajectoryControler.update(trajectoryController.position)

