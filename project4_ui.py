# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import  sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, \
        QHBoxLayout, QVBoxLayout, QSizePolicy, \
        QFileDialog
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from image_viewer_widget import imageViewerWidget
from basic_image import basicImage
from binary_and_hist import *
from PyQt5 import QtCore, QtGui, QtWidgets
from binary_morphology_image import *
from skimage.morphology import square,diamond,disk
from higt_level_morphology_image import *

class Ui_project4(QWidget):
    def setupUi(self, project4):
        project4.setObjectName("project4")
        project4.resize(1065, 849)
        project4.setFocusPolicy(QtCore.Qt.TabFocus)
        self.opening_button = QtWidgets.QPushButton(project4)
        self.opening_button.setGeometry(QtCore.QRect(70, 210, 141, 31))
        self.opening_button.setObjectName("opening_button")
        self.erosion_button = QtWidgets.QPushButton(project4)
        self.erosion_button.setGeometry(QtCore.QRect(70, 160, 141, 31))
        self.erosion_button.setObjectName("erosion_button")
        self.dilation_button = QtWidgets.QPushButton(project4)
        self.dilation_button.setGeometry(QtCore.QRect(70, 110, 141, 31))
        self.dilation_button.setObjectName("dilation_button")
        self.import_file = QtWidgets.QPushButton(project4)
        self.import_file.setGeometry(QtCore.QRect(70, 60, 141, 31))
        self.import_file.setObjectName("import_file")
        self.name_label_1 = QtWidgets.QLabel(project4)
        self.name_label_1.setGeometry(QtCore.QRect(410, 780, 71, 31))
        self.name_label_1.setObjectName("name_label_1")
        self.marker_image = imageViewerWidget(project4)
        self.marker_image.setGeometry(QtCore.QRect(280, 440, 321, 321))
        self.marker_image.setText("")
        self.marker_image.setScaledContents(True)
        self.marker_image.setObjectName("marker_image")
        self.closing_button = QtWidgets.QPushButton(project4)
        self.closing_button.setGeometry(QtCore.QRect(70, 260, 141, 31))
        self.closing_button.setObjectName("closing_button")
        self.name_label_4 = QtWidgets.QLabel(project4)
        self.name_label_4.setGeometry(QtCore.QRect(380, 370, 111, 31))
        self.name_label_4.setObjectName("name_label_4")
        self.name_label_5 = QtWidgets.QLabel(project4)
        self.name_label_5.setGeometry(QtCore.QRect(660, 380, 271, 20))
        self.name_label_5.setObjectName("name_label_5")
        self.gray_morphological_image = imageViewerWidget(project4)
        self.gray_morphological_image.setGeometry(QtCore.QRect(630, 30, 321, 321))
        self.gray_morphological_image.setText("")
        self.gray_morphological_image.setScaledContents(True)
        self.gray_morphological_image.setObjectName("gray_morphological_image")
        self.initial_image = imageViewerWidget(project4)
        self.initial_image.setGeometry(QtCore.QRect(280, 30, 321, 321))
        self.initial_image.setText("")
        self.initial_image.setScaledContents(True)
        self.initial_image.setObjectName("initial_image")
        self.structuring_box = QtWidgets.QComboBox(project4)
        self.structuring_box.setGeometry(QtCore.QRect(70, 340, 131, 21))
        self.structuring_box.setObjectName("structuring_box")
        self.structuring_box.addItem("")
        self.structuring_box.addItem("")
        self.structuring_box.addItem("")
        self.spinBox = QtWidgets.QSpinBox(project4)
        self.spinBox.setGeometry(QtCore.QRect(150, 380, 46, 22))
        self.spinBox.setMinimum(3)
        self.spinBox.setMaximum(10)
        self.spinBox.setObjectName("spinBox")
        self.binary_reconstruct_by_select_marker_button = QtWidgets.QPushButton(project4)
        self.binary_reconstruct_by_select_marker_button.setGeometry(QtCore.QRect(150, 590, 101, 31))
        self.binary_reconstruct_by_select_marker_button.setObjectName("binary_reconstruct_by_select_marker_button")
        self.select_SE = QtWidgets.QLabel(project4)
        self.select_SE.setGeometry(QtCore.QRect(70, 310, 101, 21))
        self.select_SE.setObjectName("select_SE")
        self.SE_size = QtWidgets.QLabel(project4)
        self.SE_size.setGeometry(QtCore.QRect(70, 380, 71, 21))
        self.SE_size.setObjectName("SE_size")
        self.reconstruction_image = imageViewerWidget(project4)
        self.reconstruction_image.setGeometry(QtCore.QRect(630, 440, 321, 321))
        self.reconstruction_image.setText("")
        self.reconstruction_image.setScaledContents(True)
        self.reconstruction_image.setObjectName("reconstruction_image")
        self.name_label_2 = QtWidgets.QLabel(project4)
        self.name_label_2.setGeometry(QtCore.QRect(740, 780, 121, 31))
        self.name_label_2.setObjectName("name_label_2")
        self.edge_detect_label = QtWidgets.QLabel(project4)
        self.edge_detect_label.setGeometry(QtCore.QRect(70, 420, 101, 21))
        self.edge_detect_label.setObjectName("edge_detect_label")
        self.edge_type_box = QtWidgets.QComboBox(project4)
        self.edge_type_box.setGeometry(QtCore.QRect(70, 450, 131, 21))
        self.edge_type_box.setObjectName("edge_type_box")
        self.edge_type_box.addItem("")
        self.edge_type_box.addItem("")
        self.edge_type_box.addItem("")
        self.gradient_type_box = QtWidgets.QComboBox(project4)
        self.gradient_type_box.setGeometry(QtCore.QRect(70, 520, 131, 21))
        self.gradient_type_box.setObjectName("gradient_type_box")
        self.gradient_type_box.addItem("")
        self.gradient_type_box.addItem("")
        self.gradient_type_box.addItem("")
        self.gradient_label = QtWidgets.QLabel(project4)
        self.gradient_label.setGeometry(QtCore.QRect(70, 490, 101, 21))
        self.gradient_label.setObjectName("gradient_label")
        self.binary_reconstruct_label = QtWidgets.QLabel(project4)
        self.binary_reconstruct_label.setGeometry(QtCore.QRect(30, 560, 221, 21))
        self.binary_reconstruct_label.setObjectName("binary_reconstruct_label")
        self.binary_select_marker_button = QtWidgets.QPushButton(project4)
        self.binary_select_marker_button.setGeometry(QtCore.QRect(30, 590, 111, 31))
        self.binary_select_marker_button.setObjectName("binary_select_marker_button")
        self.binary_reconstruct_by_open_button = QtWidgets.QPushButton(project4)
        self.binary_reconstruct_by_open_button.setGeometry(QtCore.QRect(50, 630, 171, 31))
        self.binary_reconstruct_by_open_button.setObjectName("binary_reconstruct_by_open_button")
        self.gray_OBR_botton = QtWidgets.QPushButton(project4)
        self.gray_OBR_botton.setGeometry(QtCore.QRect(60, 710, 71, 31))
        self.gray_OBR_botton.setObjectName("gray_OBR_botton")
        self.gray_reconstruct_label = QtWidgets.QLabel(project4)
        self.gray_reconstruct_label.setGeometry(QtCore.QRect(40, 680, 221, 21))
        self.gray_reconstruct_label.setObjectName("gray_reconstruct_label")
        self.gray_CBR_button = QtWidgets.QPushButton(project4)
        self.gray_CBR_button.setGeometry(QtCore.QRect(140, 710, 71, 31))
        self.gray_CBR_button.setObjectName("gray_CBR_button")

        self.retranslateUi(project4)
        QtCore.QMetaObject.connectSlotsByName(project4)

        self.initial_image_matrix = np.zeros([1, 1])
        self.initial_image_class = basicImage()
        self.marker_image_class = basicImage()
        self.binary_image_matrix = np.zeros([1, 1])
        self.reconstruction_image_matrix = np.zeros([1, 1])
        self.gray_morphological_image_matrix = np.zeros([1, 1])
        self.marker_image_matrix = np.zeros([1, 1])
        # self.binary_distance_matrix = np.zeros([1, 1])
        # self.binary_skeleton_matrix = np.zeros([1, 1])
        self.binary_thresuld = None
        self.temp_struct = np.zeros([3,3])+1

        self.import_file.clicked.connect(self.actLoadImage)
        self.spinBox.valueChanged.connect(self.change_binary_struct)
        self.structuring_box.currentIndexChanged.connect(self.change_binary_struct)
        self.dilation_button.clicked.connect(self.draw_gray_dilation_image)
        self.erosion_button.clicked.connect(self.draw_gray_erosion_image)
        self.opening_button.clicked.connect(self.draw_gray_opening_image)
        self.closing_button.clicked.connect(self.draw_gray_closing_image)
        self.gradient_type_box.currentIndexChanged.connect(self.draw_morphological_gradient_image)
        self.edge_type_box.currentIndexChanged.connect(self.draw_morphological_edge_image)
        self.binary_select_marker_button.clicked.connect(self.select_marker_image)
        self.binary_reconstruct_by_select_marker_button.clicked.connect(self.draw_binary_reconstruct_image)
        self.binary_reconstruct_by_open_button.clicked.connect(self.draw_binary_open_reconstruct_image)
        self.gray_OBR_botton.clicked.connect(self.draw_gray_OBR_image)
        self.gray_CBR_button.clicked.connect(self.draw_gray_CBR_image)


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
            # self.binary_image_matrix = 255 * entropy_binary_gray_image(self.initial_image_matrix)
            # self.binary_image.setImage(self.binary_image_matrix)

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

    def draw_gray_dilation_image(self):
        self.gray_morphological_image_matrix=gray_morphology_dilation(self.initial_image_matrix,self.temp_struct)
        self.gray_morphological_image.setImage(self.gray_morphological_image_matrix)
    def draw_gray_erosion_image(self):
        self.gray_morphological_image_matrix = gray_morphology_erosion(self.initial_image_matrix, self.temp_struct)
        self.gray_morphological_image.setImage(self.gray_morphological_image_matrix)
    def draw_gray_opening_image(self):
        self.gray_morphological_image_matrix = gray_morphology_open(self.initial_image_matrix, self.temp_struct)
        self.gray_morphological_image.setImage(self.gray_morphological_image_matrix)
    def draw_gray_closing_image(self):
        self.gray_morphological_image_matrix = gray_morphology_close(self.initial_image_matrix, self.temp_struct)
        self.gray_morphological_image.setImage(self.gray_morphological_image_matrix)
    def draw_morphological_gradient_image(self):
        # dilation_binary_image = gray_morphology_dilation(self.initial_image_matrix,self.temp_struct)
        # erosion_binary_image= gray_morphology_erosion(self.initial_image_matrix,self.temp_struct)
        if self.gradient_type_box.currentIndex()==0:
            self.gray_morphological_image_matrix=morphological_gradient_subtract(gray_morphology_dilation(self.initial_image_matrix,self.temp_struct), gray_morphology_erosion(self.initial_image_matrix, self.temp_struct))

        else:
            if self.gradient_type_box.currentIndex()==1:
                self.gray_morphological_image_matrix = morphological_gradient_subtract(self.initial_image_matrix,
                gray_morphology_erosion(self.initial_image_matrix, self.temp_struct))

            else:
                self.gray_morphological_image_matrix = morphological_gradient_subtract(
                gray_morphology_dilation(self.initial_image_matrix, self.temp_struct),
                self.initial_image_matrix)
        self.gray_morphological_image.setImage(self.gray_morphological_image_matrix)
    def draw_morphological_edge_image(self):
        self.binary_image_matrix = 255 * entropy_binary_gray_image(self.initial_image_matrix)
        if self.edge_type_box.currentIndex()==0:
            self.gray_morphological_image_matrix=morphological_gradient_subtract(binary_morphology_dilation(self.binary_image_matrix,self.temp_struct), binary_morphology_erosion(self.binary_image_matrix, self.temp_struct))

        else:
            if self.edge_type_box.currentIndex()==1:
                self.gray_morphological_image_matrix=morphological_gradient_subtract(self.binary_image_matrix, binary_morphology_erosion(self.binary_image_matrix, self.temp_struct))


            else:
                self.gray_morphological_image_matrix=morphological_gradient_subtract(binary_morphology_dilation(self.binary_image_matrix,self.temp_struct), self.binary_image_matrix)

        self.gray_morphological_image.setImage(self.gray_morphological_image_matrix)
    def select_marker_image(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            imgPath = str(dialog.selectedFiles()[0])
            self.marker_image_class.loadImage(imgPath)
            self.marker_image_matrix = self.marker_image_class.getImage()
            self.marker_image_matrix=threshold_binary_gray_image(self.marker_image_matrix,100)
            self.marker_image.setImage(self.marker_image_matrix)
    def draw_binary_reconstruct_image(self):
        self.initial_image_matrix=threshold_binary_gray_image(self.initial_image_matrix,100)
        self.reconstruction_image_matrix=binary_morphology_dilation_reconstruct(self.initial_image_matrix,self.marker_image_matrix,self.temp_struct)
        self.reconstruction_image.setImage(self.reconstruction_image_matrix)
    def draw_binary_open_reconstruct_image(self):
        self.initial_image_matrix = threshold_binary_gray_image(self.initial_image_matrix, 100)
        self.marker_image_matrix=binary_morphology_open(self.initial_image_matrix,self.temp_struct)
        self.reconstruction_image_matrix=binary_morphology_dilation_reconstruct(self.initial_image_matrix,self.marker_image_matrix,self.temp_struct)
        self.marker_image.setImage(self.marker_image_matrix)
        self.reconstruction_image.setImage(self.reconstruction_image_matrix)
    def draw_gray_OBR_image(self):
        self.marker_image_matrix=gray_morphology_open(self.initial_image_matrix,self.temp_struct)
        self.reconstruction_image_matrix=morphological_OBR(self.initial_image_matrix,self.temp_struct)
        self.marker_image.setImage(self.marker_image_matrix)
        self.reconstruction_time = self.reconstruction_image_matrix.shape[2]
        self.timer = QTimer()
        self.timer.setInterval(20)
        self.timer.start()
        self.timer.timeout.connect(self.draw_gray_OBR_image_part)
    def draw_gray_OBR_image_part(self):
        temp_dim = self.reconstruction_image_matrix.shape[2] - self.reconstruction_time
        self.reconstruction_image.setImage(self.reconstruction_image_matrix[:, :, temp_dim])
        self.reconstruction_time -= 1
        if self.reconstruction_time == 0:
            if self.timer.isActive():
                self.timer.stop()
    def draw_gray_CBR_image(self):
        self.marker_image_matrix=gray_morphology_close(self.initial_image_matrix,self.temp_struct)
        self.reconstruction_image_matrix=morphological_CBR(self.initial_image_matrix,self.temp_struct)
        self.marker_image.setImage(self.marker_image_matrix)
        self.reconstruction_time = self.reconstruction_image_matrix.shape[2]
        self.timer = QTimer()
        self.timer.setInterval(20)
        self.timer.start()
        self.timer.timeout.connect(self.draw_gray_OBR_image_part)
    # def draw_gray_CBR_image_part(self):
    #     temp_dim = self.reconstruction_image_matrix.shape[2] - self.reconstruction_time
    #     self.reconstruction_image.setImage(self.reconstruction_image_matrix[:, :, temp_dim])
    #     self.reconstruction_time -= 1
    #     if self.reconstruction_time == 0:
    #         if self.timer.isActive():
    #             self.timer.stop()


    # def draw_binary_skeleton_reconstruction_image(self):
    #     self.skeletonreconstruction_image_matrix=binary_morphology_skeleton_reconstruct(self.skeletonreconstruction_image_matrix,self.temp_struct)
    #     self.max_skeleton_time = self.skeletonreconstruction_image_matrix.shape[2]
    #     self.timer = QTimer()
    #     self.timer.setInterval(200)
    #     self.timer.start()
    #     self.timer.timeout.connect(self.binary_skeleton_reconstruction)
    # def binary_skeleton_reconstruction(self):
    #     temp_dim = self.skeletonreconstruction_image_matrix.shape[2] - self.max_skeleton_time
    #     self.skeletonreconstruction_image.setImage(self.skeletonreconstruction_image_matrix[:, :, temp_dim])
    #     self.max_skeleton_time -= 1
    #     if self.max_skeleton_time == 0:
    #         if self.timer.isActive():
    #             self.timer.stop()




    def retranslateUi(self, project4):
        _translate = QtCore.QCoreApplication.translate
        project4.setWindowTitle(_translate("project4", "Form"))
        self.opening_button.setText(_translate("project4", "opening"))
        self.erosion_button.setText(_translate("project4", "erosion"))
        self.dilation_button.setText(_translate("project4", "dilation"))
        self.import_file.setText(_translate("project4", "import file"))
        self.name_label_1.setText(_translate("project4", "marker"))
        self.closing_button.setText(_translate("project4", "closing"))
        self.name_label_4.setText(_translate("project4", "initial image"))
        self.name_label_5.setText(_translate("project4", "gray morphological operation"))
        self.structuring_box.setItemText(0, _translate("project4", "Euclidean"))
        self.structuring_box.setItemText(1, _translate("project4", "city"))
        self.structuring_box.setItemText(2, _translate("project4", "chessboard"))
        self.binary_reconstruct_by_select_marker_button.setText(_translate("project4", "reconstruct"))
        self.select_SE.setText(_translate("project4", "select SE:"))
        self.SE_size.setText(_translate("project4", "SE size:"))
        self.name_label_2.setText(_translate("project4", "reconstruction"))
        self.edge_detect_label.setText(_translate("project4", "edge detect:"))
        self.edge_type_box.setItemText(0, _translate("project4", "standard"))
        self.edge_type_box.setItemText(1, _translate("project4", "internal"))
        self.edge_type_box.setItemText(2, _translate("project4", "external"))
        self.gradient_type_box.setItemText(0, _translate("project4", "standard"))
        self.gradient_type_box.setItemText(1, _translate("project4", "internal"))
        self.gradient_type_box.setItemText(2, _translate("project4", "external"))
        self.gradient_label.setText(_translate("project4", "gradient:"))
        self.binary_reconstruct_label.setText(_translate("project4", "bianry image reconstruction"))
        self.binary_select_marker_button.setText(_translate("project4", "select marker"))
        self.binary_reconstruct_by_open_button.setText(_translate("project4", "opening reconstruct"))
        self.gray_OBR_botton.setText(_translate("project4", "OBR"))
        self.gray_reconstruct_label.setText(_translate("project4", "gray scale reconstruction"))
        self.gray_CBR_button.setText(_translate("project4", "CBR"))

class MyMainForm(QMainWindow, Ui_project4):
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