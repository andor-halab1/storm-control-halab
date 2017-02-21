#!/usr/bin/python
#
## @file
#
# Control of various Nikon TiE accessories (using Micro-Manager).
#
# Hazen 4/15
#

import MMCorePy

## TiEMisc
#
# Encapsulates control of various TiE accessories.
#
class TiEMisc(object):

    ## __init__
    #
    def __init__(self):
        self.mmc = MMCorePy.CMMCore()
        self.mmc.loadDevice('TIScope', 'NikonTI', 'TIScope')
        self.mmc.loadDevice('TIFilterBlock1', 'NikonTI', 'TIFilterBlock1')
        self.mmc.initializeAllDevices()

    ## getFilterWheel
    #
    # @return Current position of the filter wheel.
    #
    def getFilterWheel(self):
        return int(self.mmc.getProperty('TIFilterBlock1', 'State'))

    ## setFilterWheel
    #
    # @param state The filter wheel position.
    #
    def setFilterWheel(self, state):
        self.mmc.setProperty('TIFilterBlock1', 'State', str(state))
