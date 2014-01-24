import sys
sys.path.insert(0,"../control/")
import motorControl
sys.path.insert(0, "../settings/")
import settings
import time
import numpy as np

#Scan, detect and open communication with the motor on network
motorSettings = settings.MotorSettings()
motorControler = motorControl.MotorControl(motorSettings.get())

#Set motor speed to 10 ( the value is between 0 and 1024)
motorControler.setAllSpeed(10)

motorName = "head"
initValue = 125
finalValue = 175
step = 10
stepTime = 0.1

#Go to initial position
motorControler.setMotorsByName([[motorName,initValue]])
time.sleep(5)
print ""
print "Init ok"
print "position : " + str(initValue)

for i in np.arange(0,step,1):
  #Compute next position
  position = initValue + (finalValue - initValue) * i/step
  #Set the value to the motor
  motorControler.setMotorsByName([[motorName,position]])
  print ""
  print "go to position : " + str(position)
  time.sleep(stepTime)
