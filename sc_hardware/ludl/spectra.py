#!/usr/bin/python
#
## @file
#
# Spectra stage communication.
#
# Hazen 02/14
#

import imp
imp.load_source("setPath", "C:\\storm-control-halab\\sc_library\\setPath.py")

import sc_hardware.serial.RS232 as RS232
import time


## Spectra
#
# Encapsulates control of a Spectra light source.
#
class Spectra(RS232.RS232):

    ## __init__
    #
    # @param port (Optional) The RS-232 port to use, defaults to "COM2".
    # @param timeout (Optional) The time out value for communication, defaults to None.
    # @param baudrate (Optional) The communication baud rate, defaults to 9600.
    # @param wait_time How long to wait between polling events before it is decided that there is no new data available on the port, defaults to 20ms.
    #
    def __init__(self, port, timeout = None, baudrate = 9600, wait_time = 0.02):
        
        # RS232 stuff
        RS232.RS232.__init__(self, port, timeout, baudrate, "\r", wait_time)

    ## _command
    #
    # @param command The command string to send.
    #
    # @return The response to the command.
    #
    def _command(self, command):
        response = self.commWithResp(command)
        if response:
            return response.split("\r")

    ## getStatus
    #
    # @return True/False if we are actually connected to the stage.
    #
    def getStatus(self):
        return True

    ## setLight
    #
    # @param state The color of light.
    #
    def setLight(self, color):
        if color == 0: # Violet
            print("Violet on")
            self._command("53180301F80050");
            self._command("4F7750");
        if color == 1: # Green
            self._command("53180304F80050");
            self._command("4F7D50");
        if color == 2: # Red
            self._command("53180308F80050");
            self._command("4F7E50");
        if color == 3: # Teal
            self._command("531A0302F80050");
            self._command("4F3F50");


#
# Testing
# 

if __name__ == "__main__":
    lights = Spectra("COM6")
    
    lights.setLight(0)

#
# The MIT License
#
# Copyright (c) 2011 Zhuang Lab, Harvard University
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
