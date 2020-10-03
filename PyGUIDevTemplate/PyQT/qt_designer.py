# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_designer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1072, 684)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 40, 972, 561))
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_generate_random_signal = QtWidgets.QPushButton(self.widget)
        self.pushButton_generate_random_signal.setMinimumSize(QtCore.QSize(120, 60))
        self.pushButton_generate_random_signal.setObjectName("pushButton_generate_random_signal")
        self.horizontalLayout.addWidget(self.pushButton_generate_random_signal)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButton_open_file = QtWidgets.QPushButton(self.widget)
        self.pushButton_open_file.setMinimumSize(QtCore.QSize(120, 60))
        self.pushButton_open_file.setObjectName("pushButton_open_file")
        self.horizontalLayout_2.addWidget(self.pushButton_open_file)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.MplWidget = MplWidget(self.widget)
        self.MplWidget.setMinimumSize(QtCore.QSize(480, 320))
        self.MplWidget.setObjectName("MplWidget")
        self.gridLayout_2.addWidget(self.MplWidget, 1, 0, 1, 1)
        self.cv2Label = cv2Label(self.widget)
        self.cv2Label.setMinimumSize(QtCore.QSize(480, 320))
        self.cv2Label.setObjectName("cv2Label")
        self.gridLayout_2.addWidget(self.cv2Label, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.dialLabel = QtWidgets.QLabel(self.widget)
        self.dialLabel.setObjectName("dialLabel")
        self.gridLayout_3.addWidget(self.dialLabel, 2, 2, 1, 1)
        self.verticalLabel = QtWidgets.QLabel(self.widget)
        self.verticalLabel.setObjectName("verticalLabel")
        self.gridLayout_3.addWidget(self.verticalLabel, 1, 1, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.widget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_3.addWidget(self.horizontalSlider, 2, 1, 1, 1)
        self.verticalSlider = QtWidgets.QSlider(self.widget)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout_3.addWidget(self.verticalSlider, 0, 0, 3, 1)
        self.horizontalLabel = QtWidgets.QLabel(self.widget)
        self.horizontalLabel.setObjectName("horizontalLabel")
        self.gridLayout_3.addWidget(self.horizontalLabel, 0, 1, 1, 1)
        self.dial = QtWidgets.QDial(self.widget)
        self.dial.setObjectName("dial")
        self.gridLayout_3.addWidget(self.dial, 0, 2, 2, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 2)
        self.runProgress = QtWidgets.QPushButton(self.widget)
        self.runProgress.setObjectName("runProgress")
        self.gridLayout_5.addWidget(self.runProgress, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_5.addWidget(self.progressBar, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1072, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_generate_random_signal.setText(_translate("MainWindow", "Generate\n"
"Random\n"
"Signal"))
        self.pushButton_open_file.setText(_translate("MainWindow", "Open\n"
"File"))
        self.cv2Label.setText(_translate("MainWindow", "cv2label"))
        self.dialLabel.setText(_translate("MainWindow", "dialLabel"))
        self.verticalLabel.setText(_translate("MainWindow", "verticalLabel"))
        self.horizontalLabel.setText(_translate("MainWindow", "horizontalLabel"))
        self.runProgress.setText(_translate("MainWindow", "Run"))
from cv2label import cv2Label
from mplwidget import MplWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
