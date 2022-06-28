# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setLineWidth(0)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_mouse = QtWidgets.QFrame(self.frame_main)
        self.frame_mouse.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_mouse.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_mouse.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mouse.setLineWidth(0)
        self.frame_mouse.setObjectName("frame_mouse")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_mouse)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_logo = QtWidgets.QFrame(self.frame_mouse)
        self.frame_logo.setMinimumSize(QtCore.QSize(50, 0))
        self.frame_logo.setToolTipDuration(-6)
        self.frame_logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo.setLineWidth(0)
        self.frame_logo.setObjectName("frame_logo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_logo)
        self.horizontalLayout_2.setContentsMargins(6, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_logo = QtWidgets.QLabel(self.frame_logo)
        self.label_logo.setStyleSheet("border-image: url(:/logo/logo.png);")
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.horizontalLayout_2.addWidget(self.label_logo)
        self.horizontalLayout.addWidget(self.frame_logo)
        spacerItem = QtWidgets.QSpacerItem(627, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame_buttons = QtWidgets.QFrame(self.frame_mouse)
        self.frame_buttons.setMinimumSize(QtCore.QSize(120, 40))
        self.frame_buttons.setMaximumSize(QtCore.QSize(120, 40))
        self.frame_buttons.setStyleSheet("")
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons.setLineWidth(0)
        self.frame_buttons.setObjectName("frame_buttons")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_buttons)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButtonMinimize = QtWidgets.QPushButton(self.frame_buttons)
        self.pushButtonMinimize.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButtonMinimize.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButtonMinimize.setStyleSheet("QPushButton {\n"
"    border-image: url(:/icons/minimize.png);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 5px solid;\n"
"    border-image: url(:/icons/minimize.png);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.pushButtonMinimize.setText("")
        self.pushButtonMinimize.setObjectName("pushButtonMinimize")
        self.horizontalLayout_8.addWidget(self.pushButtonMinimize)
        self.pushButtonMaximize = QtWidgets.QPushButton(self.frame_buttons)
        self.pushButtonMaximize.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButtonMaximize.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButtonMaximize.setStyleSheet("QPushButton {\n"
"    border-image: url(:/icons/maximize.png);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 5px solid;\n"
"    border-image: url(:/icons/maximize.png);\n"
"}\n"
"\n"
"\n"
"")
        self.pushButtonMaximize.setText("")
        self.pushButtonMaximize.setObjectName("pushButtonMaximize")
        self.horizontalLayout_8.addWidget(self.pushButtonMaximize)
        self.pushButtonClose = QtWidgets.QPushButton(self.frame_buttons)
        self.pushButtonClose.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButtonClose.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButtonClose.setStyleSheet("QPushButton {\n"
"    border-image: url(:/icons/close.png);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 5px solid;\n"
"    border-image: url(:/icons/close.png);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.pushButtonClose.setText("")
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.horizontalLayout_8.addWidget(self.pushButtonClose)
        self.horizontalLayout.addWidget(self.frame_buttons)
        self.verticalLayout_2.addWidget(self.frame_mouse)
        self.frame_main_content = QtWidgets.QFrame(self.frame_main)
        self.frame_main_content.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_main_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main_content.setLineWidth(0)
        self.frame_main_content.setObjectName("frame_main_content")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_main_content)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_content = QtWidgets.QFrame(self.frame_main_content)
        self.frame_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.verticalLayout_3.addWidget(self.frame_content)
        self.frame_gap = QtWidgets.QFrame(self.frame_main_content)
        self.frame_gap.setMinimumSize(QtCore.QSize(0, 1))
        self.frame_gap.setMaximumSize(QtCore.QSize(16777215, 1))
        self.frame_gap.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_gap.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_gap.setLineWidth(0)
        self.frame_gap.setObjectName("frame_gap")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_gap)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_gap = QtWidgets.QLabel(self.frame_gap)
        self.label_gap.setStyleSheet("background-color: rgb(79, 79, 79);")
        self.label_gap.setLineWidth(0)
        self.label_gap.setText("")
        self.label_gap.setObjectName("label_gap")
        self.horizontalLayout_3.addWidget(self.label_gap)
        self.verticalLayout_3.addWidget(self.frame_gap)
        self.verticalLayout_2.addWidget(self.frame_main_content)
        self.verticalLayout.addWidget(self.frame_main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

import images_rc
