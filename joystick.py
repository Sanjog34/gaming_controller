import serial
import subprocess
val=0

def is_com4_connected():
    try:
        with serial.Serial('COM8'): #put the name of port arduino is connected to.
            return True
    except serial.SerialException:
        return False

while True:
    if is_com4_connected():
        if val==0:
            # print("COM8 connected! Opening Python program...")
            subprocess.run(['python', 'joystick.py'])
            val=1
        elif val == 1 :
            # print("connection established")
            continue
    else :
        # print("not connected")
        val=0 
