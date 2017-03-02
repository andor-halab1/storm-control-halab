#!/usr/bin/python
#
## @file
#
# Lambda 10-B communication.
#
# Hazen 02/14
#

import imp
imp.load_source("setPath", "C:\\storm-control-halab\\sc_library\\setPath.py")

import serial
import time
import math

## Lambda 10-B
#
# Encapsulates control of a Spectra light source.
#
class Lambda10B(serial.Serial):

    ## __init__
    #
    # @param port (Optional) The serial port to use, defaults to "COM4".
    # @param timeout (Optional) The time out value for communication, defaults to None.
    # @param baudrate (Optional) The communication baud rate, defaults to 9600.
    # @param wait_time How long to wait between polling events before it is decided that there is no new data available on the port, defaults to 20ms.
    #
    def __init__(self, port, baudrate = 9600):
        
        # RS232 stuff
        serial.Serial.__init__(self, port, baudrate)
        
    ## _command
    #
    # @param command The command string to send.
    #
    # @return The response to the command.
    #
    def _command(self, command):
        self.write(command)
        return self.read(1)

    ## getStatus
    #
    # @return True/False if we are actually connected to the stage.
    #
    def getStatus(self):
        return True

    ## setFilter
    #
    # @param pos The position of filter wheel.
    #
    def setFilter(self, pos):
        cmd = str(16*1+pos)
        print cmd
        self._command(cmd)


#
# Testing
# 

if __name__ == "__main__":
    filters = Lambda10B("COM7", 9600)
    #filters.setFilter(5)
    temp = filters._command('\b00110001')
    print temp


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
