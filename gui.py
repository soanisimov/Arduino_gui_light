from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import serial
from rgb2 import Ui_MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    arduinoSerial = serial.Serial('COM4',9600) #instead of COM 4 you must write your port
    ui.comboBox.addItem("Гирлянда")
    ui.comboBox.addItems(["Мигалка","Переключение","Все режимы","Переливание" ,"Переливание2" ,"Переливание3 " ,"Переливание4" ,"Цикл переливаний"])

def red_b():
	arduinoSerial.write(b'1')
	ui.label.setText("Красный")
	ui.red.setStyleSheet("color:red; border-radius: 7px; border: 1px solid black;");

def green_B():
	arduinoSerial.write(b'2')
	ui.green.setStyleSheet("color:green; border-radius: 7px; border: 1px solid black;");


def blue():
	arduinoSerial.write(b'3')
	ui.blue.setStyleSheet("color:#0010ff; border-radius: 7px; border: 1px solid black;");

def red_off():
	arduinoSerial.write(b'4')
	ui.red.setStyleSheet("color:#E1E1E1;border-radius: 7px; border: 1px solid black; background-color:#1E1E1E");
def green_off():
	arduinoSerial.write(b'5')
	ui.green.setStyleSheet("color:#E1E1E1;border-radius: 7px; border: 1px solid black; background-color:#1E1E1E");

def blue_off():
	arduinoSerial.write(b'6')
	ui.blue.setStyleSheet("color:#E1E1E1;border-radius: 7px; border: 1px solid black; background-color:#1E1E1E");

def rej():
	if(ui.comboBox.currentText() == "Гирлянда"):
		arduinoSerial.write(b'!!!!!!!!!!')
		ui.red.setStyleSheet("color:#E1E1E1;border-radius: 7px; border: 1px solid black; background-color:#1E1E1E");
		ui.green.setStyleSheet("color:#E1E1E1;border-radius: 7px; border: 1px solid black; background-color:#1E1E1E");
		ui.blue.setStyleSheet("color:#E1E1E1;border-radius: 7px; border: 1px solid black; background-color:#1E1E1E");
	if (ui.comboBox.currentText() == "Мигалка"):
		arduinoSerial.write(b'@@@@@@@@@@')
		ui.red.setStyleSheet("color:#E1E1E1;border-radius: 7px; border: 1px solid black; background-color:#1E1E1E");
		ui.green.setStyleSheet("color:#E1E1E1;border-radius: 7px; border: 1px solid black; background-color:#1E1E1E");
		ui.blue.setStyleSheet("color:#E1E1E1;border-radius: 7px; border: 1px solid black; background-color:#1E1E1E");
	if (ui.comboBox.currentText() == "Переключение"):
		arduinoSerial.write(b'$$$$$$$$$$')
		ui.red.setStyleSheet("color:#E1E1E1;border-radius: 7px; border: 1px solid black; background-color:#1E1E1E");
		ui.green.setStyleSheet("color:#E1E1E1;border-radius: 7px; border: 1px solid black; background-color:#1E1E1E");
		ui.blue.setStyleSheet("color:#E1E1E1;border-radius: 7px; border: 1px solid black; background-color:#1E1E1E");
	if (ui.comboBox.currentText() == "Все режимы"):
		arduinoSerial.write(b'!!!!@@@@$$$$^^')
		ui.red.setStyleSheet("color:#E1E1E1;border-radius: 7px; border: 1px solid black; background-color:#1E1E1E");
		ui.green.setStyleSheet("color:#E1E1E1;border-radius: 7px; border: 1px solid black; background-color:#1E1E1E");
		ui.blue.setStyleSheet("color:#E1E1E1;border-radius: 7px; border: 1px solid black; background-color:#1E1E1E");
	if (ui.comboBox.currentText() == "Переливание"):
		arduinoSerial.write(b'^^')
	if (ui.comboBox.currentText() == "Переливание2"):
		arduinoSerial.write(b'*')
	if (ui.comboBox.currentText() == "Переливание3"):
		arduinoSerial.write(b'(')
	if (ui.comboBox.currentText() == "Переливание4"):
		arduinoSerial.write(b')')
	if (ui.comboBox.currentText() == "Цикл переливаний"):
		arduinoSerial.write(b'^*()')	



ui.red.clicked.connect(red_b)
ui.green.clicked.connect(green_B)
ui.blue.clicked.connect(blue)
ui.off_red.clicked.connect(red_off)
ui.off_green.clicked.connect(green_off)
ui.off_blue.clicked.connect(blue_off)
ui.comfirm.clicked.connect(rej)
sys.exit(app.exec_())
ui.red.double_click.connect(double)
ui.offall.connect(all_off)
