# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets, QtGui
from ChatApp.chat_dialog import ChatDlg
from ChatApp.group_dialog import GroupDlg
from ChatApp.global_variables import user

global user


class Ui_MainWindow(object):

    def __init__(self, main_window):
        self.MainWindow = main_window
        self.current_chat_id = None
        self.chat_name = None
        self.current_group_id = None

    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(800, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainWindow.sizePolicy().hasHeightForWidth())
        self.MainWindow.setSizePolicy(sizePolicy)
        self.MainWindow.setMinimumSize(QtCore.QSize(800, 560))
        self.MainWindow.setMaximumSize(QtCore.QSize(800, 560))
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.push_button_logout = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clicked_logout())
        self.push_button_logout.setGeometry(QtCore.QRect(700, 10, 89, 25))
        self.push_button_logout.setObjectName("push_button_logout")
        self.push_button_delete = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clicked_delete())
        self.push_button_delete.setGeometry(QtCore.QRect(568, 10, 121, 25))
        self.push_button_delete.setObjectName("push_button_delete")
        self.push_button_chat = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clicked_chat())
        self.push_button_chat.setGeometry(QtCore.QRect(10, 10, 131, 25))
        self.push_button_chat.setObjectName("push_button_chat")
        self.push_button_group = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clicked_group())
        self.push_button_group.setGeometry(QtCore.QRect(150, 10, 151, 25))
        self.push_button_group.setObjectName("push_button_group")
        self.label_chats = QtWidgets.QLabel(self.centralwidget)
        self.label_chats.setGeometry(QtCore.QRect(10, 40, 67, 25))
        self.label_chats.setObjectName("label_chats")
        self.label_chat_heading = QtWidgets.QLabel(self.centralwidget)
        self.label_chat_heading.setGeometry(QtCore.QRect(310, 40, 480, 25))
        self.label_chat_heading.setObjectName("label_chat_heading")
        self.list_widget_chats = QtWidgets.QListWidget(self.centralwidget, clicked=lambda: self.clicked_chat_id())
        self.list_widget_chats.setGeometry(QtCore.QRect(10, 70, 290, 220))
        self.list_widget_chats.setObjectName("list_widget_chats")
        self.label_groups = QtWidgets.QLabel(self.centralwidget)
        self.label_groups.setGeometry(QtCore.QRect(10, 300, 67, 25))
        self.label_groups.setObjectName("label_groups")
        self.list_widget_messages = QtWidgets.QListWidget(self.centralwidget)
        self.list_widget_messages.setGeometry(QtCore.QRect(310, 70, 480, 440))
        self.list_widget_messages.setObjectName("list_widget_messages")
        self.line_edit_message = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_message.setGeometry(QtCore.QRect(310, 525, 380, 25))
        self.line_edit_message.setObjectName("line_edit_message")
        self.push_button_send = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clicked_send())
        self.push_button_send.setGeometry(QtCore.QRect(700, 525, 90, 25))
        self.push_button_send.setObjectName("push_button_send")
        self.list_widget_groups = QtWidgets.QListWidget(self.centralwidget, clicked=lambda: self.clicked_group_id())
        self.list_widget_groups.setGeometry(QtCore.QRect(10, 330, 290, 220))
        self.list_widget_groups.setObjectName("list_widget_groups")
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

        self.timer = QtCore.QTimer(self.MainWindow)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.refresh)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python ChatApp"))
        self.push_button_logout.setText(_translate("MainWindow", "Logout"))
        self.push_button_delete.setText(_translate("MainWindow", "Delete Account"))
        self.push_button_chat.setText(_translate("MainWindow", "Start a new chat"))
        self.push_button_group.setText(_translate("MainWindow", "Create a new group"))
        self.label_chats.setText(_translate("MainWindow", "Chats"))
        self.label_chat_heading.setText(_translate("MainWindow", ""))
        self.label_groups.setText(_translate("MainWindow", "Groups"))
        self.push_button_send.setText(_translate("MainWindow", "Send"))

    ####################################################################################################################

    """ USER GENERATED CODE STARTS HERE """

    ####################################################################################################################

    # needed for constant refreshment
    def start_timer(self):
        self.timer.start()

    # refreshes the users attributes and updates the list widgets
    def refresh(self):
        user.update_user()
        self.list_widget_chats.clear()
        self.list_widget_chats.addItems(user.Chat_Partners)
        self.list_widget_groups.clear()
        self.list_widget_groups.addItems(user.Groups)

        if self.current_chat_id is not None:
            self.list_widget_messages.clear()
            self.list_widget_messages.addItems(user.print_messages(self.current_chat_id))

        elif self.current_group_id is not None:
            self.list_widget_messages.clear()
            self.list_widget_messages.addItems(user.print_messages(self.current_group_id))

    ####################################################################################################################

    # logout the user | push_button_logout
    def clicked_logout(self):
        user.logout()
        self.MainWindow.close()

    # delete the user | push_button_delete
    def clicked_delete(self):
        user.delete_user(user.User_ID, user.Password)
        self.MainWindow.close()

    # open chat creation dialog | push_button_chat
    def clicked_chat(self):
        self.open_chat_dialog()

    # open group creation dialog | push_button_group
    def clicked_group(self):
        self.open_group_dialog()

    # try to send a message | push_button_send
    def clicked_send(self):
        content = self.line_edit_message.text()
        if self.current_chat_id is not None and content.strip() != "":
            user.send_message(self.current_chat_id, content)
        elif self.current_group_id is not None and content.strip() != "":
            user.send_message(self.current_group_id, content)
        self.line_edit_message.clear()
        self.refresh()

    ####################################################################################################################

    # open a chat | list_widget_chats
    def clicked_chat_id(self):
        self.current_group_id = None
        self.chat_name = self.list_widget_chats.currentItem().text()
        self.current_chat_id = user.Chats[user.Chat_Partners.index(self.chat_name)]
        self.label_chat_heading.setText(self.chat_name)
        self.refresh()

    # open a group | list_widget_groups
    def clicked_group_id(self):
        self.current_chat_id, self.chat_name = None, None
        self.current_group_id = self.list_widget_groups.currentItem().text()
        self.label_chat_heading.setText(self.current_group_id)
        self.refresh()

    ####################################################################################################################

    def open_chat_dialog(self):
        dlg = ChatDlg(self.MainWindow)
        dlg.exec()

    def open_group_dialog(self):
        dlg = GroupDlg(self.MainWindow)
        dlg.exec()

