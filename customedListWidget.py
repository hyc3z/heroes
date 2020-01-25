from PyQt5.QtCore import QSize, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QListWidget, QListView, QListWidgetItem


class customedListWidget(QListWidget):

    def __init__(self, parent=None):
        super(QListWidget, self).__init__(parent)
        self.setViewMode(QListView.IconMode)
        self.setIconSize(QSize(200, 100))
        self.setSpacing(0)
        self.setResizeMode(QListWidget.Adjust)
        self.setMovement(QListWidget.Static)

    def add_item(self, filename_icon:str, description:str):
        imageItem = QListWidgetItem()
        imageItem.setIcon(QIcon(filename_icon))
        imageItem.setText(description)
        imageItem.setSizeHint(QSize(100, 120))
        self.addItem(imageItem)
