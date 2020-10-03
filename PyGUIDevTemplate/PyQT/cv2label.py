# ------------------------------------------------------
# -------------------- mplwidget.py --------------------
# ------------------------------------------------------
import append_run_path

from PyQt5.QtWidgets import*
from PyQt5 import QtGui

import cv2
import numpy as np
    
class cv2Label(QLabel):
    """defined in Qt Designer"""
    
    def __init__(self, parent = None):
        QLabel.__init__(self, parent)


    def init(self):

        ## set init image on cv2Label
        rgb_color=(255, 255, 255)
        cvimg = np.zeros((self.height(), self.width(), 3), np.uint8)
        color = tuple(reversed(rgb_color))
        cvimg[:] = color
        pixmap = self.cv2pixmap(cvimg)
        self.setPixmap(pixmap)


    def set_img(self, path):

        try:
            cvimg = cv2.imread(path)
            pixmap = self.cv2pixmap(cvimg)
            ## set pixmap on cv2Label
            self.setPixmap(pixmap)
        except Exception as e:
            print(str(e))


    def cv2pixmap(self, cvimg):
            
        # image resize
        try:
            cvimg = cv2.resize(cvimg, 
                                dsize=(self.width(), self.height()), 
                                interpolation=cv2.INTER_AREA)

        except Exception as e:
            print(str(e))
            rgb_color=(0, 0, 0)
            cvimg = np.zeros( ( self.height(), self.width(), 3), np.uint8 )
            color = tuple(reversed(rgb_color))
            cvimg[:] = color
        
        # convert from cv image to qt image
        height, width, channel = cvimg.shape
        bytesPerLine = 3 * width
        qtimg = QtGui.QImage(cvimg.data, 
                            width, 
                            height, 
                            bytesPerLine, 
                            QtGui.QImage.Format_RGB888).rgbSwapped()

        return QtGui.QPixmap.fromImage(qtimg) # return pixmap