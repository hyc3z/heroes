from PyQt5.QtWidgets import QListWidget


class customedListWidget(QListWidget):

    def __init__(self, parent=None):
        super(QListWidget, self).__init__(parent)
