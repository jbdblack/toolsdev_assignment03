import sys
import pymel.core as pmc
import maya.cmds as cmds
import random as rand

import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance

from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Qt


def maya_main_window():
    """Return the maya main window widget"""
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window), QtWidgets.QWidget)


class SliderBox(QtWidgets.QAbstractSlider):
    """"""

    def __init__(self):
        """Constructor"""
        super(SliderBox, self).__init__()
        self.setWindowTitle("Sliders Example")
        self.resize(800, 300)
        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)
        self.create_widgets()
        self.create_layout()
        self.create_connections()
        self.slider_value()
        self.createbricks()

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

        self.brick_btn = QtWidgets.QPushButton("Create Bricks")

    def create_layout(self):
        """Lay out our widgets in the UI"""
        self.sliders_lay = QtWidgets.QFormLayout()
        self.sliders_lay.addRow(self.tr("&Height:"), self.sld_lbl_01)
        self.sliders_lay.addRow(self.ext_sld_01)
        self.sliders_lay.addRow(self.tr("&Width:"), self.sld_lbl_02)
        self.sliders_lay.addRow(self.ext_sld_02)

        self.bottom_btn_lay = QtWidgets.QHBoxLayout()
        self.bottom_btn_lay.addWidget(self.brick_btn)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.sliders_lay)
        self.main_layout.addLayout(self.bottom_btn_lay)
        self.setLayout(self.main_layout)


    def create_connections(self):
        """Connect our widget signal to slots"""
        self.ext_sld_01.valueChanged.connect(self.sld_lbl_01.setNum)
        self.ext_sld_02.valueChanged.connect(self.sld_lbl_02.setNum)
        self.brick_btn.clicked.connect(self.createbricks)


    def slider_value(self):
        slider_val_01 = self.ext_sld_01.value()
        return slider_val_01

    @QtCore.Slot()
    def createbricks(self):

        offx = 0.0
        offy = 0.0
        offz = 0.0
        row = int(self.ext_sld_01.value())
        col = int(self.ext_sld_02.value())
        bevel = float(1)
        width = float(2)
        height = float(2)
        depth = float(2)
        offset = float(2)

        for i in range(0,row):
            for j in range(0,col):
                pmc.polyCube(sz=1, sy=1, sx=1, d=depth, h=height, n="brick 01", w=width, ax=(0, 1, 0))
                pmc.polyBevel(offsetAsFraction=1, segments=2, autoFit=1, angleTolerance=180, mergeVertexTolerance=0.0001,
                          worldSpace=1, smoothingAngle=30, offset=bevel, mergeVertices=1, uvAssignment=1,
                          miteringAngle=180, fillNgons=1)
                # extracting bounding box of the cube
                minX = float(pmc.getAttr(".boundingBoxMinX"))
                minY = float(pmc.getAttr(".boundingBoxMinY"))
                minZ = float(pmc.getAttr(".boundingBoxMinZ"))
                maxX = float(pmc.getAttr(".boundingBoxMaxX"))
                maxY = float(pmc.getAttr(".boundingBoxMaxY"))
                maxZ = float(pmc.getAttr(".boundingBoxMaxZ"))
                off = (maxX - minX) / 2
                if i % 2 == 0:
                    offx = (maxX - minX) * j
                    offy = (maxY - minY) * i
                    cmds.move(offx, offy, 0, r=1)

                else:
                    offx = ((maxX - minX) * j) + off
                    offy = (maxY - minY) * i
                    cmds.move(offx, offy, 0, r=1)

                #offz = float(rand(0, .2))
                cmds.move(0, 0, offz, r=1)