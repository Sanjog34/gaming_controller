# gaming_controller




# Arduino code.
the arduino sends the button states and joystick states through COM port at 115200 baud rate.

# driver code.
It involves providing instructions on which key to press based on the received data. The data is read from the COM port at a baud rate of 115200.

*Baud rate for arduino and driver should be same*

# joystick code
The controller itself is not referred to as a "controller". Rather, it simulates the pressing and releasing of keyboard keys. To utilize it, initially, one must connect the controller and subsequently launch the driver program on the computer. However, if the connection between the computer and the controller experiences interruptions, such as a loose cable or accidental USB disconnection, the program terminates, necessitating reopening whenever such disruption occurs. The joystick program addresses this issue by detecting the port's connection status. When the port is connected, the driver code executes automatically. If the port is not connected, the program waits until a connection to the port is established.

*make sure the driver and joystick program is in same folder*
