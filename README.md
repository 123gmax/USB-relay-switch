# USB-relay-switch
Application to control USB relay switch

Source code in this repo is developed to control the USB relay which is similar to the one shown below. It typically will have a CH340 chip interfaced to AVR chip(Atiny45) on board.

<img src="https://user-images.githubusercontent.com/11489701/210126546-ae964475-808c-465e-a16a-71d094b85e71.jpg" width=50% height=50%>

The source code of the application is in Python. The GUI is developed using PyQt. Serial commands are sent using PySerial.

Note : This application is not compatible with USB relay which just has AVR chip on it which typically use v-usb firmware to communicate over USB. 

**Start the application**

Application can be started from terminal as follow. Make sure all modules(like PySerial, PyQt etc) are installed before staring.

*$python run.py*

There are also "*precompiled binary*" for Windows and Linux (Ubuntu). See folder "*bin*"
1. Ubuntu OS  : USBRealySwitch_ubuntu
2. Windows OS : TBD

See help menu after launching the application to know about each setting. 


**Screen shots**

<img src="https://user-images.githubusercontent.com/11489701/210126892-dd253afa-3bcd-4583-b20d-2e2b9293b16f.png" width=25% height=25%>



 
