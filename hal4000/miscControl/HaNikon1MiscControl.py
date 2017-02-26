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

        # setup filter wheel
        self.filters = [self.ui.filter1Button,
                        self.ui.filter2Button,
                        self.ui.filter3Button,
                        self.ui.filter4Button,
                        self.ui.filter5Button,
                        self.ui.filter6Button]
        for filter in self.filters:
            filter.clicked.connect(self.handleFilter)
        self.filters[self.tie_misc.getFilterWheel()].click()

        # setup light
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
        for lightAmp in self.lightAmps:
            lightAmp.valueChanged.connect(self.handlelightSpinBox)

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
    def handleLight(self, bool):
        for i, light in enumerate(self.lights):
            if light.isChecked():
                self.spectra.setLight(i)
                self.parameters.set("light", i)
            else:
                pass

    @hdebug.debug
    def handlelightSpinBox(self, bool):
        for i, lightAmp in enumerate(self.lightAmps):
            if lightAmp.valueChanged():
                amp = lightAmp.getValue()
                self.spectra.setAmp(i, amp)
                self.parameters.set("light-amp", amp)
            else:
                pass

    @hdebug.debug
    def newParameters(self, parameters):
        self.parameters = parameters
        
        names = parameters.get("misc.filter_names")
        if (len(names) == 6):
            for i in range(6):
                self.filters[i].setText(names[i])
        self.filters[self.parameters.get("misc.filter_position")].click()
        self.lights[self.parameters.get("misc.light")].click()
        self.spectra.setAmp(self.parameters.get("misc.light"), self.parameters.get("misc.light-amp"))

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
