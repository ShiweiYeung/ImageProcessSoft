# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project3.ui'
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
from PyQt5.QtCore import QTimer
from hist_widget import histWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from image_viewer_widget import imageViewerWidget
from basic_image import basicImage
from binary_and_hist import *
from PyQt5 import QtCore, QtGui, QtWidgets
from binary_morphology_image import *
from skimage.morphology import square,diamond,disk

class Ui_project3(QWidget):
    def setupUi(self, project3):
        project3.setObjectName("project3")
        project3.resize(1034, 849)
        project3.setFocusPolicy(QtCore.Qt.TabFocus)
        self.opening_button = QtWidgets.QPushButton(project3)
        self.opening_button.setGeometry(QtCore.QRect(70, 210, 141, 31))
        self.opening_button.setObjectName("opening_button")
        self.erosion_button = QtWidgets.QPushButton(project3)
        self.erosion_button.setGeometry(QtCore.QRect(70, 160, 141, 31))
        self.erosion_button.setObjectName("erosion_button")
        self.dilation_button = QtWidgets.QPushButton(project3)
        self.dilation_button.setGeometry(QtCore.QRect(70, 110, 141, 31))
        self.dilation_button.setObjectName("dilation_button")
        self.import_file = QtWidgets.QPushButton(project3)
        self.import_file.setGeometry(QtCore.QRect(70, 60, 141, 31))
        self.import_file.setObjectName("import_file")
        self.name_label_1 = QtWidgets.QLabel(project3)
        self.name_label_1.setGeometry(QtCore.QRect(310, 780, 251, 31))
        self.name_label_1.setObjectName("name_label_1")
        self.binary_morphological_image = imageViewerWidget(project3)
        self.binary_morphological_image.setGeometry(QtCore.QRect(280, 440, 321, 321))
        self.binary_morphological_image.setText("")
        self.binary_morphological_image.setScaledContents(True)
        self.binary_morphological_image.setObjectName("binary_morphological_image")
        self.closing_button = QtWidgets.QPushButton(project3)
        self.closing_button.setGeometry(QtCore.QRect(70, 260, 141, 31))
        self.closing_button.setObjectName("closing_button")
        self.name_label_4 = QtWidgets.QLabel(project3)
        self.name_label_4.setGeometry(QtCore.QRect(380, 370, 111, 31))
        self.name_label_4.setObjectName("name_label_4")
        self.name_label_5 = QtWidgets.QLabel(project3)
        self.name_label_5.setGeometry(QtCore.QRect(740, 380, 101, 16))
        self.name_label_5.setObjectName("name_label_5")
        self.binary_image = imageViewerWidget(project3)
        self.binary_image.setGeometry(QtCore.QRect(630, 30, 321, 321))
        self.binary_image.setText("")
        self.binary_image.setScaledContents(True)
        self.binary_image.setObjectName("binary_image")
        self.initial_image = imageViewerWidget(project3)
        self.initial_image.setGeometry(QtCore.QRect(280, 30, 321, 321))
        self.initial_image.setText("")
        self.initial_image.setScaledContents(True)
        self.initial_image.setObjectName("initial_image")
        self.structuring_box = QtWidgets.QComboBox(project3)
        self.structuring_box.setGeometry(QtCore.QRect(70, 340, 131, 21))
        self.structuring_box.setObjectName("structuring_box")
        self.structuring_box.addItem("")
        self.structuring_box.addItem("")
        self.structuring_box.addItem("")
        self.spinBox = QtWidgets.QSpinBox(project3)
        self.spinBox.setGeometry(QtCore.QRect(150, 380, 46, 22))
        self.spinBox.setMinimum(3)
        self.spinBox.setMaximum(10)
        self.spinBox.setObjectName("spinBox")
        self.distance_button = QtWidgets.QPushButton(project3)
        self.distance_button.setGeometry(QtCore.QRect(70, 420, 141, 31))
        self.distance_button.setObjectName("distance_button")
        self.skeleton_button = QtWidgets.QPushButton(project3)
        self.skeleton_button.setGeometry(QtCore.QRect(70, 470, 141, 31))
        self.skeleton_button.setObjectName("skeleton_button")
        self.skeleton_reconstruction_button = QtWidgets.QPushButton(project3)
        self.skeleton_reconstruction_button.setGeometry(QtCore.QRect(70, 520, 141, 31))
        self.skeleton_reconstruction_button.setObjectName("skeleton_reconstruction_button")
        self.select_SE = QtWidgets.QLabel(project3)
        self.select_SE.setGeometry(QtCore.QRect(70, 310, 101, 21))
        self.select_SE.setObjectName("select_SE")
        self.SE_size = QtWidgets.QLabel(project3)
        self.SE_size.setGeometry(QtCore.QRect(70, 380, 71, 21))
        self.SE_size.setObjectName("SE_size")
        self.skeletonreconstruction_image = imageViewerWidget(project3)
        self.skeletonreconstruction_image.setGeometry(QtCore.QRect(630, 440, 321, 321))
        self.skeletonreconstruction_image.setText("")
        self.skeletonreconstruction_image.setScaledContents(True)
        self.skeletonreconstruction_image.setObjectName("skeletonreconstruction_image")
        self.name_label_2 = QtWidgets.QLabel(project3)
        self.name_label_2.setGeometry(QtCore.QRect(690, 780, 201, 31))
        self.name_label_2.setObjectName("name_label_2")

        self.retranslateUi(project3)
        QtCore.QMetaObject.connectSlotsByName(project3)

        self.initial_image_matrix = np.zeros([1, 1])
        self.initial_image_class = basicImage()
        self.binary_image_matrix = np.zeros([1, 1])
        self.skeletonreconstruction_image_matrix=np.zeros([1, 1])
        self.binary_morphological_image_matrix=np.zeros([1, 1])
        self.binary_distance_matrix=np.zeros([1, 1])
        self.binary_skeleton_matrix = np.zeros([1, 1])
        self.binary_thresuld = None
        self.temp_struct = np.zeros([3, 3])+1

        self.import_file.clicked.connect(self.actLoadImage)
        self.dilation_button.clicked.connect(self.draw_binary_dilation_image)
        self.erosion_button.clicked.connect(self.draw_binary_erosion_image)
        self.opening_button.clicked.connect(self.draw_binary_opening_image)
        self.closing_button.clicked.connect(self.draw_binary_closing_image)
        self.skeleton_button.clicked.connect(self.draw_binary_skeleton_image)
        self.distance_button.clicked.connect(self.draw_binary_distance_image)
        self.skeleton_reconstruction_button.clicked.connect(self.draw_binary_skeleton_reconstruction_image)
        self.spinBox.valueChanged.connect(self.change_binary_struct)
        self.structuring_box.currentIndexChanged.connect(self.change_binary_struct)



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
            self.binary_image_matrix=255*entropy_binary_gray_image(self.initial_image_matrix)
            self.binary_image.setImage(self.binary_image_matrix)
    def change_binary_struct(self):
        if self.structuring_box.currentIndex()==0:
            self.temp_struct=disk(int((self.spinBox.value()-1)/2))
            # print((int(self.spinBox.value()-1)/2))
            # print(self.temp_struct)
        else:
            if self.structuring_box.currentIndex()==1:
                self.temp_struct = diamond(int((self.spinBox.value()-1)/2))
                # print((int(self.spinBox.value() - 1) / 2))
                # print(self.temp_struct)
            else:
                self.temp_struct = square(self.spinBox.value())
                # print(self.temp_struct)
    def draw_binary_dilation_image(self):
        # if self.structuring_box.currentIndex()==0:
        #     self.temp_struct=disk(self.spinBox.value())
        # else:
        #     if self.structuring_box.currentIndex()==1:
        #         self.temp_struct = diamond(self.spinBox.value())
        #     else:
        #         self.temp_struct = square(self.spinBox.value())
        self.binary_morphological_image_matrix=binary_morphology_dilation(self.binary_image_matrix,self.temp_struct)
        self.binary_morphological_image.setImage(self.binary_morphological_image_matrix)
    def draw_binary_erosion_image(self):
        # if self.structuring_box.currentIndex()==0:
        #     self.temp_struct=disk(self.spinBox.value())
        # else:
        #     if self.structuring_box.currentIndex()==1:
        #         self.temp_struct = diamond(self.spinBox.value())
        #     else:
        #         self.temp_struct = square(self.spinBox.value())
        self.binary_morphological_image_matrix=binary_morphology_erosion(self.binary_image_matrix,self.temp_struct)
        self.binary_morphological_image.setImage(self.binary_morphological_image_matrix)
    def draw_binary_opening_image(self):
        # if self.structuring_box.currentIndex()==0:
        #     self.temp_struct=disk(self.spinBox.value())
        # else:
        #     if self.structuring_box.currentIndex()==1:
        #         self.temp_struct = diamond(self.spinBox.value())
        #     else:
        #         self.temp_struct = square(self.spinBox.value())
        self.binary_morphological_image_matrix=binary_morphology_open(self.binary_image_matrix,self.temp_struct)
        self.binary_morphological_image.setImage(self.binary_morphological_image_matrix)
    def draw_binary_closing_image(self):
        # if self.structuring_box.currentIndex()==0:
        #     self.temp_struct=disk(self.spinBox.value())
        # else:
        #     if self.structuring_box.currentIndex()==1:
        #         self.temp_struct = diamond(self.spinBox.value())
        #     else:
        #         self.temp_struct = square(self.spinBox.value())
        self.binary_morphological_image_matrix=binary_morphology_close(self.binary_image_matrix,self.temp_struct)
        self.binary_morphological_image.setImage(self.binary_morphological_image_matrix)
    def draw_binary_skeleton_image(self):
        self.binary_distance_matrix,self.binary_skeleton_matrix,self.skeletonreconstruction_image_matrix=binary_morphology_distance(self.binary_image_matrix,self.temp_struct)
        self.max_skeleton_time=self.binary_skeleton_matrix.shape[2]
        # self.binary_distance_matrix=(self.binary_distance_matrix/np.max(self.binary_distance_matrix)*255).astype(np.uint8)
        self.timer=QTimer()
        self.timer.setInterval(200)
        self.timer.start()
        self.timer.timeout.connect(self.draw_binary_skeleton)

    def draw_binary_skeleton(self):
        # print(self.max_skeleton_time)
        temp_dim=self.binary_skeleton_matrix.shape[2]-self.max_skeleton_time
        self.binary_morphological_image.setImage(self.binary_skeleton_matrix[:,:,temp_dim])
        self.max_skeleton_time-=1
        if self.max_skeleton_time==0:
            if self.timer.isActive():
                self.timer.stop()
    def draw_binary_distance_image(self):
        self.binary_distance_matrix,self.binary_skeleton_matrix,self.skeletonreconstruction_image_matrix=binary_morphology_distance(self.binary_image_matrix,self.temp_struct)
        self.max_skeleton_time=self.binary_distance_matrix.shape[2]
        self.timer=QTimer()
        self.timer.setInterval(200)
        self.timer.start()
        self.timer.timeout.connect(self.draw_binary_distance)

    def draw_binary_distance(self):
        # print(self.max_skeleton_time)
        temp_dim=self.binary_distance_matrix.shape[2]-self.max_skeleton_time
        self.binary_morphological_image.setImage(self.binary_distance_matrix[:,:,temp_dim])
        self.max_skeleton_time-=1
        if self.max_skeleton_time==0:
            if self.timer.isActive():
                self.timer.stop()
    def draw_binary_skeleton_reconstruction_image(self):
        self.skeletonreconstruction_image_matrix=binary_morphology_skeleton_reconstruct(self.skeletonreconstruction_image_matrix,self.temp_struct)
        self.max_skeleton_time = self.skeletonreconstruction_image_matrix.shape[2]
        self.timer = QTimer()
        self.timer.setInterval(200)
        self.timer.start()
        self.timer.timeout.connect(self.binary_skeleton_reconstruction)
    def binary_skeleton_reconstruction(self):
        temp_dim = self.skeletonreconstruction_image_matrix.shape[2] - self.max_skeleton_time
        self.skeletonreconstruction_image.setImage(self.skeletonreconstruction_image_matrix[:, :, temp_dim])
        self.max_skeleton_time -= 1
        if self.max_skeleton_time == 0:
            if self.timer.isActive():
                self.timer.stop()



    def retranslateUi(self, project3):
        _translate = QtCore.QCoreApplication.translate
        project3.setWindowTitle(_translate("project3", "Form"))
        self.opening_button.setText(_translate("project3", "opening"))
        self.erosion_button.setText(_translate("project3", "erosion"))
        self.dilation_button.setText(_translate("project3", "dilation"))
        self.import_file.setText(_translate("project3", "import file"))
        self.name_label_1.setText(_translate("project3", "binary morphological operation"))
        self.closing_button.setText(_translate("project3", "closing"))
        self.name_label_4.setText(_translate("project3", "initial image"))
        self.name_label_5.setText(_translate("project3", "binary image"))
        self.structuring_box.setItemText(0, _translate("project3", "Euclidean"))
        self.structuring_box.setItemText(1, _translate("project3", "city"))
        self.structuring_box.setItemText(2, _translate("project3", "chessboard"))
        self.distance_button.setText(_translate("project3", "distance"))
        self.skeleton_button.setText(_translate("project3", "skeleton"))
        self.skeleton_reconstruction_button.setText(_translate("project3", "reconstruction"))
        self.select_SE.setText(_translate("project3", "select SE:"))
        self.SE_size.setText(_translate("project3", "SE size:"))
        self.name_label_2.setText(_translate("project3", "skeleton reconstruction"))

class MyMainForm(QMainWindow, Ui_project3):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    QApplication.setStyle("fusion")
    # 初始化
    myWin = MyMainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())

