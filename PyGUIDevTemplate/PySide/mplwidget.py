

from PySide2.QtWidgets import QWidget, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure

import numpy as np
import random

# from PySide2 import QtGui
# import sys
# app = QtGui.QApplication(sys.argv)
# screen_rect = app.desktop().screenGeometry()
# width, height = screen_rect.width(), screen_rect.height()

class MplWidget(QWidget):
    """defined in Qt Designer"""

    def __init__(self, parent=None):
        
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())
        # self.canvas = FigureCanvas(Figure())
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

    def update_graph(self):
        fs = 500
        f = random.randint(1, 100)
        ts = 1/fs
        length_of_signal = 100
        t = np.linspace(0,1,length_of_signal)
        
        cosinus_signal = np.cos(2*np.pi*f*t)
        sinus_signal = np.sin(2*np.pi*f*t)

        self.canvas.axes.clear()
        self.canvas.axes.plot(t, cosinus_signal)
        self.canvas.axes.plot(t, sinus_signal)
        self.canvas.axes.legend(('cosinus', 'sinus'),
                                            loc='upper right')
        self.canvas.axes.set_title('Cosinus - Sinus Signal')

        ## update matplotlib plot
        self.canvas.draw()