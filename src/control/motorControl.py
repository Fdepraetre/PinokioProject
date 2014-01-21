import sys
import dynamixel
import time
import random
import sys
import optparse
import plot
sys.path.insert(0, "../settings/")
import settings
import math

class Motor:

  def __init__(self,motor,name,minAngle = 0,maxAngle = 300 ):
    self.motor = motor
    self.maxAngle = maxAngle
    self.minAngle = minAngle
    self.valeur = 0
    self.name = name


  def update(self,val):
    if val > self.maxi:
      self.motor.goal_position = maxi
    elif val < self.mini:
      self.motor.goal_position = mini
    else :
      self.motor.goal_position = val

  def setAngle(self,angle):
    if angle > self.maxAngle or angle < self.minAngle:
      print "Angle out of range"
      print "motor : " + str(self.name)
      print "value : " + str(angle)
      print "range : [" + str(self.maxAngle) + "," + str(self.minAngle) + "]"
    if self.name == "bottom":
      fact = 6.82
    else:
      fact = 3.41
    self.motor.goal_position = int(fact * angle)

  def setSpeed(self,speed):
       self.motor.moving_speed = speed

  def setSynchronize(self,synchronized):
       self.motor.synchronized = synchronized

  def readMotorPosition(self):
      self.motor.read_all()
      time.sleep(0.1)
      return self.motor.current_position


class MotorControl:
   
  def __init__(self,settings):
    self.portName       = settings['port']
    self.baudRate       = settings['baudRate']
    self.motorConfig    = settings['motorConfig']
    self.motors         = [] 
     
    # Establish a serial connection to the dynamixel network.
    # This usually requires a USB2Dynamixel
    serial   = dynamixel.SerialStream(port        = self.portName, baudrate = self.baudRate, timeout = 1)
    self.net = dynamixel.DynamixelNetwork(serial)
    self.idList = []
    self.nameList = []

    print "Scanning for Dynamixels..."
    for conf in self.motorConfig:
      self.idList += [conf[0]]
      self.nameList += [conf[3]]
    self.net.scan(min(self.idList),max(self.idList))
    for conf in self.motorConfig:
      if conf[0] in [motor.id for motor in self.net.get_dynamixels()]:
        print "motor " + str(conf[3]) + " has been found"
        self.motors += [Motor(self.net[conf[0]],conf[3],conf[1],conf[2])]
      else:
        print "motor " + str(conf[3]) + " has not been found"
        self.motors += [None]
    self.setAllSpeed()
        
     
  def setAllSpeed(self,speed=100, synchronized = True):
     # Ping the range of servos that are attached

     for motor in self.motors:
       if motor != None :
         motor.setSpeed(speed)
         motor.setSynchronize(synchronized)

  def setAllMotors(self,values):
    for val in values:
      if val[0] in self.idList :
        index = self.idList.index(val[0])
        if self.motors[index] != None:
          self.motors[index].setAngle(val[1]) 
    self.net.synchronize()
    time.sleep(0.1)

  def setAllMotorsByName(self,values):
    for val in values:
        if val[0] in self.nameList :
            index = self.nameList.index(val[0])
            if self.motors[index] != None:
                self.motors[index].setAngle(val[1]) 
    self.net.synchronize()
    time.sleep(0.1)

  def readAllMotors(self):
    out = []
    for motor in self.motors:
      if motor != None:
        motor.motor.read_all()
        out += [motor.motor.current_position]
      else:
        print "motor not connected"
    return out

  def readMotorByName(self,values):
     out = []
     for val in values:
      index = self.nameList.index(val[0])
      if self.motors[index]!= None:
        self.motors[index].motor.read_all()
        if val == "bottom" :
          out += [self.motors[index].motor.current_position/6.82]
        else:
          out += [self.motors[index].motor.current_position/3.41]
      else:
        print "Motor not connected"
     return out

  def moveHead(self, angleHead,angleNeck):
    print angleHead
    print angleNeck
    setAllMotorsByName([["head",angleHead],["top",angleNeck]])


