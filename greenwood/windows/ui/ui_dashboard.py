# Form implementation generated from reading ui file 'c:\Users\mikuk\Documents\yr2gp\greenwood\greenwood\windows\ui\dashboard.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1281, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1281, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1281, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\mikuk\\Documents\\yr2gp\\greenwood\\greenwood\\windows\\ui\\../assets/greenwood_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1281, 121))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: #B3ADAD;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.loginButton = QtWidgets.QPushButton(parent=self.frame)
        self.loginButton.setEnabled(True)
        self.loginButton.setGeometry(QtCore.QRect(1230, 0, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.loginButton.setFont(font)
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.loginButton.setStyleSheet("QPushButton:hover{\n"
"    text-decoration: underline solid;\n"
"    color: #06D036;\n"
"}\n"
"\n"
"QPushButton{\n"
"    border-radius: 48px;\n"
"}")
        self.loginButton.setCheckable(False)
        self.loginButton.setFlat(True)
        self.loginButton.setObjectName("loginButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 40, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton:hover{\n"
"    text-decoration: underline solid;\n"
"    color: #06D036;\n"
"}\n"
"\n"
"QPushButton{\n"
"    border-radius:48px;\n"
"}")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.inviteButton = QtWidgets.QPushButton(parent=self.frame)
        self.inviteButton.setGeometry(QtCore.QRect(1172, 0, 51, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inviteButton.setFont(font)
        self.inviteButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.inviteButton.setStyleSheet("QPushButton:hover{\n"
"    text-decoration: underline solid;\n"
"    color: #06D036;\n"
"}\n"
"\n"
"QPushButton{\n"
"    border-radius: 48px;\n"
"}")
        self.inviteButton.setObjectName("inviteButton")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 120, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.locationBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.locationBox.setGeometry(QtCore.QRect(50, 120, 141, 31))
        self.locationBox.setObjectName("locationBox")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 130, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(690, 120, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.dateBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.dateBox.setGeometry(QtCore.QRect(320, 120, 121, 31))
        self.dateBox.setObjectName("dateBox")
        self.tagBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.tagBox.setGeometry(QtCore.QRect(540, 120, 141, 31))
        self.tagBox.setObjectName("tagBox")
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(50, 180, 256, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(parent=self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(50, 440, 256, 192))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(parent=self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(380, 440, 256, 192))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(990, 430, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_4.setObjectName("label_4")
        self.audioUploadField = QtWidgets.QLabel(parent=self.centralwidget)
        self.audioUploadField.setGeometry(QtCore.QRect(980, 270, 151, 151))
        self.audioUploadField.setStyleSheet("QLabel{\n"
"    border: 2px dashed black\n"
"\n"
"}")
        self.audioUploadField.setText("")
        self.audioUploadField.setPixmap(QtGui.QPixmap("c:\\Users\\mikuk\\Documents\\yr2gp\\greenwood\\greenwood\\windows\\ui\\../assets/upload.png"))
        self.audioUploadField.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.audioUploadField.setObjectName("audioUploadField")
        self.fileButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.fileButton.setGeometry(QtCore.QRect(1010, 460, 93, 28))
        self.fileButton.setStyleSheet("")
        self.fileButton.setObjectName("fileButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1281, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Greenwood"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "View Reports"))
        self.inviteButton.setText(_translate("MainWindow", "Invite"))
        self.label.setText(_translate("MainWindow", "Location"))
        self.label_2.setText(_translate("MainWindow", "Date"))
        self.label_3.setText(_translate("MainWindow", "Tags"))
        self.label_4.setText(_translate("MainWindow", "Upload Audio"))
        self.fileButton.setText(_translate("MainWindow", "Choose file"))
