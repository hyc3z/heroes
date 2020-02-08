import sys
import os

from PyQt5.QtGui import QBrush, QColor

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication, QFile, QTextStream, QObject
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from ui_app import Ui_app
from get_hero import *


class AppMain(QDialog, Ui_app):

    def __init__(self):
        super(QDialog, self).__init__()
        self.hero_dict = get_heroes_icons_local()
        self.translation = get_trans_dict()
        self.setupUi(self)
        self.show_heroes(self.hero_dict)
        self.listWidget_index.itemClicked.connect(self.show_detail)
        self.lineEdit_search.textChanged.connect(self.search)
        self.pushButton_return.clicked.connect(self.return_index)
        self.stackedWidget.setCurrentIndex(0)
        self.init_table()
        self.setWindowTitle("Dota helper v0.1")
        self.show()

    def init_table(self):
        table = self.tableWidget_winrate
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(['英雄', '克制指数', '胜率', '盘数'])

    def return_index(self):
        self.stackedWidget.setCurrentIndex(0)

    def show_table(self, data:dict):
        table = self.tableWidget_winrate
        table.clearContents()
        table.setRowCount(len(data))
        rowcount = 0
        for i in data:
            item0 = QTableWidgetItem(self.translation[i[0]])

            item0.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item0.setForeground(QBrush(QColor(204, 120, 50)))
            table.setItem(rowcount, 0, item0)
            item1 = QTableWidgetItem()
            item1.setData(QtCore.Qt.DisplayRole, float(i[1][1]))
            item1.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item1.setForeground(QBrush(QColor(85, 150, 186)))
            table.setItem(rowcount, 1, item1)
            item2 = QTableWidgetItem()
            item2.setData(QtCore.Qt.DisplayRole, float(i[1][2]))
            item2.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item2.setForeground(QBrush(QColor(106, 135, 89)))
            table.setItem(rowcount, 2, item2)
            item3 = QTableWidgetItem()
            item3.setData(QtCore.Qt.DisplayRole, float(i[1][0]))
            item3.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item3.setForeground(QBrush(QColor(106, 135, 89)))
            table.setItem(rowcount, 3, item3)
            rowcount += 1

    def show_heroes(self, hero_dict):
        self.listWidget_index.clear()
        for hero in hero_dict:
            self.listWidget_index.add_item(hero_dict[hero], hero)

    def search(self):
        keyword = self.lineEdit_search.text()
        if len(keyword) == 0:
            self.show_heroes(self.hero_dict)
        else:
            result = {}
            for i in self.hero_dict.keys():
                if keyword in i or keyword in self.translation[i]:
                    result[i] = self.hero_dict[i]
            self.show_heroes(result)

    def show_detail(self):
        sender = self.sender().currentItem()
        hero_name = sender.text()
        hero_name_english = self.translation[hero_name]
        winrate = get_hero_matchups_data_local_precise(hero_name_english)
        self.show_table(winrate)
        self.label_currentHero.setText("当前英雄：{}".format(hero_name))
        self.stackedWidget.setCurrentIndex(1)


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

