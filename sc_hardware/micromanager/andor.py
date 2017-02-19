#!/usr/bin/python
#
## @file
#
# Test how to use Micro-Manager.
#

import sys
sys.path.append("C:\Program Files\Micro-Manager-1.4")

import MMCorePy
import time


mmc1 = MMCorePy.CMMCore()
mmc1.loadDevice('cam', 'Andor', 'Andor')
mmc1.loadDevice('shutter', 'NI100x', 'DigitalIO')
#mmc1.loadDevice('autofocus', 'ASIStage', 'CRISP')
#mmc1.setSerialProperties('COM5', '500', '9600', '0.00', 'Off', 'None', '1')
mmc1.initializeAllDevices()

def valToType(val):
    if (val == 0):
        return "None"
    if (val == 1):
        return "String"
    if (val == 2):
        return "Float"
    if (val == 3):
        return "Int"
    
def listProps(mmcore, dev_label):
    dev_props = mmcore.getDevicePropertyNames(dev_label)
    for prop in dev_props:
        print prop, valToType(mmcore.getPropertyType(dev_label, prop)), mmcore.getProperty(dev_label, prop)
        if mmcore.hasPropertyLimits(dev_label, prop):
            print "  ", mmcore.getPropertyLowerLimit(dev_label, prop), mmc1.getPropertyUpperLimit(dev_label, prop)
    print ""
    
listProps(mmc1, 'autofocus')

'''
mmc1.initializeDevice("Andor")
mmc1.initializeDevice("CRISP")
'''


