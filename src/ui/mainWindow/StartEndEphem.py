from PyQt5 import QtCore
from PyQt5 import QtWidgets

from src.ui.commons.layout import set_hbox, set_lvbox
from src.ui.commons.widgets import get_qfont


class StartEndEphem(QtWidgets.QFrame):

    def __init__(self, parent=None):
        super(StartEndEphem, self).__init__(parent)
        self.init_widgets()
        self.config_widgets()

    def init_widgets(self):
        self.title = QtWidgets.QLabel("Observation Time", self)
        start_l = QtWidgets.QLabel("Start:", self)

        start_field = QtWidgets.QLabel("HH MM")

        end_l = QtWidgets.QLabel("End:", self)

        end_field = QtWidgets.QLabel("HH MM")

        self.setLayout(set_lvbox(set_hbox(self.title),
                                 set_hbox(start_l, start_field),
                                 set_hbox(end_l, end_field)))

    def config_widgets(self):
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setFont(get_qfont(True))

        self.setStyleSheet("background-color: rgb(50, 50, 50); border-radius: 10px; color: white;")