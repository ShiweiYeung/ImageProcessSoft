# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import  sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, \
        QHBoxLayout, QVBoxLayout, QSizePolicy, \
        QFileDialog

from PyQt5 import QtCore, QtGui, QtWidgets
from image_viewer_widget import imageViewerWidget
from basic_image import basicImage
from binary_and_hist import *
from image_convolution import *

class Ui_project2(QWidget):
    def setupUi(self, project2):
        project2.setObjectName("project2")
        project2.resize(1065, 849)

        self.initial_image_matrix = np.zeros([1, 1])
        self.initial_image_class = basicImage()

        project2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.sobel_button = QtWidgets.QPushButton(project2)
        self.sobel_button.setGeometry(QtCore.QRect(70, 210, 71, 31))
        self.sobel_button.setObjectName("sobel_button")
        self.prewitt_button = QtWidgets.QPushButton(project2)
        self.prewitt_button.setGeometry(QtCore.QRect(70, 160, 71, 31))
        self.prewitt_button.setObjectName("prewitt_button")
        self.roberts_button = QtWidgets.QPushButton(project2)
        self.roberts_button.setGeometry(QtCore.QRect(70, 110, 71, 31))
        self.roberts_button.setObjectName("roberts_button")
        self.import_file = QtWidgets.QPushButton(project2)
        self.import_file.setGeometry(QtCore.QRect(70, 60, 141, 31))
        self.import_file.setObjectName("import_file")
        self.initial_image = imageViewerWidget(project2)
        self.initial_image.setGeometry(QtCore.QRect(290, 30, 700, 700))
        self.initial_image.setText("")
        self.initial_image.setScaledContents(True)
        self.initial_image.setObjectName("initial_image")
        self.gaussian_kernal_size = QtWidgets.QSpinBox(project2)
        self.gaussian_kernal_size.setGeometry(QtCore.QRect(70, 260, 71, 31))
        self.gaussian_kernal_size.setObjectName("gaussian_kernal_size")
        self.gaussian_kernal_size.setMinimum(1)
        self.gaussian_kernal_size.setMaximum(10)
        self.gaussian_kernal_var = QtWidgets.QSpinBox(project2)
        self.gaussian_kernal_var.setGeometry(QtCore.QRect(150, 260, 71, 31))
        self.gaussian_kernal_var.setObjectName("gaussian_kernal_var")
        self.gaussian_kernal_var.setMinimum(1)
        self.gaussian_kernal_var.setMaximum(10)
        self.gaussian_button = QtWidgets.QPushButton(project2)
        self.gaussian_button.setGeometry(QtCore.QRect(70, 310, 141, 31))
        self.gaussian_button.setObjectName("gaussian_button")
        self.median_kernal_size = QtWidgets.QSpinBox(project2)
        self.median_kernal_size.setGeometry(QtCore.QRect(100, 360, 71, 31))
        self.median_kernal_size.setObjectName("median_kernal_size")
        self.median_kernal_size.setMinimum(1)
        self.median_kernal_size.setMaximum(10)
        self.median_button = QtWidgets.QPushButton(project2)
        self.median_button.setGeometry(QtCore.QRect(70, 410, 141, 31))
        self.median_button.setObjectName("median_button")
        self.gridLayoutWidget = QtWidgets.QWidget(project2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 460, 171, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.filter_6 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.filter_6.setObjectName("filter_6")
        self.filter_6.setMinimum(-5)
        self.filter_6.setMaximum(5)
        self.gridLayout.addWidget(self.filter_6, 1, 2, 1, 1)
        self.filter_5 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.filter_5.setObjectName("filter_5")
        self.filter_5.setMinimum(-5)
        self.filter_5.setMaximum(5)
        self.gridLayout.addWidget(self.filter_5, 1, 1, 1, 1)
        self.filter_4 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.filter_4.setObjectName("filter_4")
        self.filter_4.setMinimum(-5)
        self.filter_4.setMaximum(5)
        self.gridLayout.addWidget(self.filter_4, 1, 0, 1, 1)
        self.filter_1 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.filter_1.setObjectName("filter_1")
        self.filter_1.setMinimum(-5)
        self.filter_1.setMaximum(5)
        self.gridLayout.addWidget(self.filter_1, 0, 0, 1, 1)
        self.filter_3 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.filter_3.setObjectName("filter_3")
        self.filter_3.setMinimum(-5)
        self.filter_3.setMaximum(5)
        self.gridLayout.addWidget(self.filter_3, 0, 2, 1, 1)
        self.filter_2 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.filter_2.setObjectName("filter_2")
        self.filter_2.setMinimum(-5)
        self.filter_2.setMaximum(5)
        self.gridLayout.addWidget(self.filter_2, 0, 1, 1, 1)
        self.filter_7 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.filter_7.setObjectName("filter_7")
        self.filter_7.setMinimum(-5)
        self.filter_7.setMaximum(5)
        self.gridLayout.addWidget(self.filter_7, 2, 0, 1, 1)
        self.filter_8 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.filter_8.setObjectName("filter_8")
        self.filter_8.setMinimum(-5)
        self.filter_8.setMaximum(5)
        self.gridLayout.addWidget(self.filter_8, 2, 1, 1, 1)
        self.filter_9 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.filter_9.setObjectName("filter_9")
        self.filter_9.setMinimum(-5)
        self.filter_9.setMaximum(5)
        self.gridLayout.addWidget(self.filter_9, 2, 2, 1, 1)
        self.filter_button = QtWidgets.QPushButton(project2)
        self.filter_button.setGeometry(QtCore.QRect(70, 610, 141, 31))
        self.filter_button.setObjectName("filter_button")

        self.layoutWidget = QtWidgets.QWidget(project2)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 160, 71, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.prewitt_y = QtWidgets.QRadioButton(self.layoutWidget)
        self.prewitt_y.setObjectName("prewitt_y")
        self.horizontalLayout_2.addWidget(self.prewitt_y)
        self.prewitt_x = QtWidgets.QRadioButton(self.layoutWidget)
        self.prewitt_x.setObjectName("prewitt_x")
        self.horizontalLayout_2.addWidget(self.prewitt_x)
        self.layoutWidget_2 = QtWidgets.QWidget(project2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(150, 210, 71, 31))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sobel_y = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.sobel_y.setObjectName("sobel_y")
        self.horizontalLayout_3.addWidget(self.sobel_y)
        self.sobel_x = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.sobel_x.setObjectName("sobel_x")
        self.horizontalLayout_3.addWidget(self.sobel_x)
        self.edge_pice_scrollbar = QtWidgets.QScrollBar(project2)
        self.edge_pice_scrollbar.setGeometry(QtCore.QRect(50, 670, 171, 21))
        self.edge_pice_scrollbar.setMaximum(255)
        self.edge_pice_scrollbar.setSingleStep(1)
        self.edge_pice_scrollbar.setOrientation(QtCore.Qt.Horizontal)

        self.edge_pice_scrollbar.setObjectName("edge_pice_scrollbar")

        self.edge_pice_scrollbar.setVisible(False)
        self.label = QtWidgets.QLabel(project2)
        self.label.setGeometry(QtCore.QRect(80, 710, 121, 21))
        self.label.setObjectName("label")
        self.label.setVisible(False)
        self.widget = QtWidgets.QWidget(project2)
        self.widget.setGeometry(QtCore.QRect(150, 110, 71, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.robert_y = QtWidgets.QRadioButton(self.widget)
        self.robert_y.setObjectName("robert_y")
        self.horizontalLayout.addWidget(self.robert_y)
        self.robert_x = QtWidgets.QRadioButton(self.widget)
        self.robert_x.setObjectName("robert_x")
        self.horizontalLayout.addWidget(self.robert_x)


        self.retranslateUi(project2)
        QtCore.QMetaObject.connectSlotsByName(project2)

        self.import_file.clicked.connect(self.actLoadImage)
        self.roberts_button.clicked.connect(self.draw_roberts_filter_image)
        self.prewitt_button.clicked.connect(self.draw_prewitt_filter_image)
        self.sobel_button.clicked.connect(self.draw_sobel_filter_image)
        self.gaussian_button.clicked.connect(self.draw_gaussian_filter_image)
        self.median_button.clicked.connect(self.draw_median_filter_image)
        self.filter_button.clicked.connect(self.draw_randow_filter_image)
        self.edge_pice_scrollbar.valueChanged.connect(self.draw_convolution_edge_image)




    def retranslateUi(self, project2):
        _translate = QtCore.QCoreApplication.translate
        project2.setWindowTitle(_translate("project2", "Form"))
        self.sobel_button.setText(_translate("project2", "Sobel"))
        self.prewitt_button.setText(_translate("project2", "Prewitt"))
        self.roberts_button.setText(_translate("project2", "Roberts"))
        self.import_file.setText(_translate("project2", "import file"))
        self.gaussian_button.setText(_translate("project2", "Gaussian"))
        self.median_button.setText(_translate("project2", "Median"))
        self.filter_button.setText(_translate("project2", "filter"))

        self.prewitt_y.setText(_translate("project2", "y"))
        self.prewitt_x.setText(_translate("project2", "x"))
        self.sobel_y.setText(_translate("project2", "y"))
        self.sobel_x.setText(_translate("project2", "x"))
        self.label.setText(_translate("project2", "edge detection"))
        self.robert_y.setText(_translate("project2", "y"))
        self.robert_x.setText(_translate("project2", "x"))

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
    def draw_roberts_filter_image(self):
        if self.robert_x.isChecked():
            roberts_operator = np.array([[-1, 0], [0, 1]])
        else:
            roberts_operator = np.array([[0, -1], [1, 0]])
        self.initial_image_matrix = self.initial_image_class.getImage()
        self.initial_image_matrix=Image_Convolution(self.initial_image_matrix, roberts_operator)
        self.initial_image.setImage(self.initial_image_matrix.astype(np.uint8))
    def draw_prewitt_filter_image(self):
        if self.prewitt_x.isChecked():
            prewitt_operator=np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
        else:
            prewitt_operator=np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        self.initial_image_matrix = self.initial_image_class.getImage()
        self.initial_image_matrix=Image_Convolution(self.initial_image_matrix, prewitt_operator)
        self.initial_image.setImage(self.initial_image_matrix.astype(np.uint8))
    def draw_sobel_filter_image(self):
        if self.sobel_x.isChecked():
            sobel_operator=np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        else:
            sobel_operator=np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        self.initial_image_matrix = self.initial_image_class.getImage()
        self.initial_image_matrix=Image_Convolution(self.initial_image_matrix, sobel_operator)
        self.initial_image.setImage(self.initial_image_matrix.astype(np.uint8))
    def draw_gaussian_filter_image(self):
        self.initial_image_matrix = self.initial_image_class.getImage()
        gauss_kernal=gauss_filter(self.gaussian_kernal_size.value(),self.gaussian_kernal_var.value())
        self.initial_image_matrix = Image_Convolution(self.initial_image_matrix, gauss_kernal)
        self.initial_image.setImage(self.initial_image_matrix.astype(np.uint8))
    def draw_median_filter_image(self):
        self.initial_image_matrix = self.initial_image_class.getImage()
        # median_kernal=median_filter(self.median_kernal_size.value())
        # self.initial_image_matrix = Image_Convolution(self.initial_image_matrix, median_kernal)
        self.initial_image_matrix = ture_median_filter(self.initial_image_matrix,self.median_kernal_size.value())
        self.initial_image.setImage(self.initial_image_matrix.astype(np.uint8))
    def draw_randow_filter_image(self):
        self.initial_image_matrix = self.initial_image_class.getImage()
        kernal=np.zeros([3,3])
        kernal[0,0] = self.filter_1.value()
        kernal[0,1] = self.filter_2.value()
        kernal[0,2] = self.filter_3.value()
        kernal[1,0] = self.filter_4.value()
        kernal[1,1] = self.filter_5.value()
        kernal[1,2] = self.filter_6.value()
        kernal[2,0] = self.filter_7.value()
        kernal[2,1] = self.filter_8.value()
        kernal[2,2] = self.filter_9.value()
        self.initial_image_matrix = Image_Convolution(self.initial_image_matrix, kernal)
        self.initial_image.setImage(self.initial_image_matrix.astype(np.uint8))
    def draw_convolution_edge_image(self):
        threshold=self.edge_pice_scrollbar.value()
        self.edge_image_matrix=threshold_binary_gray_image(self.initial_image_matrix,threshold)
        self.initial_image.setImage(self.edge_image_matrix.astype(np.uint8))


class MyMainForm(QMainWindow, Ui_project2):
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