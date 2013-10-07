#!/usr/bin/python
#
# qtCameraWidget specialized for data from a Andor camera.
#
# Hazen 06/12
#

import numpy
from PyQt4 import QtCore, QtGui

import qtWidgets.qtCameraWidget as qtCameraWidget

# Andor Camera Widget
class ACameraWidget(qtCameraWidget.QCameraWidget):

    def __init__(self, parameters, parent = None):
        qtCameraWidget.QCameraWidget.__init__(self, parameters, parent)

#    def updateImageWithFrame(self, frame):
#        if frame:
#            w = frame.image_x
#            h = frame.image_y
#            image_data = numpy.fromstring(frame.data, dtype=numpy.uint16)
#            image_data = image_data.reshape((h,w))
#            self.image_min = numpy.min(image_data)
#            self.image_max = numpy.max(image_data)
#
#            if self.flip_vertical:
#                image_data = numpy.flipud(image_data)
#
#            if self.flip_horizontal:
#                image_data = numpy.fliplr(image_data)
#
#            temp = image_data.astype(numpy.float32)
#            temp = 255.0*(temp - self.display_range[0])/(self.display_range[1] - self.display_range[0])
#            temp[(temp > 255.0)] = 255.0
#            temp[(temp < 0.0)] = 0.0
#            temp = temp.astype(numpy.uint8)
#
#            self.image = QtGui.QImage(temp.data, w, h, QtGui.QImage.Format_Indexed8)
#            self.image.ndarray = temp
#
#            self.setColorTable()
#            self.update()
#
#            if self.show_info:
#                x_loc = self.x_click
#                y_loc = self.y_click
#                value = 0
#                if ((x_loc >= 0) and (x_loc < w) and (y_loc >= 0) and (y_loc < h)):
#                    value = image_data[y_loc, x_loc]
#                    self.intensityInfo.emit(x_loc, y_loc, value)

#
# The MIT License
#
# Copyright (c) 2012 Zhuang Lab, Harvard University
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
