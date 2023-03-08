from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QDialog, QLabel    
from PyQt6 import uic, QtCore
from PyQt6.QtGui import QPixmap
from dashboard_manager import DashboardManager
from PyQt6.QtCore import Qt
import sys

class Dashboard(QMainWindow):
    def __init__(self):
        super(Dashboard, self).__init__()
        self.ui = uic.loadUi("ui\dashboard.ui", self)

        #####################SET UP DROP BOX######################

        self.audioUploadField = DropBox(parent=self.ui.centralwidget)
        self.audioUploadField.setGeometry(QtCore.QRect(980, 270, 151, 151))
        self.audioUploadField.setStyleSheet("QLabel{\n"
"    border: 2px dashed black\n"
"\n"
"}")
        self.audioUploadField.setText("")
        self.audioUploadField.setPixmap(QPixmap("../windows/assets/upload.png"))
        self.audioUploadField.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.audioUploadField.setObjectName("audioUploadField")

        ###########################################################
        self.show()
        self.loginScreen = LogIn(parent=self)

class LogIn(QDialog):
    def __init__(self, parent=None):
        super(LogIn, self).__init__(parent)
        self.ui = uic.loadUi("ui\login.ui", self)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint);
        self.show()

class DropBox(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
    
    def dragEnterEvent(self, event):

        if (event.mimeData().hasUrls() and
             self.__isExtension(".wav", event)):
           event.accept()
           print("can enter")
        else:
           event.ignore()

    def dragMoveEvent(self, event):
        
        if (event.mimeData().hasUrls() and 
            self.__isExtension(".wav", event)):
           event.accept()
           print("can move")
        else:
           event.ignore()
        
    def dropEvent(self, event):
        if (event.mimeData().hasUrls() and
            self.__isExtension(".wav", event)):
           event.accept()
           print("can drop")
        else:
           event.ignore()
    
    def __isExtension(self, extension, event):

        if(event.mimeData().text()[-4:] == extension):
            return True
        else:
            return False


        
####### set up
app = QApplication(sys.argv)
UIWindow = Dashboard()
manager = DashboardManager(UIWindow)
manager.addToComboBox(UIWindow.ui.locationBox, "test1")

####### drop box setup
#def dragEnterEvent(UIWindow.ui)

app.exec()