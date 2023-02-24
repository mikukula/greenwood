from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QDialog    
from PyQt6 import uic
import sys

class Dashboard(QMainWindow):
    def __init__(self):
        super(Dashboard, self).__init__()

        uic.loadUi("ui\dashboard.ui", self)
        
        self.show()
        self.loginScreen = LogIn()
        

class LogIn(QDialog):
    def __init__(self):
        super(LogIn, self).__init__()
        uic.loadUi("ui\login.ui", self)
        self.show()
        

app = QApplication(sys.argv)
UIWindow = LogIn()
app.exec()