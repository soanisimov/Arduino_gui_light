# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rgb.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(299, 465)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.red = QtWidgets.QPushButton(self.centralwidget)
        self.centralwidget.setStyleSheet("background-color:#272727")
        self.red.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.red.setObjectName("red")
        self.offall = QtWidgets.QPushButton(self.centralwidget)
        self.offall.setGeometry(QtCore.QRect(210, 130, 75, 23))
        self.offall.setObjectName("offall")
        self.offall.setStyleSheet("color:#E1E1E1;border-radius: 7px; border: 1px solid black; background-color:#1E1E1E");
        self.green = QtWidgets.QPushButton(self.centralwidget)
        self.green.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.green.setObjectName("green")
        self.blue = QtWidgets.QPushButton(self.centralwidget)
        self.blue.setGeometry(QtCore.QRect(10, 90, 75, 23))
        self.blue.setObjectName("blue")
        self.blue.setStyleSheet("color:#E1E1E1;border-radius: 7px; border: 1px solid black; background-color:#1E1E1E");
        self.red.setStyleSheet("color:#E1E1E1; border-radius: 7px; border: 1px solid black; background-color:#1E1E1E");
        self.green.setStyleSheet("color:#E1E1E1;border-radius: 7px; border: 1px solid black;background-color:#1E1E1E");
        self.off_red = QtWidgets.QPushButton(self.centralwidget)
        self.off_red.setGeometry(QtCore.QRect(210, 10, 75, 23))
        self.off_red.setObjectName("off_red")
        self.off_green = QtWidgets.QPushButton(self.centralwidget)
        self.off_green.setGeometry(QtCore.QRect(210, 50, 75, 23))
        self.off_green.setObjectName("off_green")
        self.off_blue = QtWidgets.QPushButton(self.centralwidget)
        self.off_blue.setGeometry(QtCore.QRect(210, 90, 75, 23))
        self.off_blue.setObjectName("off_blue")
        self.off_red.setStyleSheet("color:#FE7576;border-radius: 7px; border: 1px solid black; background-color:#1E1E1E")
        self.off_blue.setStyleSheet("color:#FE7576;border-radius: 7px; border: 1px solid black; background-color:#1E1E1E")
        self.off_green.setStyleSheet("color:#FE7576;border-radius: 7px; border: 1px solid black; background-color:#1E1E1E")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 260, 281, 161))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("QPushButton{\n"
"  background-color: white;\n"
"  width: 75px;\n"
"  height: 50px;\n"
"  font-size: 14px;\n"
"  font-weight: bold;\n"
"  border: none;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: silver;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 160, 110, 22))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comfirm = QtWidgets.QPushButton(self.centralwidget)
        self.comfirm.setGeometry(QtCore.QRect(10, 200, 91, 23))
        self.comfirm.setObjectName("comfirm")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 299, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.comboBox.setStyleSheet("color:#E1E1E1;")
        self.comfirm.setStyleSheet("color:#E1E1E1;")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Светильник"))
        self.red.setText(_translate("MainWindow", "Красный"))
        self.green.setText(_translate("MainWindow", "Зеленый"))
        self.blue.setText(_translate("MainWindow", "Синий"))
        self.off_red.setText(_translate("MainWindow", "Выключить"))
        self.off_green.setText(_translate("MainWindow", "Выключить"))
        self.off_blue.setText(_translate("MainWindow", "Выключить"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.comfirm.setText(_translate("MainWindow", "Подтвердить"))
        self.offall.setText(_translate("MainWindow", "Подтвердить"))
