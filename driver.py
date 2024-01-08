import serial.tools.list_ports
import serial
import pydirectinput #can use pyautogui
import time
# time.sleep(0.01)
keysDown = {}
pydirectinput.PAUSE=0
	
def keyDown(key):
	if key not in keysDown: 
		keysDown[key] = True
		pydirectinput.keyDown(key)
	# print('Down: ', key)


def keyUp(key):
	if key in keysDown:
		del(keysDown[key])
		pydirectinput.keyUp(key)
		# print('Up: ', key)


def handleJoyStickAsArrowKeys(m,e,b,n,x,y):
	if m == 1:
		current_position=pydirectinput.position()	
		i, j =current_position
		# print(x,y,m,i,j)
		if x == 2:
			i=i+2
			pydirectinput.moveTo(i,j)
			# print("New Mouse Position:", pydirectinput.position())
		elif x ==0:
			i=i-2
			pydirectinput.moveTo(i,j)
			# print("New Mouse Position:", pydirectinput.position())
		if y == 2:
			j=j-2
			pydirectinput.moveTo(i,j)
			# print("New Mouse Position:", pydirectinput.position())
		elif y == 0:
			j=j+2
			pydirectinput.moveTo(i,j)
			# print("New Mouse Position:", pydirectinput.position())	
		if b == 1:
			pydirectinput.leftClick()
			pydirectinput.mouseUp()	
		if n == 1:
			pydirectinput.rightClick()
			pydirectinput.mouseUp()
		if e == 1 :
			pydirectinput.click()
		elif x == 1 and y == 1 :
			# print("New Mouse Position:", pydirectinput.position())
			pydirectinput.moveTo(i, j)
	elif m == 0:
		if y == 0:
			keyDown('down')
			keyUp('up')
			# print("down")
		elif y == 2:
			keyDown('up')
			keyUp('down')
			# print("up")
		else:
			keyUp('down')
			keyUp('up')
		
		if x == 0:
			keyDown('left')
			keyUp('right')
			# print("left")
		elif x == 2:
			keyDown('right')
			keyUp('left')
			# print("right")
		else:
			keyUp('right')
			keyUp('left')
			
		if e==1:
			keyDown('enter')
			# print("enter")
		else:
			keyUp('enter')
		if b==1:
			keyDown('s')
			# print("s")
		else :
			keyUp('s')
		if n==1:
			keyDown('space')
			# print("space")
		else: 
			keyUp('space')

available_ports = serial.tools.list_ports.comports()
selected_port = available_ports[0].device
arduino=serial.Serial(selected_port,115200,timeout=.1)		
while True :
		rawdata = arduino.readline()
		data =str(rawdata.decode('utf-8'))
		if data.startswith("m"):
			e,b,n,m,x,y=(int(data[i]) for i in range(6))
			handleJoyStickAsArrowKeys(m,e,b,n,x,y)

