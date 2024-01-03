import serial
import subprocess
val=0

def is_com4_connected():
    try:
        with serial.Serial('COM8'):
            return True
    except serial.SerialException:
        return False

while True:
    if is_com4_connected():
        if val==0:
            print("COM8 connected! Opening Python program...")
            subprocess.run(['python', 'driver.py'])
            val=1
        elif val == 1 :
            continue
    else :
        print("not connected")
        val=0 
