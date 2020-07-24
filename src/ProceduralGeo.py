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


class SliderBox(QtWidgets.QDialog): #Change from QAbstractSlider to something else (QtWidgets.QDialog)
    """"""

    def __init__(self):
        """Constructor"""
        super(SliderBox, self).__init__(parent=maya_main_window())
        self.setWindowTitle("Brick Wall Generator")
        self.resize(800, 300)
        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)
        self.create_widgets()
        self.create_layout()
        self.create_connections()
        self.slider_value()
        self.createbricks()

    def create_widgets(self):
        """Creates widgets for our UI"""
        self.sld_lbl_row = QtWidgets.QLabel()
        self.sld_lbl_col = QtWidgets.QLabel()
        self.sld_lbl_bvl = QtWidgets.QLabel()
        self.sld_lbl_offset = QtWidgets.QLabel()
        self.sld_lbl_width = QtWidgets.QLabel()
        self.sld_lbl_height = QtWidgets.QLabel()
        self.sld_lbl_depth = QtWidgets.QLabel()

        self.ext_sld_row = QtWidgets.QSlider()
        self.ext_sld_col = QtWidgets.QSlider()
        self.ext_sld_bvl = QtWidgets.QSlider()
        self.ext_sld_offset = QtWidgets.QSlider()
        self.ext_sld_width = QtWidgets.QSlider()
        self.ext_sld_height = QtWidgets.QSlider()
        self.ext_sld_depth = QtWidgets.QSlider()

        self.ext_sld_row.setOrientation(Qt.Horizontal)
        self.ext_sld_col.setOrientation(Qt.Horizontal)
        self.ext_sld_bvl.setOrientation(Qt.Horizontal)
        self.ext_sld_offset.setOrientation(Qt.Horizontal)
        self.ext_sld_width.setOrientation(Qt.Horizontal)
        self.ext_sld_height.setOrientation(Qt.Horizontal)
        self.ext_sld_depth.setOrientation(Qt.Horizontal)

        self.ext_sld_row.setMaximum(250)
        self.ext_sld_col.setMaximum(250)
        self.ext_sld_bvl.setMaximum(1)
        self.ext_sld_offset.setMaximum(0.4)
        self.ext_sld_width.setMaximum(20)
        self.ext_sld_width.setValue(2)
        self.ext_sld_height.setMaximum(20)
        self.ext_sld_height.setValue(1)
        self.ext_sld_depth.setMaximum(20)

        self.brick_btn = QtWidgets.QPushButton("Create Bricks")

    def create_layout(self):
        """Lay out our widgets in the UI"""
        self.sliders_lay = QtWidgets.QFormLayout()
        self.sliders_lay.addRow(self.tr("&Wall Rows:"), self.sld_lbl_row)
        self.sliders_lay.addRow(self.ext_sld_row)
        self.sliders_lay.addRow(self.tr("&Wall Columns:"), self.sld_lbl_col)
        self.sliders_lay.addRow(self.ext_sld_col)

        self.sliders_lay.addRow(self.tr("&Brick Bevel:"), self.sld_lbl_bvl)
        self.sliders_lay.addRow(self.ext_sld_bvl)

        self.sliders_lay.addRow(self.tr("&Brick Offset:"), self.sld_lbl_offset)
        self.sliders_lay.addRow(self.ext_sld_offset)

        self.sliders_lay.addRow(self.tr("&Brick Width:"), self.sld_lbl_width)
        self.sliders_lay.addRow(self.ext_sld_width)

        self.sliders_lay.addRow(self.tr("&Brick Height:"), self.sld_lbl_height)
        self.sliders_lay.addRow(self.ext_sld_height)

        self.sliders_lay.addRow(self.tr("&Brick Depth:"), self.sld_lbl_depth)
        self.sliders_lay.addRow(self.ext_sld_depth)



        self.bottom_btn_lay = QtWidgets.QHBoxLayout()
        self.bottom_btn_lay.addWidget(self.brick_btn)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.sliders_lay)
        self.main_layout.addLayout(self.bottom_btn_lay)
        self.setLayout(self.main_layout)


    def create_connections(self):
        """Connect our widget signal to slots"""
        self.ext_sld_row.valueChanged.connect(self.sld_lbl_row.setNum)
        self.ext_sld_col.valueChanged.connect(self.sld_lbl_col.setNum)
        self.ext_sld_bvl.valueChanged.connect(self.sld_lbl_bvl.setNum)
        self.ext_sld_offset.valueChanged.connect(self.sld_lbl_offset.setNum)
        self.ext_sld_width.valueChanged.connect(self.sld_lbl_width.setNum)
        self.ext_sld_height.valueChanged.connect(self.sld_lbl_height.setNum)
        self.ext_sld_depth.valueChanged.connect(self.sld_lbl_depth.setNum)
        self.brick_btn.clicked.connect(self.createbricks)


    def slider_value(self):
        slider_val_01 = self.ext_sld_row.value()
        return slider_val_01

    @QtCore.Slot()
    def createbricks(self):

        offx = 0.0
        offy = 0.0
        offz = 0.0
        row = int(self.ext_sld_row.value())
        col = int(self.ext_sld_col.value())
        bevel = float(self.ext_sld_bvl.value())
        width = float(self.ext_sld_width.value())
        height = float(self.ext_sld_height.value())
        depth = float(self.ext_sld_depth.value())
        offset = float(self.ext_sld_offset.value())

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