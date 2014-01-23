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

  def setAngle(self,angle):
    ''' Set the motor angle '''
    if angle > self.maxAngle or angle < self.minAngle:
      print "Angle out of range"
      print "motor : " + str(self.name)
      print "value : " + str(angle)
      print "range : [" + str(self.maxAngle) + "," + str(self.minAngle) + "]"
    else:
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
      if self.name == "bottom":
        fact = 6.82
      else:
        fact = 3.41
      self.motor.read_all()
#      time.sleep(0.1)
      return self.motor.current_position / fact
  
  def getRange(self):
    return [self.minAngle,self.maxAngle]


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
        
     
  def setAllSpeed(self,speed=100):
    ''' Set the speed for every motors '''
     # Ping the range of servos that are attached
     for motor in self.motors:
       if motor != None :
         motor.setSpeed(speed)

  def setSynchronize(self,synchronized = True):
    ''' Set the synchronization for every motors '''
     for motor in self.motors:
       if motor != None :
         motor.setSynchronize(synchronized)

  def setMotorsById(self,values):
    ''' Set the angle motor by ID ( values is a list of tuple [ motorId , Angle]) '''
    for val in values:
      if val[0] in self.idList :
        index = self.idList.index(val[0])
        if self.motors[index] != None:
          self.motors[index].setAngle(val[1]) 
    self.net.synchronize()
    #time.sleep(0.1)

  def setMotorsByName(self,values):
    ''' Set the angle motor by name ( values is a list of tuple [ motorName , Angle]) '''
    for val in values:
        if val[0] in self.nameList :
            index = self.nameList.index(val[0])
            if self.motors[index] != None:
                self.motors[index].setAngle(val[1]) 
    self.net.synchronize()
    #time.sleep(0.1)

  def readAllMotors(self):
    '''Return each motor position in tick motor  '''
    out = []
    for motor in self.motors:
      if motor != None:
        motor.motor.read_all()
        out += [motor.readMotorPosition()]
      else:
        print "motor not connected"
    return out

  def readMotorByName(self,values):
    '''Return each motor position in values in tick motor  '''
     out = []
     for val in values:
      index = self.nameList.index(val)
      if self.motors[index]!= None:
        self.motors[index].motor.read_all()
        out += [self.motors[index].readMotorPosition()]
      else:
        print "Motor not connected"
     return out

  def getRangeByName(self,names):
    ''' Return the motor range for motor in names '''
    out = {}
    for name in names:
      index = self.nameList.index(name)
      if self.motors[index]!= None:
        out[name] = self.motors[index].getRange()
      else:
        print "Motor not connected"
    return out


