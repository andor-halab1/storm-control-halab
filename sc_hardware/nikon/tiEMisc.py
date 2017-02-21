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

    ## Initialization
    #
    # initialization and turn off all light
    #
    def initialization(self):
        print("spectra initialized")
        self.mmc.setSerialPortCommand("Spectra", "5702FF50", "\r");
        self.mmc.setSerialPortCommand("Spectra", "5703AB50", "\r");
        self.mmc.setSerialPortCommand("Spectra", "4F7F50", "\r");

    ## setLight
    #
    # @param state The color of light.
    #
    def setLight(self, color):
        if color == 0: # Violet
            print("Violet on")
            self.mmc.setSerialPortCommand("Spectra", "53180301F80050", "\r");
            self.mmc.setSerialPortCommand("Spectra", "4F7750", "\r");
        if color == 1: # Green
            self.mmc.setSerialPortCommand("Spectra", "53180304F80050", "\r");
            self.mmc.setSerialPortCommand("Spectra", "4F7D50", "\r");
        if color == 2: # Red
            self.mmc.setSerialPortCommand("Spectra", "53180308F80050", "\r");
            self.mmc.setSerialPortCommand("Spectra", "4F7E50", "\r");
        if color == 3: # Teal
            self.mmc.setSerialPortCommand("Spectra", "531A0302F80050", "\r");
            self.mmc.setSerialPortCommand("Spectra", "4F3F50", "\r");
            
    
