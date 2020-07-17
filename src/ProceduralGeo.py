import sys
from PySide2 import QtWidgets
from PySide2.QtCore import Qt


class SliderBox(QtWidgets.QAbstractSlider):
    """"""

    def __init__(self, parent=None):
        """Constructor"""
        super(SliderBox, self).__init__(parent)
        self.setWindowTitle("Sliders Example")
        self.create_widgets()
        self.create_layout()
        self.create_connections()
        self.slider_value()

    def create_widgets(self):
        self.ext_lbl = QtWidgets.QLabel()
        self.sld_lbl_01 = QtWidgets.QLabel()
        self.sld_lbl_02 = QtWidgets.QLabel()
        self.ext_sld_01 = QtWidgets.QSlider()
        self.ext_sld_02 = QtWidgets.QSlider()
        self.ext_sld_01.setOrientation(Qt.Horizontal)
        self.ext_sld_02.setOrientation(Qt.Horizontal)
        self.ext_sld_01.setMaximum(100)
        self.ext_sld_02.setMaximum(100)

    def create_layout(self):
        self.lay = QtWidgets.QFormLayout()
        self.lay.addRow(self.tr("&Height:"), self.sld_lbl_01)
        self.lay.addRow(self.ext_sld_01)
        self.lay.addRow(self.tr("&Width:"), self.sld_lbl_02)
        self.lay.addRow(self.ext_sld_02)
        self.setLayout(self.lay)

    def create_connections(self):
        #self.ext_cmb.currentIndexChanged.connect(self._update_ext_lbl)
        self.ext_sld_01.valueChanged.connect(self.sld_lbl_01.setNum)
        self.ext_sld_02.valueChanged.connect(self.sld_lbl_02.setNum)

    #def _update_ext_lbl(self):
        #self.ext_lbl.setText(self.ext_cmb.currentText())

    def slider_value(self):
        slider_val_01 = self.ext_sld_01.value()
        return slider_val_01
