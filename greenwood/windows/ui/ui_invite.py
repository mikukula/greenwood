# Form implementation generated from reading ui file 'c:\Users\mikuk\Documents\yr2gp\greenwood\greenwood\windows\ui\invite.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 355)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\mikuk\\Documents\\yr2gp\\greenwood\\greenwood\\windows\\ui\\../assets/greenwood_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.formLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 90, 281, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.ItemRole.SpanningRole, spacerItem)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.ItemRole.SpanningRole, spacerItem1)
        self.invite = QtWidgets.QPushButton(parent=Dialog)
        self.invite.setGeometry(QtCore.QRect(100, 240, 196, 28))
        self.invite.setObjectName("invite")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 280, 201, 61))
        self.label_3.setStyleSheet("color: #006D2C;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(130, 20, 141, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("c:\\Users\\mikuk\\Documents\\yr2gp\\greenwood\\greenwood\\windows\\ui\\../assets/logo_text.png"))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Invite"))
        self.label.setText(_translate("Dialog", "Email"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.invite.setText(_translate("Dialog", "Invite Member"))
        self.label_3.setText(_translate("Dialog", "Greenwood software is invite only.\n"
"Please provide credentials for\n"
"your member."))
