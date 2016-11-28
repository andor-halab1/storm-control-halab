#!/usr/bin/python
#
## @file
#
# A very simple git parser.
#
# Hazen 05/14
#

import os

branch = ""
version = ""

try:
    directory = os.path.abspath(__file__)
    git_dir = os.path.join(os.path.split(os.path.split(directory)[0])[0], ".git")

    fp = open(os.path.join(git_dir, "HEAD"))
    ref = fp.readline().rstrip().split(" ")[1]
    branch = os.path.basename(ref)
    fp.close()

    fp = open(os.path.join(git_dir, ref))
    version = fp.readline().rstrip()
    fp.close()
except:
    print "Did not find .git directory here:", git_dir

def getBranch():
    return branch

def getVersion():
    return version

if __name__ == "__main__":
    print "Branch:", branch
    print "Version:", version

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
