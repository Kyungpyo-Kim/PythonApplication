import append_run_path

from PyQt5.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure

import sys
import numpy as np
import random

from PyQt5.QtWidgets import QApplication
app = QApplication(sys.argv)
screen = app.screens()[0]
dpi = screen.physicalDotsPerInch()
del app, screen
    
class MplWidget(QWidget):
    """defined in Qt Designer"""

    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure(figsize=(self.width()/dpi, self.height()/dpi)))
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