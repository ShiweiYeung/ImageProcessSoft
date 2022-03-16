#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2 as cv
from PyQt5.QtCore import pyqtSignal, QObject

class basicImage(QObject):
    imageChanged = pyqtSignal()
    def __init__(self, parent=None):
        super(basicImage, self).__init__(parent)
        self.__image = None

    # reset only variables define in current class
    def __reset(self):
        self.__image = None

    # reset all
    def reset(self):
        self.__reset()
    

    @staticmethod
    def __checkImage(image):
        assert image is not None, 'empty image'
        assert isinstance(image, np.ndarray), 'image should be numpy array'
        assert image.ndim == 2, 'greyscale image only'
        assert image.dtype == np.uint8, 'uint8 pixel type only'

    # set current image
    def setImage(self, image):
        print('image set')
        if (self.__image is not None) and np.array_equal(self.__image, image):
            return
        self.__checkImage(image)
        self.__reset()
        self.__image = image
        print('image emited!')
        self.imageChanged.emit()

    # get current image
    def getImage(self):
        assert self.__image is not None, 'image unset'
        return self.__image.copy()

    # read image from file
    def loadImage(self, imgPath):
        image = cv.imread(imgPath, cv.IMREAD_GRAYSCALE) # greyscale, uint8 img
        self.setImage(image)

