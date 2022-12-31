import sys
import time
from PyQt5 import QtWidgets, uic

# Local modules
import serial_port as sp

# Get the template file
UI_TEMPLATE = "./usbrelay.ui"
HELP_UI_TEMPLATE = "./help.ui"


class HELP_UI:
    def __init__(self):
        self.HelpWindow = uic.loadUi(HELP_UI_TEMPLATE)
        self.HelpWindow.show()

class UI:
    def __init__(self):
        self.delay = 1
        self.MainWindow = uic.loadUi(UI_TEMPLATE)

        # Reset
        self.MainWindow.Reset_Button.clicked.connect(self.RESET_Click)

        # OFF
        self.MainWindow.OFF_Button.clicked.connect(self.OFF_Click)

        # ON
        self.MainWindow.ON_Button.clicked.connect(self.ON_Click)

        # COM port name
        self.MainWindow.COM_Name.setText("COM?")

        # Delay value
        self.MainWindow.Delay_Value.setText("5")

        # Message label
        self.MainWindow.label_Message.setText("")

        # Help
        self.MainWindow.actionHelp.triggered.connect(self.Help_Click)

        # Show window
        self.MainWindow.show()

    def Refresh_Display(self):
        self.MainWindow.label_Message.setText("")

    def RESET_Click(self):
        # print("Reset click")
        self.Refresh_Display()
        if not Reset_Operations(self.MainWindow):
            self.MainWindow.label_Message.setText("Invalid serial port!")

    def ON_Click(self):
        # print('On click')
        self.Refresh_Display()
        if not Relay_ON(self.MainWindow):
            self.MainWindow.label_Message.setText("Invalid serial port!")

    def OFF_Click(self):
        # print('Off Click')
        self.Refresh_Display()
        if not Relay_OFF(self.MainWindow):
            self.MainWindow.label_Message.setText("Invalid serial port!")

    def Help_Click(self):
        self.ui = HELP_UI()
        #print("Help")

def Get_Com_Port(MainWindow):
    COM_PortName = MainWindow.COM_Name.text()
    COM_PortName = COM_PortName.replace(" ", "")
    # print("Port name :" + COM_PortName)
    if "?" in COM_PortName:
        # Com port not set
        return None
    if "tty" in COM_PortName or "COM" in COM_PortName:
        return COM_PortName
    return "COM" # Some return


'''
Action to be performed when Reset button is clicked 
'''


def Reset_Operations(MainWindow):
    delay_str = MainWindow.Delay_Value.text()
    delay = 1  # Default delay
    if delay_str.isnumeric():
        delay = int(delay_str, 10)
    if Relay_ON(MainWindow):
        time.sleep(delay)
        Relay_OFF(MainWindow)
        return True
    else:
        return False



'''
Turns the Relay ON 
'''


def Relay_ON(MainWindow):
    COM_PortName = Get_Com_Port(MainWindow)
    if COM_PortName is None:
        # Invalid configuration of COM port
        return False
    return sp.Turn_Relay_ON(COM_PortName)


'''
Turns the Relay OFF
'''


def Relay_OFF(MainWindow):
    COM_PortName = Get_Com_Port(MainWindow)
    if COM_PortName is None:
        # Invalid configuration of COM port
        return False
    return sp.Turn_Relay_OFF(COM_PortName)


if __name__ == "__main__":
    APP = QtWidgets.QApplication(sys.argv)
    my_ui = UI()
    sys.exit(APP.exec())
