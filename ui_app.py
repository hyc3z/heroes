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
        self.listWidget_index = customedListWidget(app)
        self.listWidget_index.setObjectName("listWidget_index")
        self.gridLayout.addWidget(self.listWidget_index, 0, 0, 1, 1)

        self.retranslateUi(app)
        QtCore.QMetaObject.connectSlotsByName(app)

    def retranslateUi(self, app):
        _translate = QtCore.QCoreApplication.translate
        app.setWindowTitle(_translate("app", "Dialog"))
from customedListWidget import customedListWidget
