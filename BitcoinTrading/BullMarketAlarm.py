import sys
import os
from PySide2 import QtUiTools, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide2.QtCore import QTimer, QThread, Signal, Slot

import pybithumb

tickers = ["BTC", "ETH", "BCH", "ETC"]


class Worker(QThread):
    finished = Signal(dict)

    def run(self):
        while True:
            print("Update information...")
            data = {}
            for i, ticker in enumerate(tickers):

                data[ticker] = self.get_market_infos(ticker)

            self.finished.emit(data)
            self.msleep(500)
            print("Updated!")

    def get_market_infos(self, ticker):
        df = pybithumb.get_ohlcv(ticker)
        ma5 = df['close'].rolling(window=5).mean()
        last_ma5 = ma5[-2]
        price = pybithumb.get_current_price(ticker)

        state = None
        if price > last_ma5:
            state = "상승장"
        else:
            state = "하락장"

        return price, last_ma5, state


class MainView(QMainWindow):
    def __init__(self):

        # set UI
        super().__init__()
        self.setupUI()

        UI_set.tableWidget.setRowCount(len(tickers))
        self.worker = Worker()
        self.worker.finished.connect(self.update_table_widget)
        self.worker.start()

    def setupUI(self):
        global UI_set
        UI_set = QtUiTools.QUiLoader().load(resource_path("./BullMarketAlarm.ui"))
        self.setCentralWidget(UI_set)
        self.setWindowTitle("Bull Market Alarm")
        self.show()

    @Slot(dict)
    def update_table_widget(self, data):
        try:
            for ticker, infos in data.items():
                index = tickers.index(ticker)
                UI_set.tableWidget.setItem(index, 0, QTableWidgetItem(ticker))
                UI_set.tableWidget.setItem(
                    index, 1, QTableWidgetItem(str(infos[0])))
                UI_set.tableWidget.setItem(
                    index, 2, QTableWidgetItem(str(infos[1])))
                UI_set.tableWidget.setItem(
                    index, 3, QTableWidgetItem(infos[2]))
        except:
            pass


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        return os.path.join(os.path.abspath("."), relative_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainView()
    sys.exit(app.exec_())
