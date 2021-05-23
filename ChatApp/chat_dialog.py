# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from ChatApp.global_variables import user

global user


class ChatDlg(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ChatDialog()
        self.ui.setupUi(self)


class Ui_ChatDialog(object):

    def setupUi(self, ChatDialog):
        self.ChatDialog = ChatDialog
        self.ChatDialog.setObjectName("ChatDialog")
        self.ChatDialog.resize(400, 110)
        self.ChatDialog.setMinimumSize(QtCore.QSize(400, 110))
        self.ChatDialog.setMaximumSize(QtCore.QSize(400, 110))
        self.pushButton = QtWidgets.QPushButton(self.ChatDialog, clicked=lambda: self.clicked_add())
        self.pushButton.setGeometry(QtCore.QRect(310, 20, 40, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_user_id = QtWidgets.QLabel(self.ChatDialog)
        self.label_user_id.setGeometry(QtCore.QRect(50, 20, 70, 25))
        self.label_user_id.setObjectName("label_user_id")
        self.label_error = QtWidgets.QLabel(self.ChatDialog)
        self.label_error.setGeometry(QtCore.QRect(30, 70, 340, 25))
        self.label_error.setText("")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.line_edit_user_id = QtWidgets.QLineEdit(self.ChatDialog)
        self.line_edit_user_id.setGeometry(QtCore.QRect(120, 20, 190, 25))
        self.line_edit_user_id.setObjectName("line_edit_user_id")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.ChatDialog)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.ChatDialog.setWindowTitle(_translate("ChatDialog", "Add a new Chat"))
        self.pushButton.setText(_translate("ChatDialog", "Add"))
        self.label_user_id.setText(_translate("ChatDialog", "User ID:"))

    ####################################################################################################################

    """ USER GENERATED CODE STARTS HERE """

    ####################################################################################################################

    # try to create a chat | push_button_add
    def clicked_add(self):
        user_id = self.line_edit_user_id.text()
        if user.add_chat_partner(user_id):
            self.ChatDialog.close()
        else:
            self.label_error.setText("This user id does not exist. Please try again.")
