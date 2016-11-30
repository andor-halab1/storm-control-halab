#!/usr/bin/python
#
## @file
#
# RS232 interface to a Applied Scientific Instrumentation MFC2000 Z stage with Crisp.
#

import imp
imp.load_source("setPath", "C:\\STORM_controller\\storm-control-halab\\sc_library\\setPath.py")

import sys
import time

import sc_library.hdebug as hdebug

import sc_hardware.serial.RS232 as RS232


## MFC2000
#
# Applied Scientific Instrumentation MFC2000 RS232 interface class.
#
class MFC2000(RS232.RS232):

    ## __init__
    #
    # Connect to the MFC2000 stage at the specified port.
    #
    # @param port The RS-232 port name (e.g. "COM1").
    # @param wait_time (Optional) How long (in seconds) for a response from the stage.
    #
    def __init__(self, port, wait_time = 0.02):

        self.live = True
        self.unit_to_um = 0.1
        self.um_to_unit = 1.0/self.unit_to_um
        
        # RS232 stuff
        RS232.RS232.__init__(self, port, None, 9600, "\r", wait_time)
        try:
            test = self.commWithResp("Ver")
            if not test:
                self.live = False
        except:
            self.live = False
        if not self.live:
            print "ASI Z Stage is not connected? Z Stage is not on?"

        # self.state is dynamic, and it can be set by user
        self.state = self.read_State()
        if self.state != 'I':
            self.idle()
            if self.state != 'I':
                print "ASI Z stage cannot access the correct initial state."
            else:
                print "ASI Z stage is now put into the idle state."
        else:
            print "ASI Z stage is already in the idle state."

        '''
        # self.err is dynamic, but it cannot be set by user
        self.err = self.read_Err()
        # self.os is static, but it can be set by user
        self.os = self.read_Offset()
        # self.gn is static, but it can be set by user
        self.gn = self.read_Gain()
        # self.lr is static, but it can be set by user
        self.lr = self.read_LockRange()
        
        # self.z is dynamic, but it cannot be directly set by user. Any change in self.z
        # should be conducted through changing self.os.
        self.z = self.position()
        '''
        
        self.verbose()
    
    # built-in function in MFC2000 controller
    #
    def verbose(self):
        self.commWithResp("VB X=16")
    
    '''
    # built-in function in MFC2000 controller
    #
    def curve(self):
        self.commWithResp("LK F=97")
    '''
    
    # built-in function in MFC2000 controller
    #
    def read_State(self):
        if self.live:
            try:
                self.state = str(self.commWithResp("LK X?"))[3]
            except:
                hdebug.logText("  Warning: Bad state from ASI Z stage.")
            return self.state
        else:
            return 'I'
        
    # built-in function in MFC2000 controller
    #
    def read_Err(self):
        if self.live:
            try:
                self.err = float(self.commWithResp("LK Y?").split(" ")[1])
            except:
                hdebug.logText("  Warning: Bad error from ASI Z stage.")
            return self.err
        else:
            return 0.0

    # built-in function in MFC2000 controller
    #
    def read_Offset(self):
        if self.live:
            try:
                self.os = float(self.commWithResp("LK Z?").split(" ")[1])
            except:
                hdebug.logText("  Warning: Bad offset from ASI Z stage.")
            return self.os
        else:
            return 0.0

    # built-in function in MFC2000 controller
    #
    def read_Gain(self):
        if self.live:
            try:
                self.lr = float(str(self.commWithResp("LR X?").split(" ")[1])[2:])
            except:
                hdebug.logText("  Warning: Bad gain from ASI Z stage.")
            return self.lr
        else:
            return -5000.00
    
    # built-in function in MFC2000 controller
    #
    def read_LockRange(self):
        if self.live:
            try:
                self.lr = float(str(self.commWithResp("LR Z?").split(" ")[1])[2:])
            except:
                hdebug.logText("  Warning: Bad lock range from ASI Z stage.")
            return self.lr
        else:
            return 0.032
            
    # built-in function in MFC2000 controller
    #
    # This function will set the state to 'G'
    #
    def IoG_Cal(self):
        self.commWithResp("LK F=72")

    # built-in function in MFC2000 controller
    #
    # This fucntion will set the state to dither states.
    #
    def dither(self):
        self.commWithResp("LK F=102")
        
    # built-in function in MFC2000 controller
    #
    # This fucntion will set the state to 'R'.
    # It automatically sets a new gain and sets the current offset as focus target.
    #
    def gain_Cal(self):
        self.commWithResp("LK F=67")

    # built-in function in MFC2000 controller
    #
    # This function will either sets zero or a specific offset as focus target.
    #
    def set_Offset(self, ost):
        if ost is None:
            self.commWithResp("LK F=111")
        else:
            self.commWithResp("LK Z=" + str(ost))
        #self.os = self.read_Offset()

    # built-in function in MFC2000 controller
    #
    # This fucntion will set lock range.
    #
    def set_LockRange(self, lrt=0.030):
        self.commWithResp("LR Z=" + str(lrt))
        #self.lr = self.read_LockRange()

    ## idle
    #
    # This state can be accessed from any other states, so it serves as a point of origin.
    #
    # built-in function in MFC2000 controller
    #
    def idle(self):
        self.commWithResp("LK F=79")
        #self.state = self.read_State()

    ## ready
    #
    # built-in function in MFC2000 controller
    #
    def getReady(self):
        self.commWithResp("LK F=85")
        #self.state = self.read_State()
    
    ## focus
    #
    # built-in function in MFC2000 controller
    #
    def getFocus(self):
        self.commWithResp("LK F=83")
        #self.state = self.read_State()

    ## relax
    #
    # built-in function in MFC2000 controller
    #
    def getRelax(self):
        self.getReady()

    ## getStatus
    #
    # @return True/False if we are actually connected to the stage.
    #
    def getStatus(self):
        return self.live

    ## position
    #
    # @return [stage z (um)]
    #
    def position(self):
        if self.live:
            try:
                self.z = float(self.commWithResp("Where Z").split(" ")[1])
            except:
                hdebug.logText("  Warning: Bad position from ASI Z stage.")
            return self.z * self.unit_to_um
        else:
            return 0.0

    ## goAbsolute
    #
    # @param x Stage x position in um.
    # @param y Stage y position in um.
    #
    def goAbsolute(self, z):
        pass
        '''
        if self.live:
            Z = z * self.um_to_unit
            self.commWithResp("Move Z=" + str(Z))
        self.z = self.position()
        '''

    ## goRelative
    #
    # @param x Amount to move the stage in x in um.
    # @param y Amount to move the stage in y in um.
    #
    def goRelative(self, z):
        pass
        '''
        if self.live:
            Z = z * self.um_to_unit
            self.commWithResp("Movrel Z=" + str(Z))
        self.z = self.position()
        '''

    ## jog
    #
    def jog(self, x_speed, y_speed):
        pass

    ## joystickOnOff
    #
    def joystickOnOff(self, on):
        pass

    ## setVelocity
    #
    # @param x_vel Maximum velocity to move in x.
    # @param y_vel Maximum velocity to move in y.
    #
    def setVelocity(self, z_vel):
        if self.live:
            vz = z_vel
            self.commWithResp("Speed Z=" + str(vz))

    ## zero
    #
    # Set the current stage position as the stage zero.
    #
    def zero(self):
        pass
        '''
        if self.live:
            self.commWithResp("Here Z=0")
        self.z = self.position()
        '''



