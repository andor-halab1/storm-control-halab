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
        # self.mmc.loadDevice('Spectra', 'LumencorSpectra', 'Spectra')
        self.mmc.loadDevice('Spectra', 'SerialManager', 'COM6');
        self.mmc.setProperty('Spectra', 'StopBits', '1');
        self.mmc.setProperty('Spectra', 'Parity', 'None');
        self.mmc.setProperty('Spectra', 'Handshaking', 'Off');
        self.mmc.setProperty('Spectra', 'DelayBetweenCharsMs', '0.0000');
        self.mmc.setProperty('Spectra', 'BaudRate', '9600');
        self.mmc.setProperty('Spectra', 'AnswerTimeout', '500.0000');
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

    ## getLight
    #
    # @return Current light.
    #
    def getLight(self):
        return int(0)

    ## setLight
    #
    # @param state The color of light.
    #
    def setLight(self, color):
        pass
    
