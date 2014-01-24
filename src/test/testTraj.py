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

# Define initial position , end position and the different Motor name 
# concerned by the trajectory
initPosition = [125,75,60]
motorName = ["head","top","bowl"]
finalPosition = [175,190,120]


def valueList(name,position):
  """ Concatenate two lists in one list of couple """
  values = []
  for i in range(len(name)):
    values += [[name[i],position[i]]]
  return values

# Set the trajectory controller with a max speed equal to 1000 and a max acceleration to 200
trajectoryController = trajectoryController.TrajectoryController(1000,200)
# Init the plotter to trajectory in 3 dimensions
trajectoryPlot = trajPlot.PlotTraj()
i = 0


# Parse the YAML file with motor and communication settings
motorSettings = settings.MotorSettings()
#Scan, detect and open communication with the motor on network
motorControler = motorControl.MotorControl(motorSettings.get())

#Go to initial position
print valueList(motorName,initPosition)
#Move the motor to the initial value without trajectory controller
motorControler.setMotorsByName(valueList(motorName,initPosition))
time.sleep(5)
#Compute the different coefficiant and the complete time to make the trajectory
trajectoryController.set(initPosition,finalPosition)
#Update return if the trajectory is ended or not
while not trajectoryController.update():
  #Get the motor value
  valMotor = motorControler.readMotorByName(motorName)
  print ""
  print "Trajectory : " + str(valMotor)
  print "Position : " + str(trajectoryController.position)
  print "Speed : " + str(trajectoryController.speed)
  #Set motor speed to trajectory speed ( the value is between 0 and speed max)
  motorControler.setAllSpeed(int(trajectoryController.speed))
  # Set motor position to trajectory position
  motorControler.setMotorsByName(valueList(motorName,trajectoryController.position))
  i += 1
  # Add new val to the plot
  trajectoryPlot.addNewVal(valMotor,
      time.time()-trajectoryController.timeInit,
      [trajectoryController.position[0],trajectoryController.position[1],trajectoryController.position[2]]
      )

print "Le nombre de point est " + str(i)
#Dislay the plot
trajectoryPlot.plot()

