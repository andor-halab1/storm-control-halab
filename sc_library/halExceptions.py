#!/usr/bin/python
#
## @file
#
# Defines a series of abstract exceptions that can be sub-classed and which Hal
# can recognize
#
# Jeffrey Moffitt 3/16
#


class HalException(Exception):
    pass

## Hardware Exception
#
# A generic hardware exception.
#
class HardwareException(HalException):

    def __init__(self, message):
        HalException.__init__(self, message)


## Module Exception
#
# A generic hal module exception.
#
class ModuleException(HalException):

    def __init__(self, message):
        HalException.__init__(self, message)

## GUI Exception
#
# A generic hal gui exception.
#
class GUIException(HalException):

    def __init__(self, message):
        HalException.__init__(self, message)

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
