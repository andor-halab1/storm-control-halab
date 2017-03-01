#!/usr/bin/python
#
## @file
#
# Control of Nikon TiE focus-related accessories (using Micro-Manager).
#
# Hazen 4/15
#

# Add current storm-control directory to sys.path
import imp
imp.load_source("setPath", "C:/storm-control-halab/sc_library/setPath.py")
import time

import MMCorePy

## TiEFocus
#
# Encapsulates control of TiE focus-related accessories.
#
class TiEFocus(object):

    ## __init__
    #
    def __init__(self):
        self.mmc = MMCorePy.CMMCore()
        self.mmc.loadDevice('TIScope', 'NikonTI', 'TIScope')
        self.mmc.loadDevice('TIZDrive', 'NikonTI', 'TIZDrive')
        self.mmc.loadDevice('TIPFSOffset', 'NikonTI', 'TIPFSOffset')
        self.mmc.loadDevice('TIPFSStatus', 'NikonTI', 'TIPFSStatus')
        self.mmc.initializeAllDevices()

    ## setZPosition
    #
    # @param position The Z position.
    #
    def setZPosition(self, position):
        self.mmc.setPosition('TIZDrive',position)

    def goRelative(self, dz):
        position = self.position()+dz
        self.setZPosition(position)

    ## position
    #
    # @return [stage z (um)].
    #
    def position(self):
        position = [self.mmc.getPosition('TIZDrive')]
        return float(position[0])

    ## setZOffset
    #
    # @param Offset The Z offset.
    #
    def setZOffset(self, offset):
        self.mmc.setAutoFocusOffset(offset)

    def set_Offset(self, offset):
        self.setZOffset(offset)

    ## offset
    #
    # @return [stage offset].
    #
    def offset(self):
##        return [self.mmc.getProperty('TIPFSOffset','State')]
        return [self.mmc.getAutoFocusOffset()]

    def read_Offset(self):
        offset = self.offset()
        return float(offset[0])

    ## setZStatus
    #
    # @param status The Z status.
    #
    def setZStatus(self, status):
        self.mmc.setProperty('TIPFSStatus','State',status)

    def getFocus(self):
        self.setZStatus('On')

    def getRelax(self):
        self.setZStatus('Off')
    
    ## status
    #
    # @return [stage status].
    #
    def status(self):
        return [self.mmc.getProperty('TIPFSStatus','State')]

    def read_State(self):
        state = self.status()
        return str(state[0])

    def shutDown(self):
        self.setZStatus('Off')

if __name__ == "__main__":
    tie_focus = TiEFocus()
##    print tie_focus.position()
##    tie_focus.setZPosition(500)
##    time.sleep(2)
##    print tie_focus.position()
    print tie_focus.offset()
    tie_focus.setZOffset(500)
    time.sleep(2)
    print tie_focus.offset()
##    print tie_focus.status()
##    tie_focus.setZStatus('Off')
##    time.sleep(2)
##    print tie_focus.status()
    print tie_focus.position()
    print tie_focus.read_Offset()
    print tie_focus.read_State()



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
