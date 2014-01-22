import serial
ser = serial.Serial('\\.\COM5', 9600) # Establish the connection on a specific port

r=str(chr(150))
g=str(chr(0))
b=str(chr(0))
ser.writelines(r+g+b) # Convert the decimal number to ASCII then send it to the Arduino
     
while True:
	b=str(chr(0))
