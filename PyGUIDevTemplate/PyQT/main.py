# ------------------------------------------------------
# ---------------------- main.py -----------------------
# ------------------------------------------------------
import time

import append_run_path
import mplwidget
import cv2label

from PyQt5.QtWidgets import*
# from PyQt5.uic import loadUi # for dev version
import qt_designer # for dist version

from PyQt5 import QtGui
from PyQt5 import QtCore

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

PROGRESS_LIMIT = 100

# class PyQtDevTemplateWidget(QMainWindow): # for dev version
class PyQtDevTemplateWidget(qt_designer.Ui_MainWindow, QMainWindow): # for dist version
    
    def __init__(self):
        
        QMainWindow.__init__(self)
        
        # loadUi("qt_designer.ui",self) # for dev version
        self.setupUi(self) # for dist version

        ## set ui title
        self.setWindowTitle("PyQt5 & Matplotlib & OpenCV Example GUI")

        ##  set event handller for button
        self.pushButton_generate_random_signal.clicked.connect(self.update_graph)
        self.pushButton_open_file.clicked.connect(self.open_img)
        self.runProgress.clicked.connect(self.run_progress)

        ## set event handler for slider
        self.verticalSlider.sliderMoved.connect(self.verticalSlider_change)
        self.verticalSlider.valueChanged.connect(self.verticalSlider_change)
        self.horizontalSlider.sliderMoved.connect(self.horizontalSlider_change)
        self.horizontalSlider.valueChanged.connect(self.horizontalSlider_change)
        self.dial.sliderMoved.connect(self.dial_change)
        self.dial.valueChanged.connect(self.dial_change)

        ## set matplotlib toolbar
        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))
       
        ## set progress bar to zero
        self.progressBar.setValue(0)

        ## all input controller
        self.allInput = []
        self.allInput.append(self.pushButton_generate_random_signal)
        self.allInput.append(self.pushButton_open_file)
        self.allInput.append(self.runProgress)
        self.allInput.append(self.verticalSlider)
        self.allInput.append(self.horizontalSlider)
        self.allInput.append(self.dial)

        ## initialization of cv2Label image
        self.cv2Label.init()


    def update_graph(self):
        self.MplWidget.update_graph()


    def open_img(self):
        fname = QFileDialog.getOpenFileName(self)
        print( fname[0] )

        self.cv2Label.set_img(fname[0])

    
    def run_progress(self):
        ## disable all input
        self.setEnabled(False)
        
        count = 0
        while count < PROGRESS_LIMIT:
            count += 1
            time.sleep(0.1)
            self.progressBar.setValue(count)

        ## enable all input
        self.setEnabled(True)


    def verticalSlider_change(self):
        self.verticalLabel.setText(str(self.verticalSlider.value()))


    def horizontalSlider_change(self):
        self.horizontalLabel.setText(str(self.horizontalSlider.value()))


    def dial_change(self):
        self.dialLabel.setText(str(self.dial.value()))


    def setEnabled(self, en):
        for i in self.allInput:
            i.setEnabled(en)


if __name__ == "__main__":
    app = QApplication([])
    window = PyQtDevTemplateWidget()
    window.show()
    app.exec_()