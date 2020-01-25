import sys
import os

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication, QFile, QTextStream, QObject
from PyQt5.QtWidgets import QApplication, QDialog
from ui_app import Ui_app


class AppMain(QDialog, Ui_app):

    def __init__(self):
        super(QDialog, self).__init__()
        self.setupUi(self)
        self.show()


def main():
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app= QApplication(sys.argv)
    # 加载UI
    file = QFile("./dark.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    qss = stream.readAll()
    app.setStyleSheet(qss)
    # Ui
    mainwindow = AppMain()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

