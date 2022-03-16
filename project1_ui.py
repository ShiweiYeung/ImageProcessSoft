# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import numpy as np
import  sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, \
        QHBoxLayout, QVBoxLayout, QSizePolicy, \
        QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from hist_widget import histWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from image_viewer_widget import imageViewerWidget
from basic_image import basicImage
from binary_and_hist import *


class Ui_project1(QWidget):
    def setupUi(self, project1):
        project1.setObjectName("project1")
        project1.resize(1065, 849)

        self.initial_image_matrix = np.zeros([1, 1])
        self.initial_image_class = basicImage()
        self.binary_image_matrix = np.zeros([1, 1])
        # self.binary_image_class = basicImage()
        self.binary_thresuld = None

        project1.setFocusPolicy(QtCore.Qt.TabFocus)
        self.OTSUButton = QtWidgets.QPushButton(project1)
        self.OTSUButton.setGeometry(QtCore.QRect(70, 210, 141, 31))
        self.OTSUButton.setObjectName("OTSUButton")
        self.thresuld_scrollbar = QtWidgets.QScrollBar(project1)
        self.thresuld_scrollbar.setGeometry(QtCore.QRect(30, 270, 221, 21))
        self.thresuld_scrollbar.setAutoFillBackground(False)
        self.thresuld_scrollbar.setMinimum(20)
        self.thresuld_scrollbar.setMaximum(200)
        self.thresuld_scrollbar.setOrientation(QtCore.Qt.Horizontal)
        self.thresuld_scrollbar.setObjectName("thresuld_scrollbar")
        self.entropy_button = QtWidgets.QPushButton(project1)
        self.entropy_button.setGeometry(QtCore.QRect(70, 160, 141, 31))
        self.entropy_button.setObjectName("entropy_button")
        self.show_hist = QtWidgets.QPushButton(project1)
        self.show_hist.setGeometry(QtCore.QRect(70, 110, 141, 31))
        self.show_hist.setObjectName("show_hist")
        self.import_file = QtWidgets.QPushButton(project1)
        self.import_file.setGeometry(QtCore.QRect(70, 60, 141, 31))
        self.import_file.setObjectName("import_file")
        self.name_label_1 = QtWidgets.QLabel(project1)
        self.name_label_1.setGeometry(QtCore.QRect(430, 740, 111, 31))
        self.name_label_1.setObjectName("name_label_1")
        self.name_label_2 = QtWidgets.QLabel(project1)
        self.name_label_2.setGeometry(QtCore.QRect(770, 750, 101, 16))
        self.name_label_2.setObjectName("name_label_2")
        self.name_label_3 = QtWidgets.QLabel(project1)
        self.name_label_3.setGeometry(QtCore.QRect(620, 30, 91, 31))
        self.name_label_3.setObjectName("name_label_3")
        self.binary_image = imageViewerWidget(project1)
        self.binary_image.setGeometry(QtCore.QRect(670, 410, 311, 311))
        self.binary_image.setText("")
        self.binary_image.setScaledContents(True)
        self.binary_image.setObjectName("binary_image")
        self.initial_image = imageViewerWidget(project1)
        self.initial_image.setGeometry(QtCore.QRect(330, 410, 311, 311))
        self.initial_image.setText("")
        self.initial_image.setScaledContents(True)
        self.initial_image.setObjectName("initial_image")
        self.widget = histWidget(project1)
        self.widget.setGeometry(QtCore.QRect(331, 71, 651, 331))
        self.widget.setObjectName("widget")

        self.retranslateUi(project1)

        QtCore.QMetaObject.connectSlotsByName(project1)
        # self.import_file.clicked.connect(self.initial_image.show)
        self.show_hist.clicked.connect(self.widget.show)
        self.OTSUButton.clicked.connect(self.draw_OTSU_binary_image)
        self.entropy_button.clicked.connect(self.draw_entropy_binary_image)
        self.thresuld_scrollbar.valueChanged.connect(self.draw_scrollbar_binary_image)
        self.widget.valueChanged.connect(self.draw_threshold_binary_image)
        self.widget.mouse_clicked.connect(self.draw_mouse_binary_image)

        self.import_file.clicked.connect(self.actLoadImage)
        self.show_hist.clicked.connect(self.draw_histgram)

    def retranslateUi(self, project1):
        _translate = QtCore.QCoreApplication.translate
        project1.setWindowTitle(_translate("project1", "Form"))
        self.OTSUButton.setText(_translate("project1", "OTSU"))
        self.entropy_button.setText(_translate("project1", "entropy"))
        self.show_hist.setText(_translate("project1", "show hist"))
        self.import_file.setText(_translate("project1", "import file"))
        self.name_label_1.setText(_translate("project1", "initial image"))
        self.name_label_2.setText(_translate("project1", "binary image"))
        self.name_label_3.setText(_translate("project1", "histgram"))

    def actLoadImage(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setViewMode(QFileDialog.Detail)
        # dialog.setOption(QFileDialog.ShowDirsOnly, True)
        if dialog.exec_():
            imgPath = str(dialog.selectedFiles()[0])
            self.initial_image_class.loadImage(imgPath)
            self.initial_image_matrix = self.initial_image_class.getImage()
            self.initial_image.setImage(self.initial_image_matrix)

    def draw_histgram(self):
        self.widget.setImage(self.initial_image_matrix)

    def draw_OTSU_binary_image(self):
        self.binary_thresuld = OTSU_algorithm(self.initial_image_matrix)
        self.widget.setValue(self.binary_thresuld)

    def draw_entropy_binary_image(self):
        self.binary_thresuld = entropy_algorithm(self.initial_image_matrix)
        self.widget.setValue(self.binary_thresuld)

    def draw_threshold_binary_image(self):
        self.binary_image_matrix = threshold_binary_gray_image(self.initial_image_matrix, self.binary_thresuld)
        self.binary_image.setImage(self.binary_image_matrix)

    def draw_scrollbar_binary_image(self):
        self.binary_thresuld = self.thresuld_scrollbar.value()
        self.widget.setValue(self.binary_thresuld)

    def draw_mouse_binary_image(self):
        self.binary_thresuld = self.widget.mouse_value
        self.binary_image_matrix = threshold_binary_gray_image(self.initial_image_matrix, self.binary_thresuld)
        self.binary_image.setImage(self.binary_image_matrix)

class MyMainForm(QMainWindow, Ui_project1):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
 #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    QApplication.setStyle("fusion")
 #初始化
    myWin = MyMainForm()
 #将窗口控件显示在屏幕上
    myWin.show()
 #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())