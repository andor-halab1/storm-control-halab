#!/usr/bin/python
#
## @file
#
# Conversion of XML node(s) to dictionaries.
#
# Hazen 09/14
#

# Frank 04/02/16
from xml.etree import ElementTree

## gf
#
# Return a function that can be used to extract the value of a field from an ElementTree node.
#  Function arguments:
#   param: node A ElementTree xml node.
#
# @param field The name of the field (or None).
# @param convert_fn The function to use for conversion, or None if no conversion is desired.
# @param default_value (Optional) The value to return if the field is not found.
#
# @return A function for extracting a field from an ElementTree node.
#
def gf(field, convert_fns, default_value = None):
    def getField(node):
        temp = node.find(field)
        if temp is not None:
            for convert_fn in convert_fns:
                try:
                    return convert_fn(temp.text)
                except:
                    pass
            return temp # No conversion
        else:
            return default_value
    return getField

## booleanConversion
#
# Return a boolean based on the string or integer value of entry
#
# @parame value The value to be converted
#
# @return A boolean based on the value of entry
#
def boolConv(value):
    if (value == "False") or (value == "false") or (value == 0):
        return False
    else:
        return True

movie_node_conversion = {"delay" : gf("delay", [int]),
                         "directory" : gf("directory", [str]),
                         "find_sum" : gf("find_sum", [float]),
                         "check_focus": gf("check_focus", [None]),
                         "length" : gf("length", [int]),
                         "lock_target" : gf("lock_target", [float]),
                         "name" : gf("name", [str]),
                         "min_spots" : gf("min_spots", [int]),
                         "overwrite" : gf("overwrite", [boolConv]),
                         "parameters" : gf("parameters", [int,str]),
                         "pause" : gf("pause", [boolConv]),
                         "progression" : gf("progression", [None]),
                         "recenter" : gf("recenter", [boolConv]),
                         "stage_x" : gf("stage_x", [float]),
                         "stage_y" : gf("stage_y", [float])}

## movieNodeToDict
#
# Convert a xml movie to a dictionary.
#
# @param movie_node The xml of a movie node.
#
# @return A dictionary describing the movie node.
#
# Frank 04/01/16
#
def movieNodeToDict(movie_node):
    dict = {}
    cf_element = ElementTree.Element("check_focus")
    ElementTree.SubElement(cf_element,"focus_scan")
    flag = 0
    
    for field in movie_node_conversion.keys():
        value = movie_node_conversion[field](movie_node)
        if value is not None:
            dict[field] = value
            
    name_seg = dict["name"].split('_')
    name_length = len(name_seg)
    if (int(name_seg[name_length-1]) % 5) == 0:
        if "check_focus" in dict.keys():
            if dict["check_focus"].find("focus_scan"):
                pass
            else:
                ElementTree.SubElement(dict["check_focus"],"focus_scan")
        else:
            dict["check_focus"] = cf_element

    if "check_focus" in dict.keys():
        for node in dict["check_focus"]:
            if node.tag == "focus_scan":
                flag = 1
    
    if flag == 1:
        dict["length"] = dict["length"] + 520
    
    return dict

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
