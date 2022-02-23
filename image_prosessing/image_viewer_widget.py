#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QSlider, QLabel, QScrollArea, \
        QHBoxLayout, QVBoxLayout, QSizePolicy
from PyQt5.QtGui import QImage, QPixmap, QPalette
from PyQt5.QtCore import Qt, pyqtSlot, QPoint

import numpy as np

def array2Pixmap(array):
    assert (array.ndim==2) or (array.ndim==3 and array.shape[2]==3), \
            'Only 2D grayscale or bgr image is supported'
    if not array.dtype== np.uint8:
        array=array.astype(np.uint8)
    if array.ndim == 2:
        array = np.stack([array, array, array], axis=-1)
    img = QImage(array.copy().data, \
            array.shape[1], array.shape[0],array.shape[1]*3, QImage.Format_RGB888)
    pixmap = QPixmap.fromImage(img)
    return pixmap




class imageViewerWidget(QLabel):
    def __init__(self, parent=None):
        super(imageViewerWidget, self).__init__(parent)
        self.resize(400,400)
        self.adjustSize()

    def reset(self):
        self.setText('Not Available')

    def setImage(self, image):
        assert image.ndim == 2, "accepts 2D grayscale image only"
        pixmap = array2Pixmap(image)
        self.setPixmap(pixmap)
