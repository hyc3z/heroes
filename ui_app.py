# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_app.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_app(object):
    def setupUi(self, app):
        app.setObjectName("app")
        app.resize(570, 452)
        self.gridLayout = QtWidgets.QGridLayout(app)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(app)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_search = QtWidgets.QLineEdit(self.page)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout.addWidget(self.lineEdit_search)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.listWidget_index = customedListWidget(self.page)
        self.listWidget_index.setObjectName("listWidget_index")
        self.gridLayout_2.addWidget(self.listWidget_index, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget_winrate = modifiedTableWidget(self.page_2)
        self.tableWidget_winrate.setObjectName("tableWidget_winrate")
        self.tableWidget_winrate.setColumnCount(0)
        self.tableWidget_winrate.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidget_winrate, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_currentHero = QtWidgets.QLabel(self.page_2)
        self.label_currentHero.setObjectName("label_currentHero")
        self.horizontalLayout_2.addWidget(self.label_currentHero)
        self.pushButton_return = QtWidgets.QPushButton(self.page_2)
        self.pushButton_return.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_return.setObjectName("pushButton_return")
        self.horizontalLayout_2.addWidget(self.pushButton_return)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)

        self.retranslateUi(app)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(app)

    def retranslateUi(self, app):
        _translate = QtCore.QCoreApplication.translate
        app.setWindowTitle(_translate("app", "Dialog"))
        self.label.setText(_translate("app", "搜索"))
        self.label_currentHero.setText(_translate("app", "当前英雄"))
        self.pushButton_return.setText(_translate("app", "返回"))
from customedListWidget import customedListWidget
from modifiedTableWidget import modifiedTableWidget