#
# Testing
# 

if __name__ == "__main__":
    stage = MFC2000("COM5")
    state = stage.read_State()
    print state
    err = stage.read_Err()
    print err
    os = stage.read_Offset()
    print os
    gn = stage.read_Gain()
    print gn

    stage.gain_Cal()
    time.sleep(2)
    #stage.set_Offset(None)
    
    print "After"
    state = stage.read_State()
    print state
    err = stage.read_Err()
    print err
    os = stage.read_Offset()
    print os
    gn = stage.read_Gain()
    print gn

    #stage.getReady()
    #stage.getFocus()
    
    '''
    stage.IoG_Cal()
    time.sleep(2)

    stage.dither()
    time.sleep(15)
    

    
    print stage.state
    time.sleep(1)
    stage.getReady()
    stage.getFocus()
    print "focused"
    time.sleep(5)
    print "relexed"
    stage.getRelax()
    '''
    
    '''
    #string_pos = info.find('SNR:')
    #print info[string_pos+5:string_pos+8]
    time.sleep(1)
    err = stage.read_Err()
    print err
    time.sleep(1)
    err = stage.read_Err()
    print err
    '''
    '''
    stage.setVelocity(0.01)
    stage.goRelative(10)
    time.sleep(1)
    print stage.position()
    stage.zero()
    time.sleep(1)
    print stage.position()
    '''
    
    #stage.getFocus()

    #print stage.commWithResp("W X Y")
    #stage.goAbsolute(100.0, 100.0)
    #time.sleep(5)
    #print stage.position()
    #stage.goAbsolute(0.0, 0.0)
    #time.sleep(5)
    #print stage.position()

    #print "SN:", stage.serialNumber()
    #stage.zero()
    #print "Position:", stage.position()
    #stage.goAbsolute(100.0, 100.0)
    #print "Position:", stage.position()
    #stage.goRelative(100.0, 100.0)
    #print "Position:", stage.position()
    stage.shutDown()

#    for info in stage.info():
#        print info
#    stage.zero()
#    print stage.position()
#    stage.goAbsolute(100000,100000)
#    print stage.position()
#    stage.goAbsolute(0,0)
#    print stage.position()
#    stage.goRelative(-100000,-100000)
#    print stage.position()
#    stage.goAbsolute(0,0)
#    print stage.position()


#
# The MIT License
#
# Copyright (c) 2014 Zhuang Lab, Harvard University
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
