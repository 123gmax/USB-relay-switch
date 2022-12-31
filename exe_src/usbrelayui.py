# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './usbrelay.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(251, 213)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Reset_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Reset_Button.setGeometry(QtCore.QRect(10, 60, 89, 25))
        self.Reset_Button.setObjectName("Reset_Button")
        self.COM_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.COM_Name.setGeometry(QtCore.QRect(90, 20, 113, 25))
        self.COM_Name.setObjectName("COM_Name")
        self.COM_label = QtWidgets.QLabel(self.centralwidget)
        self.COM_label.setGeometry(QtCore.QRect(10, 23, 71, 17))
        self.COM_label.setObjectName("COM_label")
        self.ON_Button = QtWidgets.QPushButton(self.centralwidget)
        self.ON_Button.setGeometry(QtCore.QRect(10, 110, 89, 25))
        self.ON_Button.setObjectName("ON_Button")
        self.OFF_Button = QtWidgets.QPushButton(self.centralwidget)
        self.OFF_Button.setGeometry(QtCore.QRect(110, 110, 89, 25))
        self.OFF_Button.setObjectName("OFF_Button")
        self.Delay_Value = QtWidgets.QLineEdit(self.centralwidget)
        self.Delay_Value.setGeometry(QtCore.QRect(150, 60, 31, 25))
        self.Delay_Value.setObjectName("Delay_Value")
        self.Delay_label = QtWidgets.QLabel(self.centralwidget)
        self.Delay_label.setGeometry(QtCore.QRect(110, 63, 41, 17))
        self.Delay_label.setObjectName("Delay_label")
        self.label_s = QtWidgets.QLabel(self.centralwidget)
        self.label_s.setGeometry(QtCore.QRect(182, 63, 16, 16))
        self.label_s.setObjectName("label_s")
        self.label_Message = QtWidgets.QLabel(self.centralwidget)
        self.label_Message.setGeometry(QtCore.QRect(10, 143, 231, 20))
        self.label_Message.setObjectName("label_Message")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 251, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuHELP = QtWidgets.QMenu(self.menuBar)
        self.menuHELP.setObjectName("menuHELP")
        MainWindow.setMenuBar(self.menuBar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuHELP.addAction(self.actionHelp)
        self.menuBar.addAction(self.menuHELP.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "USB Relay Controller"))
        self.Reset_Button.setText(_translate("MainWindow", "Reset"))
        self.COM_label.setText(_translate("MainWindow", "Serial Port"))
        self.ON_Button.setText(_translate("MainWindow", "ON"))
        self.OFF_Button.setText(_translate("MainWindow", "OFF"))
        self.Delay_label.setText(_translate("MainWindow", "Delay"))
        self.label_s.setText(_translate("MainWindow", "S"))
        self.label_Message.setText(_translate("MainWindow", "TextLabel"))
        self.menuHELP.setTitle(_translate("MainWindow", "Help"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
