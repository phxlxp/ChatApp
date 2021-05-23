# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'group_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ChatApp.global_variables import user

global user


class GroupDlg(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_GroupDialog()
        self.ui.setupUi(self)


class Ui_GroupDialog(object):

    def setupUi(self, GroupDialog):
        self.GroupDialog = GroupDialog
        self.GroupDialog.setObjectName("GroupDialog")
        self.GroupDialog.resize(400, 150)
        self.GroupDialog.setMinimumSize(QtCore.QSize(400, 150))
        self.GroupDialog.setMaximumSize(QtCore.QSize(400, 150))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.GroupDialog.setFont(font)
        self.label_user_id = QtWidgets.QLabel(self.GroupDialog)
        self.label_user_id.setGeometry(QtCore.QRect(50, 20, 70, 25))
        self.label_user_id.setObjectName("label_user_id")
        self.line_edit_user_id = QtWidgets.QLineEdit(self.GroupDialog)
        self.line_edit_user_id.setGeometry(QtCore.QRect(120, 20, 190, 25))
        self.line_edit_user_id.setObjectName("line_edit_user_id")
        self.push_button_add = QtWidgets.QPushButton(self.GroupDialog, clicked=lambda: self.clicked_add())
        self.push_button_add.setGeometry(QtCore.QRect(310, 20, 40, 25))
        self.push_button_add.setObjectName("push_button_add")
        self.push_button_create = QtWidgets.QPushButton(self.GroupDialog, clicked=lambda: self.clicked_create())
        self.push_button_create.setGeometry(QtCore.QRect(50, 110, 300, 25))
        self.push_button_create.setObjectName("push_button_create")
        self.label_error = QtWidgets.QLabel(self.GroupDialog)
        self.label_error.setGeometry(QtCore.QRect(30, 65, 340, 25))
        self.label_error.setText("")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.GroupDialog)

        self.Members = []

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.GroupDialog.setWindowTitle(_translate("GroupDialog", "Create a new Group"))
        self.label_user_id.setText(_translate("GroupDialog", "User ID:"))
        self.push_button_add.setText(_translate("GroupDialog", "Add"))
        self.push_button_create.setText(_translate("GroupDialog", "Create group"))

    ####################################################################################################################

    """ USER GENERATED CODE STARTS HERE """

    ####################################################################################################################

    # try to add a user to the group | push_button_add
    def clicked_add(self):
        user_id = self.line_edit_user_id.text()
        if user.check_user_exists(user_id) and user_id not in self.Members:
            self.label_error.setText("")
            self.line_edit_user_id.clear()
            self.Members.append(user_id)
        else:
            self.label_error.setText("This did not work. Please try another id.")

    # try to create a group | push_button_create
    def clicked_create(self):
        if len(self.Members) >= 2:
            user.create_group(self.Members)
            self.GroupDialog.close()
        else:
            self.label_error.setText("Add more users to create a new group.")
