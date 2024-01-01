# gaming_controller
gaming controller which can also be toggled into mouse controller (if needed)

The idea is to simulate the pressing and releasing of keyboard/mouse buttons using Arduino.

Arduino is programmed in such a way that it sends data containing a start bit/character 'm' in this case, along with other 1's and 0's depending on the pressed button.

The driver program receives data in the same order and uses it to simulate the pressing and releasing of the assigned key.
