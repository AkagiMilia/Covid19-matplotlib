# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(1600, 1080)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMouseTracking(False)
        Form.setTabletTracking(False)
        Form.setWhatsThis("")
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalGroupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalGroupBox.sizePolicy().hasHeightForWidth())
        self.horizontalGroupBox.setSizePolicy(sizePolicy)
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button1 = QtWidgets.QPushButton(self.horizontalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button1.sizePolicy().hasHeightForWidth())
        self.button1.setSizePolicy(sizePolicy)
        self.button1.setObjectName("button1")
        self.horizontalLayout_2.addWidget(self.button1)
        self.button3 = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.button3.setObjectName("button3")
        self.horizontalLayout_2.addWidget(self.button3)
        self.button4 = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.button4.setObjectName("button4")
        self.horizontalLayout_2.addWidget(self.button4)
        self.button2 = QtWidgets.QPushButton(self.horizontalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button2.sizePolicy().hasHeightForWidth())
        self.button2.setSizePolicy(sizePolicy)
        self.button2.setObjectName("button2")
        self.horizontalLayout_2.addWidget(self.button2)
        self.button5 = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.button5.setObjectName("button5")
        self.horizontalLayout_2.addWidget(self.button5)
        self.button6 = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.button6.setObjectName("button6")
        self.horizontalLayout_2.addWidget(self.button6)
        self.button7 = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.button7.setObjectName("button7")
        self.horizontalLayout_2.addWidget(self.button7)
        self.verticalLayout.addWidget(self.horizontalGroupBox)
        self.groupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Graphs of COVID-19 in America"))
        self.button1.setText(_translate("Form", "Cases"))
        self.button3.setText(_translate("Form", "Death&Cured"))
        self.button4.setText(_translate("Form", "StateCases"))
        self.button2.setText(_translate("Form", "StateDeath"))
        self.button5.setText(_translate("Form", "WorldConfirmed"))
        self.button6.setText(_translate("Form", "WorldDeath"))
        self.button7.setText(_translate("Form", "DeahRate"))
        self.groupBox.setTitle(_translate("Form", "Graphs"))
