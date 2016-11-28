#!/usr/bin/python
#
## @file
#
# Camera control specialized for a Hamamatsu camera.
#
# Hazen 09/15
#

from PyQt4 import QtCore
import os
import platform
import traceback

# Debugging
import sc_library.hdebug as hdebug

import sc_library.parameters as params
import camera.frame as frame
import camera.cameraControl as cameraControl
import sc_hardware.hamamatsu.hamamatsu_camera as hcam

## ACameraControl
#
# This class is used to control a Hamamatsu (sCMOS) camera.
#
class ACameraControl(cameraControl.HWCameraControl):

    ## __init__
    #
    # Create a Hamamatsu camera control object and initialize
    # the camera.
    #
    # @param hardware Camera hardware settings.
    # @param parent (Optional) The PyQt parent of this object.
    #
    @hdebug.debug
    def __init__(self, hardware, parameters, parent = None):
        cameraControl.HWCameraControl.__init__(self, hardware, parameters, parent)

        if hardware:
            self.camera = hcam.HamamatsuCameraMR(hardware.get("camera_id", 0))
        else:
            self.camera = hcam.HamamatsuCameraMR(0)

        # Add Hamatsu Flash4 specific camera parameters.
        cam_params = parameters.get("camera1")

        # FIXME: These should all be obtained by querying the camere.
        cam_params.add("max_intensity", params.ParameterInt("",
                                                            "max_intensity",
                                                            4096,
                                                            is_mutable = False,
                                                            is_saved = False))

        cam_params.add("x_start", params.ParameterRangeInt("AOI X start",
                                                           "x_start",
                                                           768, 0, 2046))
        cam_params.add("x_end", params.ParameterRangeInt("AOI X end",
                                                         "x_end",
                                                         1279, 1, 2047))
        cam_params.add("y_start", params.ParameterRangeInt("AOI Y start",
                                                           "y_start",
                                                           768, 0, 2046))
        cam_params.add("y_end", params.ParameterRangeInt("AOI Y end",
                                                         "y_end",
                                                         1279, 1, 2047))

        cam_params.add("x_bin", params.ParameterRangeInt("Binning in X",
                                                         "x_bin",
                                                         1, 1, 4))
        cam_params.add("y_bin", params.ParameterRangeInt("Binning in Y",
                                                         "y_bin",
                                                         1, 1, 4))

        cam_params.add("exposure_time", params.ParameterRangeFloat("Exposure time (seconds)", 
                                                                   "exposure_time", 
                                                                   0.01, 0.0, 60.0))

        cam_params.add("defect_correct_mode", params.ParameterSetInt("Defect correction mode",
                                                                     "defect_correct_mode",
                                                                     1, [0, 1]))

        cam_params.add("external_trigger", params.ParameterSetInt("Use external trigger",
                                                                  "external_trigger",
                                                                  0, [0, 1]))


    ## getAcquisitionTimings
    #
    # Returns the internal frame rate of the camera.
    #
    # @param which_camera The camera to get the timing information for.
    #
    # @return A python array containing the inverse of the internal frame rate.
    #
    @hdebug.debug
    def getAcquisitionTimings(self, which_camera):

        # The camera frame rate seems to be max(exposure time, readout time).
        # This number may not be good accurate enough for shutter synchronization?
        exposure_time = self.camera.getPropertyValue("exposure_time")[0]
        readout_time = self.camera.getPropertyValue("timing_readout_time")[0]
        if (exposure_time < readout_time):
            frame_rate = 1.0/readout_time

            # Print a warning since the user probably does not want this to be true.
            hdebug.logText("Camera exposure time (" + str(exposure_time) + ") is less than the readout time (" + str(readout_time), True)

        else:
            frame_rate = 1.0/exposure_time

        temp = 1.0/frame_rate
        return [temp, temp]

    ## newParameters
    #
    # Update the camera parameters based on a new parameters object.
    #
    # @param parameters A parameters object.
    #
    @hdebug.debug
    def newParameters(self, parameters):
        p = parameters.get("camera1")

        size_x = (p.get("x_end") - p.get("x_start") + 1)/p.get("x_bin")
        size_y = (p.get("y_end") - p.get("y_start") + 1)/p.get("y_bin")
        p.set("x_pixels", size_x)
        p.set("y_pixels", size_y)

        try:
            # Set ROI location and size.
            self.camera.setPropertyValue("subarray_hpos", p.get("x_start"))
            self.camera.setPropertyValue("subarray_hsize", p.get("x_pixels"))
            self.camera.setPropertyValue("subarray_vpos", p.get("y_start"))
            self.camera.setPropertyValue("subarray_vsize", p.get("y_pixels"))

            # Set binning.
            if (p.get("x_bin") != p.get("y_bin")):
                raise AssertionError("unequal binning is not supported.")
            if (p.get("x_bin") == 1):
                self.camera.setPropertyValue("binning", "1x1")
            elif (p.get("x_bin") == 2):
                self.camera.setPropertyValue("binning", "2x2")
            elif (p.get("x_bin") == 4):
                self.camera.setPropertyValue("binning", "4x4")
            else:
                raise AssertionError("unsupported bin size", p.get("x_bin"))

            # Set the rest of the hamamatsu properties.
            #
            # Note: These could overwrite the above. For example, if you
            #   have both "x_start" and "subarray_hpos" in the parameters
            #   file then "subarray_hpos" will overwrite "x_start". Trouble
            #   may follow if they are not set to the same value.
            #
            for key in p.getAttrs():
                if (key == "binning"): # sigh..
                    continue
                if self.camera.isCameraProperty(key):
                    self.camera.setPropertyValue(key, p.get(key))

            # Set camera sub-array mode so that it will return the correct frame rate.
            self.camera.setSubArrayMode()

            p.set("bytes_per_frame", 2 * p.get("x_pixels") * p.get("y_pixels") / (p.get("x_bin") * p.get("y_bin")))

            self.got_camera = True

        except hcam.DCAMException:
            hdebug.logText("QCameraThread: Bad camera settings")
            print traceback.format_exc()
            self.got_camera = False

        self.parameters = p

    ## quit
    #
    # Stops the camera thread and shutsdown the camera.
    #
    @hdebug.debug
    def quit(self):
        self.stopThread()
        self.wait()
        self.camera.shutdown()

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

