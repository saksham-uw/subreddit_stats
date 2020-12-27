from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(400, 280, 1200, 600)
    win.setWindowTitle("First app")

    label = QtWidgets.QLabel(win)
    label.setText("my first label")
    label.move(50, 50)

    win.show()
    sys.exit(app.exec_())

window()