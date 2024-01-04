import serial.tools.list_ports
import serial
import subprocess
val=0


def is_com_connected():
    try:
        available_ports = serial.tools.list_ports.comports()
        if len(available_ports)==0 :
            # print("no ports detected")
            return False
        selected_port = available_ports[0].device
        with serial.Serial(selected_port):
            return True
    except serial.SerialException:
        return False

while True:
    if is_com_connected():
        if val==0:
            # print(" connected! Opening Python program...")
            subprocess.run(['python', 'joystick.py'])
            val=1
        elif val == 1 :
            # print("connection established")
            continue
    else :
    #   print("not connected")
      val=0 
