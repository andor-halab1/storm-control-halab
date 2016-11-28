# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camera-display.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(645, 545)
        Frame.setFrameShape(QtGui.QFrame.NoFrame)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Frame)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.displayWidget = QtGui.QWidget(Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displayWidget.sizePolicy().hasHeightForWidth())
        self.displayWidget.setSizePolicy(sizePolicy)
        self.displayWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.displayWidget.setObjectName(_fromUtf8("displayWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.displayWidget)
        self.horizontalLayout_2.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cameraScrollArea = QCameraScrollArea(self.displayWidget)
        self.cameraScrollArea.setMinimumSize(QtCore.QSize(514, 514))
        self.cameraScrollArea.setAutoFillBackground(False)
        self.cameraScrollArea.setWidgetResizable(True)
        self.cameraScrollArea.setObjectName(_fromUtf8("cameraScrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 569, 512))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.cameraScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.cameraScrollArea)
        self.scaleWidget = QtGui.QWidget(self.displayWidget)
        self.scaleWidget.setMinimumSize(QtCore.QSize(70, 0))
        self.scaleWidget.setMaximumSize(QtCore.QSize(70, 16777215))
        self.scaleWidget.setObjectName(_fromUtf8("scaleWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scaleWidget)
        self.verticalLayout.setContentsMargins(0, 6, 0, 6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scaleMax = QtGui.QLabel(self.scaleWidget)
        self.scaleMax.setMaximumSize(QtCore.QSize(16777215, 14))
        self.scaleMax.setAlignment(QtCore.Qt.AlignCenter)
        self.scaleMax.setObjectName(_fromUtf8("scaleMax"))
        self.verticalLayout.addWidget(self.scaleMax)
        self.slideWidget = QtGui.QWidget(self.scaleWidget)
        self.slideWidget.setObjectName(_fromUtf8("slideWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.slideWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.rangeSliderWidget = QtGui.QWidget(self.slideWidget)
        self.rangeSliderWidget.setMinimumSize(QtCore.QSize(10, 0))
        self.rangeSliderWidget.setObjectName(_fromUtf8("rangeSliderWidget"))
        self.horizontalLayout.addWidget(self.rangeSliderWidget)
        self.colorFrame = QtGui.QFrame(self.slideWidget)
        self.colorFrame.setMinimumSize(QtCore.QSize(10, 0))
        self.colorFrame.setMaximumSize(QtCore.QSize(20, 10000))
        self.colorFrame.setFrameShape(QtGui.QFrame.Panel)
        self.colorFrame.setFrameShadow(QtGui.QFrame.Sunken)
        self.colorFrame.setObjectName(_fromUtf8("colorFrame"))
        self.horizontalLayout.addWidget(self.colorFrame)
        self.verticalLayout.addWidget(self.slideWidget)
        self.scaleMin = QtGui.QLabel(self.scaleWidget)
        self.scaleMin.setMaximumSize(QtCore.QSize(16777215, 14))
        self.scaleMin.setAlignment(QtCore.Qt.AlignCenter)
        self.scaleMin.setObjectName(_fromUtf8("scaleMin"))
        self.verticalLayout.addWidget(self.scaleMin)
        self.horizontalLayout_2.addWidget(self.scaleWidget)
        self.verticalLayout_2.addWidget(self.displayWidget)
        self.infoWidget = QtGui.QWidget(Frame)
        self.infoWidget.setObjectName(_fromUtf8("infoWidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.infoWidget)
        self.horizontalLayout_3.setContentsMargins(9, 2, 9, 2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.recordButton = QtGui.QPushButton(self.infoWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recordButton.sizePolicy().hasHeightForWidth())
        self.recordButton.setSizePolicy(sizePolicy)
        self.recordButton.setMinimumSize(QtCore.QSize(60, 0))
        self.recordButton.setMaximumSize(QtCore.QSize(75, 23))
        self.recordButton.setObjectName(_fromUtf8("recordButton"))
        self.horizontalLayout_3.addWidget(self.recordButton)
        self.cameraShutterButton = QtGui.QPushButton(self.infoWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cameraShutterButton.sizePolicy().hasHeightForWidth())
        self.cameraShutterButton.setSizePolicy(sizePolicy)
        self.cameraShutterButton.setMinimumSize(QtCore.QSize(90, 0))
        self.cameraShutterButton.setMaximumSize(QtCore.QSize(75, 23))
        self.cameraShutterButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cameraShutterButton.setObjectName(_fromUtf8("cameraShutterButton"))
        self.horizontalLayout_3.addWidget(self.cameraShutterButton)
        self.feedComboBox = QtGui.QComboBox(self.infoWidget)
        self.feedComboBox.setObjectName(_fromUtf8("feedComboBox"))
        self.horizontalLayout_3.addWidget(self.feedComboBox)
        spacerItem = QtGui.QSpacerItem(185, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.intensityPosLabel = QtGui.QLabel(self.infoWidget)
        self.intensityPosLabel.setMinimumSize(QtCore.QSize(61, 0))
        self.intensityPosLabel.setMaximumSize(QtCore.QSize(61, 16777215))
        self.intensityPosLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.intensityPosLabel.setObjectName(_fromUtf8("intensityPosLabel"))
        self.horizontalLayout_3.addWidget(self.intensityPosLabel)
        self.intensityIntLabel = QtGui.QLabel(self.infoWidget)
        self.intensityIntLabel.setMinimumSize(QtCore.QSize(41, 0))
        self.intensityIntLabel.setMaximumSize(QtCore.QSize(41, 16777215))
        self.intensityIntLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.intensityIntLabel.setObjectName(_fromUtf8("intensityIntLabel"))
        self.horizontalLayout_3.addWidget(self.intensityIntLabel)
        self.syncLabel = QtGui.QLabel(self.infoWidget)
        self.syncLabel.setMinimumSize(QtCore.QSize(41, 0))
        self.syncLabel.setMaximumSize(QtCore.QSize(41, 16777215))
        self.syncLabel.setObjectName(_fromUtf8("syncLabel"))
        self.horizontalLayout_3.addWidget(self.syncLabel)
        self.syncSpinBox = QtGui.QSpinBox(self.infoWidget)
        self.syncSpinBox.setMinimumSize(QtCore.QSize(46, 0))
        self.syncSpinBox.setMaximumSize(QtCore.QSize(46, 16777215))
        self.syncSpinBox.setObjectName(_fromUtf8("syncSpinBox"))
        self.horizontalLayout_3.addWidget(self.syncSpinBox)
        self.autoScaleButton = QtGui.QPushButton(self.infoWidget)
        self.autoScaleButton.setMinimumSize(QtCore.QSize(75, 0))
        self.autoScaleButton.setMaximumSize(QtCore.QSize(75, 16777215))
        self.autoScaleButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.autoScaleButton.setObjectName(_fromUtf8("autoScaleButton"))
        self.horizontalLayout_3.addWidget(self.autoScaleButton)
        self.colorComboBox = QtGui.QComboBox(self.infoWidget)
        self.colorComboBox.setMinimumSize(QtCore.QSize(74, 0))
        self.colorComboBox.setMaximumSize(QtCore.QSize(74, 16777215))
        self.colorComboBox.setObjectName(_fromUtf8("colorComboBox"))
        self.horizontalLayout_3.addWidget(self.colorComboBox)
        self.verticalLayout_2.addWidget(self.infoWidget)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.scaleMax.setText(_translate("Frame", "TextLabel", None))
        self.scaleMin.setText(_translate("Frame", "TextLabel", None))
        self.recordButton.setText(_translate("Frame", "Record", None))
        self.cameraShutterButton.setText(_translate("Frame", "Open Shutter", None))
        self.intensityPosLabel.setText(_translate("Frame", "(0,0)", None))
        self.intensityIntLabel.setText(_translate("Frame", "0", None))
        self.syncLabel.setText(_translate("Frame", "Display:", None))
        self.autoScaleButton.setText(_translate("Frame", "Autoscale", None))

from qtWidgets.qtCameraScrollArea import QCameraScrollArea
