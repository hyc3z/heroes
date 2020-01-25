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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(app)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_search = QtWidgets.QLineEdit(app)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout.addWidget(self.lineEdit_search)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(app)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget_index = customedListWidget(self.page)
        self.listWidget_index.setObjectName("listWidget_index")
        self.gridLayout_2.addWidget(self.listWidget_index, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget_winrate = modifiedTableWidget(self.page_2)
        self.tableWidget_winrate.setObjectName("tableWidget_winrate")
        self.tableWidget_winrate.setColumnCount(0)
        self.tableWidget_winrate.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidget_winrate, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)

        self.retranslateUi(app)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(app)

    def retranslateUi(self, app):
        _translate = QtCore.QCoreApplication.translate
        app.setWindowTitle(_translate("app", "Dialog"))
        self.label.setText(_translate("app", "搜索"))
from customedListWidget import customedListWidget
from modifiedTableWidget import modifiedTableWidget
