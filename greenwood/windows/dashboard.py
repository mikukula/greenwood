from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QDialog, QLabel, QFileDialog    
from PyQt6 import uic, QtCore
from PyQt6.QtGui import QPixmap
from PyQt6.QtSql import QSqlDatabase
from dashboard_manager import DashboardManager
from pathlib import Path
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
        self.ui.fileButton.clicked.connect(self.chooseFile)
        self.ui.loginButton.clicked.connect(self.openLoginScreen)
        self.ui.inviteButton.clicked.connect(self.openInviteScreen)

        self.show()
        self.openLoginScreen()
        
        connect()

    def openLoginScreen(self):

        self.loginScreen = LogIn(parent=self)

    def openInviteScreen(self):

        self.inviteScreen = InviteScreen(parent=self)

    def chooseFile(self):

        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)
        print(fname[0])


class LogIn(QDialog):
    def __init__(self, parent=None):
        super(LogIn, self).__init__(parent)
        self.ui = uic.loadUi("ui\login.ui", self)
        self.parent = parent

        self.ui.logInButton.clicked.connect(self.loggedIn)

        parent.setEnabled(False)
        self.setEnabled(True)
        self.show()

    def loggedIn(self):

        self.parent.setEnabled(True)
        self.close()


class InviteScreen(QDialog):
    def __init__(self, parent = None):
        super(InviteScreen, self).__init__(parent)
        self.ui = uic.loadUi("ui\invite.ui", self)
        self.parent = parent

        self.ui.invite.clicked.connect(self.invited)

        parent.setEnabled(False)
        self.setEnabled(True)
        self.show()

    def invited(self):

        self.parent.setEnabled(True)
        self.close()

class DropBox(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
    
    def dragEnterEvent(self, event):

        if (event.mimeData().hasUrls() and
            isExtension(".wav", event.mimeData().text())):
           event.accept()
        else:
           event.ignore()

    def dragMoveEvent(self, event):
        
        if (event.mimeData().hasUrls() and 
            isExtension(".wav", event.mimeData().text())):
           event.accept()

        else:
           event.ignore()
        
    def dropEvent(self, event):
        if (event.mimeData().hasUrls() and
            isExtension(".wav", event.mimeData().text())):
           event.accept()
           print("can drop")
        else:
           event.ignore()
    
    
#extension checking
def isExtension(extension, filePath):

    if(filePath[-4:] == extension):
        return True
    else:
        return False
    
#database
def connect():
    db = QSqlDatabase.addDatabase("QSQLIte", "(description= (retry_count=0)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.ap-singapore-1.oraclecloud.com))(connect_data=(service_name=g6c4c0c6d559479_greenwood_low.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))")
    db.setHostName("bigblue")
    db.setDatabaseName("flightdb")
    db.setUserName("acarlson")
    db.setPassword("1uTbSbAs")
    ok = db.open()
        
####### set up
app = QApplication(sys.argv)
UIWindow = Dashboard()
manager = DashboardManager(UIWindow)
manager.addToComboBox(UIWindow.ui.locationBox, "test1")

####### drop box setup

app.exec()