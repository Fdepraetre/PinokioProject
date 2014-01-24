import serial

class Arduino:
  def __init__(self, port, baudrate):
    """ Open the serial port with the Arduino Board """
    self.ser = serial.Serial(port, baudrate)

  def lightLed(self,r ,g ,b):
    """ Light every led with the color r,g,b """
    red = str(chr(r)) #Convert the decimal number to ASCII
    blue = str(chr(b))
    green = str(chr(g))
  
    self.ser.writelines(red+green+blue) # send color to the Arduino
  def greenLight(self):
    """Light led with green color """
    self.lightLed(0,255,0)

  def redLight(self):
    """Light led with red color """
    self.lightLed(255,30,0)

  def blueLight(self):
    """Light led with blue color """
    self.lightLed(0,0,255)




