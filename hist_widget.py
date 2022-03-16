#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QSizePolicy
from PyQt5.QtCore import pyqtSignal

import matplotlib

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.lines import Line2D

class histWidget(FigureCanvas):
    valueChanged = pyqtSignal(float)
    mouse_clicked = pyqtSignal(float)
    def __init__(self, parent=None):
        self.__fig = Figure()
        super(histWidget, self).__init__(self.__fig)
        self.__axes = self.__fig.subplots()
        self.__line = None
        self.setParent(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mpl_connect('button_press_event',  self.__onMousePress)        
        self.__value = None
        self.mouse_value = None
    
    def __drawLine(self, value):
        if self.__line is not None:
            self.__line.remove()
        ylim = self.__axes.get_ylim()
        self.__line = Line2D([value, value], ylim, color='red',linewidth=8)
        #print('drawing ylim'+str(ylim))
        self.__axes.add_line(self.__line)
        self.draw()

    
    def __drawHist(self, x):
        self.__line = None
        self.__axes.cla()
        retval = self.__axes.hist(x, bins=50,density=True)
        self.draw()
        return retval
    
    def __onMousePress(self, event):

        xdata = event.xdata
        if xdata is not None:
            self.__drawLine(event.xdata)
            self.setValue(xdata)
            self.mouse_value = xdata
            self.mouse_clicked.emit(self.__value)

    
    def setValue(self, value):
        self.__value = value
        self.__drawLine(value)
        self.valueChanged.emit(value)
    
    def setImage(self, image):
        self.__drawHist(image.ravel())

