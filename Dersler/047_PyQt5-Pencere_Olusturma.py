import sys
from PyQt5 import QtWidgets

def Deneme():
	app = QtWidgets.QApplication(sys.argv)
	pencere = QtWidgets.QWidget()
	pencere.setWindowTitle("Instagram AutoBot")
	pencere.show()
	sys.exit(app.exec_()) # kapat tuşuna basana kadar açık kalsın
Deneme()