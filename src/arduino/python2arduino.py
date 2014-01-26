import serial
import settings

class Arduino:
  def __init__(self, path=None):
    """ Open the serial port with the Arduino Board """
    if path != None:
      arduinoSettings = settings.ArduinoSettings(path).get()
    else:
      arduinoSettings = settings.ArduinoSettings().get()

    self.ser = serial.Serial(arduinoSettings["port"], arduinoSettings["baudrate"])

  def lightLed(self, r, g, b):
    """ Light every led with the color r,g,b """
    red = str(chr(r)) #Convert the decimal number to ASCII
    blue = str(chr(b))
    green = str(chr(g))
  
    self.ser.writelines('l'+red+green+blue+'\n') # send color to the Arduino
  def greenLight(self):
    """Light led with green color """
    self.lightLed(0, 255, 0)

  def redLight(self):
    """Light led with red color """
    self.lightLed(255, 0, 0)

  def blueLight(self):
    """Light led with blue color """
    self.lightLed(0, 0, 255)

  def fadeLed(self, color, period):
    self.ser.writelines('f'+color+str(chr(period/100))+'\n')





