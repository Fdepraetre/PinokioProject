import os
import dynamixel
import time
import random
import sys
import subprocess
import optparse
import yaml

class SelfMotor:

  def __init__(self,motor,minAngle = 0,maxAngle = 300 ):
    self.motor = motor
    self.maxAngle = maxAngle
    self.minAngle = minAngle
    self.valeur = 0


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
    fact = 3.41
    self.motor.goal_position =int(fact * angle )

  def setSpeed(self,speed):
       self.motor.moving_speed = speed

  def setSynchronize(self,synchronized):
       self.motor.synchronized = synchronized

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

    print "Scanning for Dynamixels..."
    for conf in self.motorConfig:
      self.idList += [conf[0]]
    self.net.scan(min(self.idList),max(self.idList))
    for conf in self.motorConfig:
      if conf[0] in [motor.id for motor in self.net.get_dynamixels()]:
        print "motor " + str(conf[3]) + " has been found"
        self.motors += [SelfMotor(self.net[conf[0]],conf[1],conf[2])]
      else:
        print "motor " + str(conf[3]) + " has not been found"
        self.motors += [None]
        
        
     
  def setAllSpeed(self,speed=100, synchronized = True):
     # Ping the range of servos that are attached

     for motor in self.motors:
       if motor != None :
         motor.setSpeed(speed)
         motor.setSynchronize(synchronized)

  def setAllMotors(self,values):
    for val in values:
      index = self.idList.index(val[0])
      if self.motors[index] != None:
       self.motors[index].setAngle(val[1]) 
    self.net.synchronize()
    time.sleep(2)

def validateInput(userInput, rangeMin, rangeMax):
    '''
    Returns valid user input or None
    '''
    try:
        inTest = int(userInput)
        if inTest < rangeMin or inTest > rangeMax:
            print "ERROR: Value out of range [" + str(rangeMin) + '-' + str(rangeMax) + "]"
            return None
    except ValueError:
        print("ERROR: Please enter an integer")
        return None
    
    return inTest



if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-c", "--clean",
                      action="store_true", dest="clean", default=False,
                      help="Ignore the settings.yaml file if it exists and \
                      prompt for new settings.")
    
    (options, args) = parser.parse_args()
    
    # Look for a settings.yaml file
    settingsFile = 'settings.yaml'
    if not options.clean and os.path.exists(settingsFile):
        with open(settingsFile, 'r') as fh:
            settings = yaml.load(fh)
    # If we were asked to bypass, or don't have settings
    else:
        settings = {}
        if os.name == "posix":
            portPrompt = "Which port corresponds to your USB2Dynamixel? \n"
            # Get a list of ports that mention USB
            try:
                possiblePorts = subprocess.check_output('ls /dev/ | grep -i usb',
                                                        shell=True).split()
                possiblePorts = ['/dev/' + port for port in possiblePorts]
            except subprocess.CalledProcessError:
                sys.exit("USB2Dynamixel not found. Please connect one.")
                
            counter = 1
            portCount = len(possiblePorts)
            for port in possiblePorts:
                portPrompt += "\t" + str(counter) + " - " + port + "\n"
                counter += 1
            portPrompt += "Enter Choice: "
            portChoice = None
            while not portChoice:                
                portTest = raw_input(portPrompt)
                portTest = validateInput(portTest, 1, portCount)
                if portTest:
                    portChoice = possiblePorts[portTest - 1]

        else:
            portPrompt = "Please enter the port name to which the USB2Dynamixel is connected: "
            portChoice = raw_input(portPrompt)
    
        settings['port'] = portChoice
        
        # Baud rate
        baudRate = None
        while not baudRate:
            brTest = raw_input("Enter baud rate [Default: 1000000 bps]:")
            if not brTest:
                baudRate = 1000000
            else:
                baudRate = validateInput(brTest, 9600, 1000000)
                    
        settings['baudRate'] = baudRate#
        
        # Servo ID
        highestServoId = None
        while not highestServoId:
            hsiTest = raw_input("Please enter the highest ID of the connected servos: ")
            highestServoId = validateInput(hsiTest, 1, 255)
        
        settings['highestServoId'] = highestServoId
        
        # Save the output settings to a yaml file
        with open(settingsFile, 'w') as fh:
            yaml.dump(settings, fh)
            print("Your settings have been saved to 'settings.yaml'. \nTo " +
                   "change them in the future either edit that file or run " +
                   "this example with -c.")

    motorControler = MotorControl(settings)
    motorControler.setAllSpeed()
    while True:
      motorControler.setAllMotors([[5,280],[4,50]])
      motorControler.setAllMotors([[5,240],[4,150]])
      motorControler.setAllMotors([[5,280],[4,100]])
      motorControler.setAllMotors([[5,240],[4,50]])
