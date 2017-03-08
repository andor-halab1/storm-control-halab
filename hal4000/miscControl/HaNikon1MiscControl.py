#!/usr/bin/python
#
## @file
#
# Miscellaneous controls, such as the filter wheel.
#
# Hazen 04/15
#

from PyQt4 import QtCore, QtGui

import miscControl

# Debugging
import sc_library.hdebug as hdebug

# UIs.
import qtdesigner.HaNikon1_misc_ui as miscControlsUi

# Nikon TiU hardware control.
import sc_hardware.nikon.tiEMisc as tiEMisc
import sc_hardware.lumencor.spectra as spectra


#
# Misc Control Dialog Box
#
class AMiscControl(miscControl.MiscControl):
    @hdebug.debug
    def __init__(self, hardware, parameters, parent = None):
        miscControl.MiscControl.__init__(self, parameters, parent)

        self.tie_misc = tiEMisc.TiEMisc()
        self.spectra = spectra.Spectra("COM6")

        # UI setup
        self.ui = miscControlsUi.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle(parameters.get("setup_name") + " Misc Control")

        # connect signals
        if self.have_parent:
            self.ui.okButton.setText("Close")
            self.ui.okButton.clicked.connect(self.handleOk)
        else:
            self.ui.okButton.setText("Quit")
            self.ui.okButton.clicked.connect(self.handleQuit)

        # setup dichroic filter wheel
        self.filters = [self.ui.filter1Button,
                        self.ui.filter2Button,
                        self.ui.filter3Button,
                        self.ui.filter4Button,
                        self.ui.filter5Button,
                        self.ui.filter6Button]
        for filter in self.filters:
            filter.clicked.connect(self.handleFilter)
        self.filters[self.tie_misc.getFilterWheel()].click()

        # setup emission filter wheel
        self.efilters = [self.ui.efilter1Button,
                        self.ui.efilter2Button,
                        self.ui.efilter3Button,
                        self.ui.efilter4Button,
                        self.ui.efilter5Button]
        for efilter in self.efilters:
            efilter.clicked.connect(self.handleEFilter)
        self.efilters[4].click()

        # setup light control
        self.lights = [self.ui.light1Button,
                        self.ui.light2Button,
                        self.ui.light3Button,
                        self.ui.light4Button,
                        self.ui.light5Button]
        for light in self.lights:
            light.clicked.connect(self.handleLight)
        self.lights[4].click()

        self.lightAmps = [self.ui.light1SpinBox,
                          self.ui.light2SpinBox,
                          self.ui.light3SpinBox,
                          self.ui.light4SpinBox]
        
        self.lightAmps[0].valueChanged.connect(self.handlelight1SpinBox)
        self.lightAmps[1].valueChanged.connect(self.handlelight2SpinBox)
        self.lightAmps[2].valueChanged.connect(self.handlelight3SpinBox)
        self.lightAmps[3].valueChanged.connect(self.handlelight4SpinBox)
        self.lightAmps[0].setValue(20)
        self.lightAmps[1].setValue(20)
        self.lightAmps[2].setValue(20)
        self.lightAmps[3].setValue(20)

        self.newParameters(self.parameters)

    ## cleanup
    #
    @hdebug.debug
    def cleanup(self):
        pass

    ## connectSignals
    #
    # @param signals An array of signals that we might be interested in connecting to.
    #
    @hdebug.debug
    def connectSignals(self, signals):
        pass

    @hdebug.debug
    def handleFilter(self, bool):
        for i, filter in enumerate(self.filters):
            if filter.isChecked():
                filter.setStyleSheet("QPushButton { color: red}")
                self.tie_misc.setFilterWheel(i)
                self.parameters.set("filter_position", i)
            else:
                filter.setStyleSheet("QPushButton { color: black}")

    @hdebug.debug
    def handleEFilter(self, bool):
        for i, efilter in enumerate(self.efilters):
            if efilter.isChecked():
                efilter.setStyleSheet("QPushButton { color: red}")
                self.parameters.set("efilter_position", i)
            else:
                efilter.setStyleSheet("QPushButton { color: black}")

    @hdebug.debug
    def handleLight(self, bool):
        for i, light in enumerate(self.lights):
            if light.isChecked():
                light.setStyleSheet("QPushButton { color: red}")
                self.spectra.setLight(i)
                self.parameters.set("light", i)
            else:
                light.setStyleSheet("QPushButton { color: black}")

    @hdebug.debug
    def handlelight1SpinBox(self, amp):
        self.spectra.setAmp(0, amp)
        if self.parameters.get("misc.light") == 0:
            self.parameters.set("misc.light-amp", amp)
        else:
            self.parameters.set("light-amp", amp)

    @hdebug.debug
    def handlelight2SpinBox(self, amp):
        self.spectra.setAmp(1, amp)
        if self.parameters.get("misc.light") == 1:
            self.parameters.set("misc.light-amp", amp)
        else:
            self.parameters.set("light-amp", amp)

    @hdebug.debug
    def handlelight3SpinBox(self, amp):
        self.spectra.setAmp(2, amp)
        if self.parameters.get("misc.light") == 2:
            self.parameters.set("misc.light-amp", amp)
        else:
            self.parameters.set("light-amp", amp)
    
    @hdebug.debug
    def handlelight4SpinBox(self, amp):
        self.spectra.setAmp(3, amp)
        if self.parameters.get("misc.light") == 3:
            self.parameters.set("misc.light-amp", amp)
        else:
            self.parameters.set("light-amp", amp)

    @hdebug.debug
    def newParameters(self, parameters):
        self.parameters = parameters
        
        names = parameters.get("misc.filter_names")
        if (len(names) == 6):
            for i in range(6):
                self.filters[i].setText(names[i])
        self.filters[self.parameters.get("misc.filter_position")].click()
        self.efilters[self.parameters.get("misc.efilter_position")].click()
        
        self.lights[self.parameters.get("misc.light")].click()
        if self.parameters.get("misc.light") != 4:
            self.lightAmps[self.parameters.get("misc.light")].setValue(self.parameters.get("misc.light-amp"))


#
# The MIT License
#
# Copyright (c) 2015 Zhuang Lab, Harvard University
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
