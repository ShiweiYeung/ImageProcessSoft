import os,sys

from PyQt5.QtWidgets import QGridLayout, \
        QDesktopWidget, QMainWindow, QApplication, qApp, \
        QDockWidget, QWidget, QAction, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSlot, QPoint

from project1_ui import Ui_project1
from project2_ui import Ui_project2
from project3_ui import Ui_project3
from project4_ui import Ui_project4


class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()

        self.project1 = Ui_project1()
        self.dockProject1 = QDockWidget("Project 1", self)
        self.dockProject1.setObjectName("dock Project 1")
        self.addDockWidget(Qt.RightDockWidgetArea, self.dockProject1)
        self.dockProject1.setWidget(self.project1)
        self.project2 = Ui_project2()
        self.dockProject2 = QDockWidget("Project 2", self)
        self.dockProject2.setObjectName("dock Project 2")
        self.addDockWidget(Qt.RightDockWidgetArea, self.dockProject2)
        self.dockProject2.setWidget(self.project2)
        self.project3 = Ui_project3()
        self.dockProject3 = QDockWidget("Project 3", self)
        self.dockProject3.setObjectName("dock Project 3")
        self.addDockWidget(Qt.RightDockWidgetArea, self.dockProject3)
        self.dockProject3.setWidget(self.project3)
        self.project4 = Ui_project4()
        self.dockProject4 = QDockWidget("Project 4", self)
        self.dockProject4.setObjectName("dock Project 4")
        self.addDockWidget(Qt.RightDockWidgetArea, self.dockProject4)
        self.dockProject4.setWidget(self.project4)
        self.tabifyDockWidget(self.dockProject1, self.dockProject2)
        self.tabifyDockWidget(self.dockProject2, self.dockProject3)
        self.tabifyDockWidget(self.dockProject3, self.dockProject4)
        self.project1.setupUi(self.project1)
        self.project2.setupUi(self.project2)
        self.project3.setupUi(self.project3)
        self.project4.setupUi(self.project4)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    QApplication.setStyle("fusion")
    mainWindow = mainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

