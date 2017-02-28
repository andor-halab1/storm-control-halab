# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nstorm-misc.ui'
#
# Created: Tue Apr 14 08:52:49 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(428, 232)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(428, 232))
        Dialog.setMaximumSize(QtCore.QSize(428, 232))
        
        self.lightGroupBox = QtGui.QGroupBox(Dialog)
        self.lightGroupBox.setGeometry(QtCore.QRect(9, 9, 411, 61))
        self.lightGroupBox.setObjectName(_fromUtf8("lightGroupBox"))
        
        self.light1Button = QtGui.QPushButton(self.lightGroupBox)
        self.light1Button.setCheckable(True)
        self.light1Button.setAutoExclusive(True)
        self.light1Button.setGeometry(QtCore.QRect(5, 20, 40, 24))
        self.light1Button.setObjectName(_fromUtf8("light1Button"))
        self.light1SpinBox = QtGui.QDoubleSpinBox(self.lightGroupBox)
        self.light1SpinBox.setGeometry(QtCore.QRect(45, 20, 40, 24))
        self.light1SpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.light1SpinBox.setMinimum(0)
        self.light1SpinBox.setMaximum(100)
        self.light1SpinBox.setSingleStep(10)
        self.light1SpinBox.setDecimals(0)
        self.light1SpinBox.setObjectName(_fromUtf8("light1SpinBox"))
        
        self.light2Button = QtGui.QPushButton(self.lightGroupBox)
        self.light2Button.setCheckable(True)
        self.light2Button.setAutoExclusive(True)
        self.light2Button.setGeometry(QtCore.QRect(95, 20, 40, 24))
        self.light2Button.setObjectName(_fromUtf8("light2Button"))
        self.light2SpinBox = QtGui.QDoubleSpinBox(self.lightGroupBox)
        self.light2SpinBox.setGeometry(QtCore.QRect(135, 20, 40, 24))
        self.light2SpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.light2SpinBox.setMinimum(0)
        self.light2SpinBox.setMaximum(100)
        self.light2SpinBox.setSingleStep(10)
        self.light2SpinBox.setDecimals(0)
        self.light2SpinBox.setObjectName(_fromUtf8("light2SpinBox"))
        
        self.light3Button = QtGui.QPushButton(self.lightGroupBox)
        self.light3Button.setCheckable(True)
        self.light3Button.setAutoExclusive(True)
        self.light3Button.setGeometry(QtCore.QRect(185, 20, 40, 24))
        self.light3Button.setObjectName(_fromUtf8("light3Button"))
        self.light3SpinBox = QtGui.QDoubleSpinBox(self.lightGroupBox)
        self.light3SpinBox.setGeometry(QtCore.QRect(225, 20, 40, 24))
        self.light3SpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.light3SpinBox.setMinimum(0)
        self.light3SpinBox.setMaximum(100)
        self.light3SpinBox.setSingleStep(10)
        self.light3SpinBox.setDecimals(0)
        self.light3SpinBox.setObjectName(_fromUtf8("light3SpinBox"))
        
        self.light4Button = QtGui.QPushButton(self.lightGroupBox)
        self.light4Button.setCheckable(True)
        self.light4Button.setAutoExclusive(True)
        self.light4Button.setGeometry(QtCore.QRect(275, 20, 40, 24))
        self.light4Button.setObjectName(_fromUtf8("light4Button"))
        self.light4SpinBox = QtGui.QDoubleSpinBox(self.lightGroupBox)
        self.light4SpinBox.setGeometry(QtCore.QRect(315, 20, 40, 24))
        self.light4SpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.light4SpinBox.setMinimum(0)
        self.light4SpinBox.setMaximum(100)
        self.light4SpinBox.setSingleStep(10)
        self.light4SpinBox.setDecimals(0)
        self.light4SpinBox.setObjectName(_fromUtf8("light4SpinBox"))
        
        self.light5Button = QtGui.QPushButton(self.lightGroupBox)
        self.light5Button.setCheckable(True)
        self.light5Button.setAutoExclusive(True)
        self.light5Button.setGeometry(QtCore.QRect(365, 20, 40, 24))
        self.light5Button.setObjectName(_fromUtf8("light5Button"))
        
        self.filterWheelGroupBox = QtGui.QGroupBox(Dialog)
        self.filterWheelGroupBox.setGeometry(QtCore.QRect(9, 75, 411, 61))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterWheelGroupBox.sizePolicy().hasHeightForWidth())
        self.filterWheelGroupBox.setSizePolicy(sizePolicy)
        self.filterWheelGroupBox.setObjectName(_fromUtf8("filterWheelGroupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.filterWheelGroupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.filter1Button = QtGui.QPushButton(self.filterWheelGroupBox)
        self.filter1Button.setCheckable(True)
        self.filter1Button.setAutoExclusive(True)
        self.filter1Button.setObjectName(_fromUtf8("filter1Button"))
        self.horizontalLayout.addWidget(self.filter1Button)
        self.filter2Button = QtGui.QPushButton(self.filterWheelGroupBox)
        self.filter2Button.setCheckable(True)
        self.filter2Button.setAutoExclusive(True)
        self.filter2Button.setObjectName(_fromUtf8("filter2Button"))
        self.horizontalLayout.addWidget(self.filter2Button)
        self.filter3Button = QtGui.QPushButton(self.filterWheelGroupBox)
        self.filter3Button.setCheckable(True)
        self.filter3Button.setAutoExclusive(True)
        self.filter3Button.setObjectName(_fromUtf8("filter3Button"))
        self.horizontalLayout.addWidget(self.filter3Button)
        self.filter4Button = QtGui.QPushButton(self.filterWheelGroupBox)
        self.filter4Button.setCheckable(True)
        self.filter4Button.setAutoExclusive(True)
        self.filter4Button.setObjectName(_fromUtf8("filter4Button"))
        self.horizontalLayout.addWidget(self.filter4Button)
        self.filter5Button = QtGui.QPushButton(self.filterWheelGroupBox)
        self.filter5Button.setCheckable(True)
        self.filter5Button.setAutoExclusive(True)
        self.filter5Button.setObjectName(_fromUtf8("filter5Button"))
        self.horizontalLayout.addWidget(self.filter5Button)
        self.filter6Button = QtGui.QPushButton(self.filterWheelGroupBox)
        self.filter6Button.setCheckable(True)
        self.filter6Button.setAutoExclusive(True)
        self.filter6Button.setObjectName(_fromUtf8("filter6Button"))
        self.horizontalLayout.addWidget(self.filter6Button)

        self.efilterWheelGroupBox = QtGui.QGroupBox(Dialog)
        self.efilterWheelGroupBox.setGeometry(QtCore.QRect(9, 145, 411, 51))
        self.efilterWheelGroupBox.setObjectName(_fromUtf8("efilterWheelGroupBox"))
        
        self.efilter1Button = QtGui.QPushButton(self.efilterWheelGroupBox)
        self.efilter1Button.setCheckable(True)
        self.efilter1Button.setAutoExclusive(True)
        self.efilter1Button.setGeometry(QtCore.QRect(5, 20, 40, 24))
        self.efilter1Button.setObjectName(_fromUtf8("efilter1Button"))
        
        self.efilter2Button = QtGui.QPushButton(self.efilterWheelGroupBox)
        self.efilter2Button.setCheckable(True)
        self.efilter2Button.setAutoExclusive(True)
        self.efilter2Button.setGeometry(QtCore.QRect(95, 20, 40, 24))
        self.efilter2Button.setObjectName(_fromUtf8("efilter3Button"))
        
        self.efilter3Button = QtGui.QPushButton(self.efilterWheelGroupBox)
        self.efilter3Button.setCheckable(True)
        self.efilter3Button.setAutoExclusive(True)
        self.efilter3Button.setGeometry(QtCore.QRect(185, 20, 40, 24))
        self.efilter3Button.setObjectName(_fromUtf8("efilter3Button"))

        self.efilter4Button = QtGui.QPushButton(self.efilterWheelGroupBox)
        self.efilter4Button.setCheckable(True)
        self.efilter4Button.setAutoExclusive(True)
        self.efilter4Button.setGeometry(QtCore.QRect(275, 20, 40, 24))
        self.efilter4Button.setObjectName(_fromUtf8("efilter4Button"))

        self.efilter5Button = QtGui.QPushButton(self.efilterWheelGroupBox)
        self.efilter5Button.setCheckable(True)
        self.efilter5Button.setAutoExclusive(True)
        self.efilter5Button.setGeometry(QtCore.QRect(365, 20, 40, 24))
        self.efilter5Button.setObjectName(_fromUtf8("efilter5Button"))
        
        self.okButton = QtGui.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(340, 200, 77, 25))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okButton.sizePolicy().hasHeightForWidth())
        self.okButton.setSizePolicy(sizePolicy)
        self.okButton.setObjectName(_fromUtf8("okButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "HAL-4000 Miscellaneous Controls", None))
        
        self.lightGroupBox.setTitle(_translate("Dialog", "Light Control", None))
        self.light1Button.setText(_translate("Dialog", "Violet", None))
        self.light2Button.setText(_translate("Dialog", "Green", None))
        self.light3Button.setText(_translate("Dialog", "Red", None))
        self.light4Button.setText(_translate("Dialog", "Teal", None))
        self.light5Button.setText(_translate("Dialog", "Off", None))
        
        self.filterWheelGroupBox.setTitle(_translate("Dialog", "Dichroic Filter Wheel", None))
        self.filter1Button.setText(_translate("Dialog", "1", None))
        self.filter2Button.setText(_translate("Dialog", "2", None))
        self.filter3Button.setText(_translate("Dialog", "3", None))
        self.filter4Button.setText(_translate("Dialog", "4", None))
        self.filter5Button.setText(_translate("Dialog", "5", None))
        self.filter6Button.setText(_translate("Dialog", "6", None))

        self.efilterWheelGroupBox.setTitle(_translate("Dialog", "Emission Filter Wheel", None))
        self.efilter1Button.setText(_translate("Dialog", "DAPI", None))
        self.efilter2Button.setText(_translate("Dialog", "Cy3", None))
        self.efilter3Button.setText(_translate("Dialog", "Cy5", None))
        self.efilter4Button.setText(_translate("Dialog", "Empty", None))
        self.efilter5Button.setText(_translate("Dialog", "Close", None))
        
        self.okButton.setText(_translate("Dialog", "Ok", None))

