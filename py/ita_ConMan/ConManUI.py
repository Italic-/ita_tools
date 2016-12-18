#!/usr/autodesk/maya/bin/mayapy
# encoding: utf-8
# Generated by pyside-uic from Qt Designer, modified

import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

try:
    from utils.qtshim import QtCore, QtGui, Signal
    log.info("Imported UI libs from qtshim.")
except ImportError:
    from PySide import QtCore, QtGui
    Signal = QtCore.Signal
    log.info("Could not find qtshim. Importing from system/application PySide.")

_CManHelp = None


class QListItemCon(QtGui.QListWidgetItem):
    """
    Save constraint data for immediate retrieval through the UI.
    Data saved with scene is stored in __init__.ConItemList.
    """

    def __init__(self, data, parent=None):
        super(QListItemCon, self).__init__(parent)
        self._data = data
        self._entry_label = "{} | {} | {}".format(
            str(self._data["object"]),
            self._data["type"],
            str(self._data["con_node"]))

    def data(self, role):
        if role == QtCore.Qt.DisplayRole:
            return self.label

    @property
    def label(self):
        return self._entry_label

    @label.setter
    def label(self, label):
        self._entry_label = label

    @QtCore.Slot()
    def update_label_callback(self):
        if self.label != "{} | {} | {}".format(
                str(self._data["object"]),
                self._data["type"],
                str(self._data["con_node"])):
            self.label = "{} | {} | {}".format(
                str(self._data["object"]),
                self._data["type"],
                str(self._data["con_node"]))

    @property
    def con_type(self):
        return self._data["type"]

    @property
    def obj(self):
        return self._data["object"]

    @property
    def target(self):
        return self._data["target"]

    @property
    def con_node(self):
        return self._data["con_node"]

    @property
    def object_uuid(self):
        return cmds.ls(str(self._data["object"]), uuid=True)[0]

    @property
    def target_uuid(self):
        return [cmds.ls(str(obj), uuid=True)[0] for obj in self._data["target"]]

    @property
    def con_uuid(self):
        return cmds.ls(str(self._data["con_node"]), uuid=True)[0]


class ConManWindow(QtGui.QMainWindow):
    CloseSig = Signal()
    RenameSig = Signal()
    AddSig = Signal()
    DelSig = Signal(list)
    SelSig = Signal(list)
    OptionsSig = Signal(str, tuple, bool, float, list, list, list)

    def __init__(self, parent=None):
        super(ConManWindow, self).__init__(parent=parent)
        self.settings = QtCore.QSettings("italic", "ConMan2")
        self.setupUi()
        self.move(self.settings.value("mainwindowposition", QtCore.QPoint(0, 0)))

    def setupUi(self):
        """Set up main UI."""
        self.setObjectName("ConManWindow")
        self.resize(250, 425)
        self.setMinimumSize(250, 425)
        self.setMaximumSize(250, 425)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setFamily("Arial")
        self.setFont(font)
        self.setTabShape(QtGui.QTabWidget.Rounded)
        #
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setMinimumSize(QtCore.QSize(250, 425))
        self.centralwidget.setMaximumSize(QtCore.QSize(250, 425))
        #
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 250, 425))
        #
        self.LayoutVert1 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.LayoutVert1.setSpacing(2)
        self.LayoutVert1.setContentsMargins(5, -1, 5, -1)
        #
        self.ObjList = QtGui.QListWidget()
        self.ObjList.setMinimumSize(QtCore.QSize(240, 125))
        self.ObjList.setMaximumSize(QtCore.QSize(240, 125))
        self.ObjList.setFrameShape(QtGui.QFrame.NoFrame)
        self.ObjList.setFrameShadow(QtGui.QFrame.Plain)
        self.ObjList.setToolTip("Click to see switching options.\nDouble click to select constrained object.")
        #
        self.ButtonRow1 = QtGui.QHBoxLayout()
        self.ButtonRow1.setSpacing(0)
        #
        self.ButtonAdd = QtGui.QPushButton(self.verticalLayoutWidget)
        self.ButtonAdd.setEnabled(True)
        self.ButtonAdd.setMinimumSize(QtCore.QSize(40, 40))
        self.ButtonAdd.setMaximumSize(QtCore.QSize(40, 40))
        self.ButtonAdd.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pickHandlesComp.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ButtonAdd.setIcon(icon)
        self.ButtonAdd.setIconSize(QtCore.QSize(40, 40))
        self.ButtonAdd.setFlat(False)
        self.ButtonAdd.setToolTip("Add selected constraint nodes to the list.")
        #
        self.ButtonParent = QtGui.QPushButton(self.verticalLayoutWidget)
        self.ButtonParent.setMinimumSize(QtCore.QSize(40, 40))
        self.ButtonParent.setMaximumSize(QtCore.QSize(40, 40))
        self.ButtonParent.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/parentConstraint.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ButtonParent.setIcon(icon1)
        self.ButtonParent.setIconSize(QtCore.QSize(40, 40))
        self.ButtonParent.setFlat(False)
        self.ButtonParent.setToolTip("Create a parent constraint with options below.")
        #
        self.ButtonPoint = QtGui.QPushButton(self.verticalLayoutWidget)
        self.ButtonPoint.setMinimumSize(QtCore.QSize(40, 40))
        self.ButtonPoint.setMaximumSize(QtCore.QSize(40, 40))
        self.ButtonPoint.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/posConstraint.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ButtonPoint.setIcon(icon2)
        self.ButtonPoint.setIconSize(QtCore.QSize(40, 40))
        self.ButtonPoint.setFlat(False)
        self.ButtonPoint.setToolTip("Create a point constraint with options below.")
        #
        self.ButtonOrient = QtGui.QPushButton(self.verticalLayoutWidget)
        self.ButtonOrient.setMinimumSize(QtCore.QSize(40, 40))
        self.ButtonOrient.setMaximumSize(QtCore.QSize(40, 40))
        self.ButtonOrient.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/orientConstraint.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ButtonOrient.setIcon(icon3)
        self.ButtonOrient.setIconSize(QtCore.QSize(40, 40))
        self.ButtonOrient.setFlat(False)
        self.ButtonOrient.setToolTip("Create an orient constraint with options below.")
        #
        self.ButtonScale = QtGui.QPushButton(self.verticalLayoutWidget)
        self.ButtonScale.setMinimumSize(QtCore.QSize(40, 40))
        self.ButtonScale.setMaximumSize(QtCore.QSize(40, 40))
        self.ButtonScale.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/scaleConstraint.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ButtonScale.setIcon(icon4)
        self.ButtonScale.setIconSize(QtCore.QSize(40, 40))
        self.ButtonScale.setFlat(False)
        self.ButtonScale.setToolTip("Create a scale constraint with options below.")
        #
        self.ButtonRemove = QtGui.QPushButton(self.verticalLayoutWidget)
        self.ButtonRemove.setMinimumSize(QtCore.QSize(40, 40))
        self.ButtonRemove.setMaximumSize(QtCore.QSize(40, 40))
        self.ButtonRemove.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/smallTrash.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ButtonRemove.setIcon(icon5)
        self.ButtonRemove.setIconSize(QtCore.QSize(40, 40))
        self.ButtonRemove.setFlat(False)
        self.ButtonRemove.setToolTip("Click to remove constraint from list. Double click to delete from scene.")
        #
        self.tabWidget = QtGui.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(240, 205))
        self.tabWidget.setMaximumSize(QtCore.QSize(240, 205))
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        #
        self.tabBar = QtGui.QTabBar(self.verticalLayoutWidget)
        self.tabWidget.setTabBar(self.tabBar)
        #
        self.ConstraintOptions = QtGui.QWidget()
        #
        self.gridLayoutWidget = QtGui.QWidget(self.ConstraintOptions)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 240, 185))
        #
        self.OptionsGrid = QtGui.QGridLayout(self.gridLayoutWidget)
        self.OptionsGrid.setContentsMargins(-1, -1, -1, -1)
        self.OptionsGrid.setHorizontalSpacing(2)
        self.OptionsGrid.setVerticalSpacing(2)
        #
        # Labels
        self.LabelOffset = QtGui.QLabel(self.gridLayoutWidget)
        self.LabelOffset.setFont(font)
        self.LabelOffset.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        #
        self.LabelMOffset = QtGui.QLabel(self.gridLayoutWidget)
        self.LabelMOffset.setFont(font)
        self.LabelMOffset.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        #
        self.LabelTr = QtGui.QLabel(self.gridLayoutWidget)
        self.LabelTr.setFont(font)
        self.LabelTr.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        #
        self.LabelRo = QtGui.QLabel(self.gridLayoutWidget)
        self.LabelRo.setFont(font)
        self.LabelRo.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        #
        self.LabelSc = QtGui.QLabel(self.gridLayoutWidget)
        self.LabelSc.setFont(font)
        self.LabelSc.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        #
        self.LabelWeight = QtGui.QLabel(self.gridLayoutWidget)
        self.LabelWeight.setFont(font)
        self.LabelWeight.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LabelWeight.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        #
        # Checkboxes
        self.CheckOffset = QtGui.QCheckBox(self.gridLayoutWidget)
        self.CheckOffset.setText("")
        self.CheckOffset.setChecked(True)
        #
        # Translate checkboxes
        self.CheckTrAll = QtGui.QCheckBox(self.gridLayoutWidget)
        self.CheckTrAll.setFont(font)
        self.CheckTrAll.setChecked(True)
        #
        self.CheckTrX = QtGui.QCheckBox(self.gridLayoutWidget)
        self.CheckTrX.setFont(font)
        #
        self.CheckTrY = QtGui.QCheckBox(self.gridLayoutWidget)
        self.CheckTrY.setFont(font)
        #
        self.CheckTrZ = QtGui.QCheckBox(self.gridLayoutWidget)
        self.CheckTrZ.setFont(font)
        #
        # Rotate checkboxes
        self.CheckRoAll = QtGui.QCheckBox(self.gridLayoutWidget)
        self.CheckRoAll.setFont(font)
        self.CheckRoAll.setChecked(True)
        #
        self.CheckRoX = QtGui.QCheckBox(self.gridLayoutWidget)
        self.CheckRoX.setFont(font)
        #
        self.CheckRoY = QtGui.QCheckBox(self.gridLayoutWidget)
        self.CheckRoY.setFont(font)
        #
        self.CheckRoZ = QtGui.QCheckBox(self.gridLayoutWidget)
        self.CheckRoZ.setFont(font)
        #
        # Scale checkboxes
        self.CheckScAll = QtGui.QCheckBox(self.gridLayoutWidget)
        self.CheckScAll.setFont(font)
        self.CheckScAll.setChecked(True)
        #
        self.CheckScX = QtGui.QCheckBox(self.gridLayoutWidget)
        self.CheckScX.setFont(font)
        #
        self.CheckScY = QtGui.QCheckBox(self.gridLayoutWidget)
        self.CheckScY.setFont(font)
        #
        self.CheckScZ = QtGui.QCheckBox(self.gridLayoutWidget)
        self.CheckScZ.setFont(font)
        #
        # Spin boxes
        self.SpinOffsetX = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.SpinOffsetX.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        #
        self.SpinOffsetY = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.SpinOffsetY.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        #
        self.SpinOffsetZ = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.SpinOffsetZ.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        #
        self.SpinWeight = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.SpinWeight.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.SpinWeight.setMaximum(1.0)
        self.SpinWeight.setSingleStep(0.1)
        self.SpinWeight.setProperty("value", 1.0)
        #
        self.Switch = QtGui.QWidget()
        #
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.Switch)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 235, 110))
        #
        self.SwitchCol = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.SwitchCol.setSpacing(4)
        self.SwitchCol.setContentsMargins(5, 5, 5, 5)
        #
        self.MenuSwitchTarget = QtGui.QComboBox(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        self.MenuSwitchTarget.setSizePolicy(sizePolicy)
        self.MenuSwitchTarget.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.MenuSwitchTarget.setFrame(True)
        self.MenuSwitchTarget.setToolTip("Select a target to switch to...")
        #
        self.ButtonRow3 = QtGui.QHBoxLayout()
        self.ButtonRow3.setSpacing(4)
        #
        self.ButtonOff = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.ButtonOff.setMinimumHeight(25)
        self.ButtonOff.setToolTip("Turn all target weights OFF.")
        #
        self.ButtonAll = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.ButtonAll.setMinimumHeight(25)
        self.ButtonAll.setToolTip("Turn all target weights ON.")
        #
        self.ButtonSwitch = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.ButtonSwitch.setMinimumHeight(25)
        self.ButtonSwitch.setToolTip("Weight constraint to a single target.")
        #
        self.CheckVisTrans = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.CheckVisTrans.setChecked(True)
        self.CheckVisTrans.setToolTip("Keep object in the same position\nby updating constraint offsets.")
        #
        self.CheckKey = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.CheckKey.setChecked(True)
        self.CheckKey.setToolTip("Key offsets, transforms and blend attributes.")
        #
        self.ButtonRow2 = QtGui.QHBoxLayout()
        self.ButtonRow2.setSpacing(0)
        #
        self.ButtonHelp = QtGui.QPushButton(self.verticalLayoutWidget)
        self.ButtonHelp.setMinimumHeight(30)
        self.ButtonHelp.setFont(font)
        self.ButtonHelp.setToolTip("Open help documentation.")
        #
        self.ButtonClean = QtGui.QPushButton(self.verticalLayoutWidget)
        self.ButtonClean.setMinimumHeight(30)
        self.ButtonClean.setFont(font)
        self.ButtonClean.setToolTip("Clean stale ConMan data.")
        #
        self.ButtonPurge = QtGui.QPushButton(self.verticalLayoutWidget)
        self.ButtonPurge.setMinimumHeight(30)
        self.ButtonPurge.setFont(font)
        self.ButtonPurge.setToolTip("Remove all ConMan data. \nWARNING: CANNOT BE UNDONE")
        #
        self.place_ui()
        self.retranslate_ui()
        self.set_connections()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.set_tab_order()

    def place_ui(self):
        self.LayoutVert1.addWidget(self.ObjList)
        self.ButtonRow1.addWidget(self.ButtonAdd)
        self.ButtonRow1.addWidget(self.ButtonParent)
        self.ButtonRow1.addWidget(self.ButtonPoint)
        self.ButtonRow1.addWidget(self.ButtonOrient)
        self.ButtonRow1.addWidget(self.ButtonScale)
        self.ButtonRow1.addWidget(self.ButtonRemove)
        self.LayoutVert1.addLayout(self.ButtonRow1)
        self.OptionsGrid.addWidget(self.LabelOffset, 1, 0, 1, 1)
        self.OptionsGrid.addWidget(self.LabelMOffset, 0, 0, 1, 1)
        self.OptionsGrid.addWidget(self.LabelTr, 2, 0, 1, 1)
        self.OptionsGrid.addWidget(self.LabelRo, 4, 0, 1, 1)
        self.OptionsGrid.addWidget(self.LabelSc, 6, 0, 1, 1)
        self.OptionsGrid.addWidget(self.LabelWeight, 8, 0, 1, 1)
        self.OptionsGrid.addWidget(self.CheckOffset, 0, 1, 1, 1)
        self.OptionsGrid.addWidget(self.CheckTrAll, 2, 1, 1, 1)
        self.OptionsGrid.addWidget(self.CheckTrX, 3, 1, 1, 1)
        self.OptionsGrid.addWidget(self.CheckTrY, 3, 2, 1, 1)
        self.OptionsGrid.addWidget(self.CheckTrZ, 3, 3, 1, 1)
        self.OptionsGrid.addWidget(self.CheckRoAll, 4, 1, 1, 1)
        self.OptionsGrid.addWidget(self.CheckRoX, 5, 1, 1, 1)
        self.OptionsGrid.addWidget(self.CheckRoY, 5, 2, 1, 1)
        self.OptionsGrid.addWidget(self.CheckRoZ, 5, 3, 1, 1)
        self.OptionsGrid.addWidget(self.CheckScAll, 6, 1, 1, 1)
        self.OptionsGrid.addWidget(self.CheckScX, 7, 1, 1, 1)
        self.OptionsGrid.addWidget(self.CheckScY, 7, 2, 1, 1)
        self.OptionsGrid.addWidget(self.CheckScZ, 7, 3, 1, 1)
        self.OptionsGrid.addWidget(self.SpinOffsetX, 1, 1, 1, 1)
        self.OptionsGrid.addWidget(self.SpinOffsetY, 1, 2, 1, 1)
        self.OptionsGrid.addWidget(self.SpinOffsetZ, 1, 3, 1, 1)
        self.OptionsGrid.addWidget(self.SpinWeight, 8, 1, 1, 1)
        self.tabWidget.addTab(self.ConstraintOptions, "")
        self.SwitchCol.addWidget(self.MenuSwitchTarget)
        self.ButtonRow3.addWidget(self.ButtonOff)
        self.ButtonRow3.addWidget(self.ButtonAll)
        self.ButtonRow3.addWidget(self.ButtonSwitch)
        self.SwitchCol.addLayout(self.ButtonRow3)
        self.SwitchCol.addWidget(self.CheckVisTrans)
        self.SwitchCol.addWidget(self.CheckKey)
        self.tabWidget.addTab(self.Switch, "")
        self.LayoutVert1.addWidget(self.tabWidget)
        self.ButtonRow2.addWidget(self.ButtonHelp)
        self.ButtonRow2.addWidget(self.ButtonClean)
        self.ButtonRow2.addWidget(self.ButtonPurge)
        self.LayoutVert1.addLayout(self.ButtonRow2)
        self.setCentralWidget(self.centralwidget)

    def retranslate_ui(self):
        """Fill in UI text and special commands."""
        self.setWindowTitle(QtGui.QApplication.translate("ConManWindow", "Constraint Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelOffset.setText(QtGui.QApplication.translate("ConManWindow", "Offset", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelMOffset.setText(QtGui.QApplication.translate("ConManWindow", "Maintain Off", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelTr.setText(QtGui.QApplication.translate("ConManWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelRo.setText(QtGui.QApplication.translate("ConManWindow", "Rotate", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelSc.setText(QtGui.QApplication.translate("ConManWindow", "Scale", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelWeight.setText(QtGui.QApplication.translate("ConManWindow", "Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.CheckTrAll.setText(QtGui.QApplication.translate("ConManWindow", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.CheckTrX.setText(QtGui.QApplication.translate("ConManWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.CheckTrY.setText(QtGui.QApplication.translate("ConManWindow", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.CheckTrZ.setText(QtGui.QApplication.translate("ConManWindow", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.CheckRoAll.setText(QtGui.QApplication.translate("ConManWindow", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.CheckRoX.setText(QtGui.QApplication.translate("ConManWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.CheckRoY.setText(QtGui.QApplication.translate("ConManWindow", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.CheckRoZ.setText(QtGui.QApplication.translate("ConManWindow", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.CheckScAll.setText(QtGui.QApplication.translate("ConManWindow", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.CheckScX.setText(QtGui.QApplication.translate("ConManWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.CheckScY.setText(QtGui.QApplication.translate("ConManWindow", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.CheckScZ.setText(QtGui.QApplication.translate("ConManWindow", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ConstraintOptions), QtGui.QApplication.translate("ConManWindow", "Constraint Options", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonOff.setText(QtGui.QApplication.translate("ConManWindow", "OFF", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonAll.setText(QtGui.QApplication.translate("ConManWindow", "ALL", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonSwitch.setText(QtGui.QApplication.translate("ConManWindow", "Switch", None, QtGui.QApplication.UnicodeUTF8))
        self.CheckVisTrans.setText(QtGui.QApplication.translate("ConManWindow", "Maintain Visual Transforms", None, QtGui.QApplication.UnicodeUTF8))
        self.CheckKey.setText(QtGui.QApplication.translate("ConManWindow", "Key", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Switch), QtGui.QApplication.translate("ConManWindow", "Switch", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonHelp.setText(QtGui.QApplication.translate("ConManWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonClean.setText(QtGui.QApplication.translate("ConManWindow", "Clean Stale", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonPurge.setText(QtGui.QApplication.translate("ConManWindow", "Purge...", None, QtGui.QApplication.UnicodeUTF8))

    def set_tab_order(self):
        self.setTabOrder(self.ObjList, self.ButtonAdd)
        self.setTabOrder(self.ButtonAdd, self.ButtonParent)
        self.setTabOrder(self.ButtonParent, self.ButtonPoint)
        self.setTabOrder(self.ButtonPoint, self.ButtonOrient)
        self.setTabOrder(self.ButtonOrient, self.ButtonScale)
        self.setTabOrder(self.ButtonScale, self.ButtonRemove)
        self.setTabOrder(self.ButtonRemove, self.tabWidget)
        self.setTabOrder(self.tabWidget, self.CheckOffset)
        self.setTabOrder(self.CheckOffset, self.SpinOffsetX)
        self.setTabOrder(self.SpinOffsetX, self.SpinOffsetY)
        self.setTabOrder(self.SpinOffsetY, self.SpinOffsetZ)
        self.setTabOrder(self.SpinOffsetZ, self.CheckTrAll)
        self.setTabOrder(self.CheckTrAll, self.CheckTrX)
        self.setTabOrder(self.CheckTrX, self.CheckTrY)
        self.setTabOrder(self.CheckTrY, self.CheckTrZ)
        self.setTabOrder(self.CheckTrZ, self.CheckRoAll)
        self.setTabOrder(self.CheckRoAll, self.CheckRoX)
        self.setTabOrder(self.CheckRoX, self.CheckRoY)
        self.setTabOrder(self.CheckRoY, self.CheckRoZ)
        self.setTabOrder(self.CheckRoZ, self.CheckScAll)
        self.setTabOrder(self.CheckScAll, self.CheckScX)
        self.setTabOrder(self.CheckScX, self.CheckScY)
        self.setTabOrder(self.CheckScY, self.CheckScZ)
        self.setTabOrder(self.CheckScZ, self.SpinWeight)
        self.setTabOrder(self.SpinWeight, self.MenuSwitchTarget)
        self.setTabOrder(self.MenuSwitchTarget, self.ButtonOff)
        self.setTabOrder(self.ButtonOff, self.ButtonAll)
        self.setTabOrder(self.ButtonAll, self.ButtonSwitch)
        self.setTabOrder(self.ButtonSwitch, self.CheckVisTrans)
        self.setTabOrder(self.CheckVisTrans, self.CheckKey)
        self.setTabOrder(self.CheckKey, self.ButtonHelp)
        self.setTabOrder(self.ButtonHelp, self.ButtonClean)
        self.setTabOrder(self.ButtonClean, self.ButtonPurge)

    def set_connections(self):
        self.ButtonAdd.clicked.connect(self.add_con)
        self.ButtonParent.clicked.connect(lambda: self.send_options("Parent"))
        self.ButtonPoint.clicked.connect(lambda: self.send_options("Point"))
        self.ButtonOrient.clicked.connect(lambda: self.send_options("Orient"))
        self.ButtonScale.clicked.connect(lambda: self.send_options("Scale"))
        self.ButtonRemove.clicked.connect(self.remove_con)
        self.ButtonHelp.clicked.connect(self.show_help_ui)
        # self.ButtonClean.clicked.connect()
        # self.ButtonPurge.clicked.connect()
        self.ObjList.itemEntered.connect(self.item_list_click)
        self.ObjList.itemDoubleClicked.connect(self.item_list_double_click)

    def closeEvent(self, *args, **kwargs):
        log.debug("Closing main window...")
        self.CloseSig.emit()
        self.settings.setValue("mainwindowposition", self.pos())
        QtGui.QMainWindow.closeEvent(self, *args, **kwargs)

    def show_help_ui(self):
        global _CManHelp
        if _CManHelp is None:
            _CManHelp = ConManHelpWindow()
        _CManHelp.show()

    def clear_list(self, arg=None):
        log.debug("Clearing list")
        self.ObjList.clear()

    def populate_list(self, data):
        listItem = QListItemCon(data)
        self.RenameSig.connect(listItem.update_label_callback)
        self.ObjList.addItem(listItem)
        self.ObjList.sortItems(order=QtCore.Qt.AscendingOrder)

    def populate_menu(self, selObjs):
        """Populate combo box for target selection."""
        self.MenuSwitchTarget.clear()
        for ind, item in enumerate(selObjs):
            self.MenuSwitchTarget.addItem(str(item))
            self.MenuSwitchTarget.setItemData(ind, str(item), userData=item)

    def send_options(self, conType):
        skipT = []
        skipR = []
        skipS = []

        axes = ("x", "y", "z")

        TAll = (TX, TY, TZ) = (
            self.CheckTrX.isChecked(),
            self.CheckTrY.isChecked(),
            self.CheckTrZ.isChecked()
        )
        RAll = (RX, RY, RZ) = (
            self.CheckRoX.isChecked(),
            self.CheckRoY.isChecked(),
            self.CheckRoZ.isChecked()
        )
        SAll = (SX, SY, SZ) = (
            self.CheckScX.isChecked(),
            self.CheckScY.isChecked(),
            self.CheckScZ.isChecked()
        )

        for c, a in zip(TAll, axes):
            if not c:
                skipT.append(a)
        for c, a in zip(RAll, axes):
            if not c:
                skipR.append(a)
        for c, a in zip(SAll, axes):
            if not c:
                skipS.append(a)

        if self.CheckTrAll.isChecked():
            skipT = ['none']
        if self.CheckRoAll.isChecked():
            skipR = ['none']
        if self.CheckScAll.isChecked():
            skipS = ['none']

        mOffset = self.CheckOffset.isChecked()
        weight = self.SpinWeight.value()
        Offset = (
            self.SpinOffsetX.value(),
            self.SpinOffsetY.value(),
            self.SpinOffsetZ.value()
        )

        log.debug("Offset: {}".format(Offset))
        log.debug("Maintain offset: {}".format(mOffset))
        log.debug("Weight: {}".format(weight))
        log.debug("Skip translate: {}".format(skipT))
        log.debug("Skip rotate: {}".format(skipR))
        log.debug("Skip scale: {}".format(skipS))

        self.OptionsSig.emit(conType, Offset, mOffset, weight, skipT, skipR, skipS)

    def add_con(self):
        self.AddSig.emit()

    def remove_con(self, arg=None):
        current_row = self.ObjList.currentRow()
        current_item = self.ObjList.item(current_row)

        log.debug("Removing {} from list...".format(current_item.label))

        self.DelSig.emit(current_item.con_node)

        removed_item = self.ObjList.takeItem(current_row)
        del removed_item

        log.debug("Removed {}...".format(current_item.label))

    def iter_list(self):
        return [self.ObjList.item(i) for i in range(self.ObjList.count())]

    def item_list_click(self, item):
        log.debug("Clicked: {}".format(item.text()))
        log.debug("Targets: {}".format(item.target))
        self.populate_menu(item.target)

    def item_list_double_click(self, item):
        log.debug("Double clicked: {}".format(item.text()))
        log.debug("Selecting: {}".format(item.obj))
        self.SelSig.emit(item.obj)


class ConManHelpWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(ConManHelpWindow, self).__init__(parent=parent)

        self.helpText = (
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">ConMan2</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A constraint manager for rigging and animation.</p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Create</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Create common constraints (parent, point, orient, scale) with the given options.</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Remove</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Remove a constraint from the list with the trash icon; delete from the scene with double click.</p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Switch</span></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Switch constraint targets in the second section. Select a constraint, then a target in the dropdown menu.</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">OFF</span> turns off all weights and blend attributes.</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">ON</span> turns on all weights and blend attributes.</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">SWITCH</span> activates a single target and blend attributes and deactivates the rest.</p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Maintain Visual Transforms</span>: Update constraint offsets to maintain the object\'s world-space transforms.</p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Key</span>: Animate the switch across two frames (current and immediately previous).</p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Constraint data is saved in the scene file.</p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            # "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Clean Stale</span>: Remove old data of non-existant objects. Any data not shown in the list is removed.</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Purge...</span>: Remove ALL saved constraint data from the scene.</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">WARNING: THIS IS NOT UNDO-ABLE!</p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">LIMITATIONS AND KNOWN ISSUES:</p>\n"
            # "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- This tool supports only one parent constraint at a time. Maya supports multiple parent constraints and one of any other kind.</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- Maintain Visual Transforms: Currently updates offsets in the constraint node. Enable keying to save old offsets during switching.</p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(c) Jeffrey &quot;italic&quot; Hoover</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">italic DOT rendezvous AT gmail DOT com</p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Licensed under the Apache 2.0 license.</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This script can be used for commercial and non-commercial projects free of charge.</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.apache.org/licenses/LICENSE-2.0\"><span style=\" text-decoration: underline; color:#0057ae;\">https://www.apache.org/licenses/LICENSE-2.0</span></a></p></body></html>"
        )

        self.settings = QtCore.QSettings("italic", "ConMan2")
        self.show_ui()
        self.move(self.settings.value("helpwindowposition", QtCore.QPoint(0, 0)))

    def show_ui(self):
        self.setObjectName("ConManHelpWindow")
        self.setWindowTitle("ConMan Help")
        self.resize(325, 250)
        self.setMinimumSize(325, 250)
        self.setMaximumSize(600, 425)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setFamily("Arial")
        self.setFont(font)
        #
        self.centralwidget = QtGui.QWidget(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(325, 250))
        self.centralwidget.setMaximumSize(QtCore.QSize(600, 425))
        self.centralwidget.setObjectName("centralwidget")
        #
        self.vlayout = QtGui.QVBoxLayout(self.centralwidget)
        self.vlayout.setSpacing(2)
        self.vlayout.setContentsMargins(2, 2, 2, 2)
        self.vlayout.setObjectName("VLayout")
        #
        self.textwidget = QtGui.QTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.textwidget.setSizePolicy(sizePolicy)
        self.textwidget.setReadOnly(True)
        self.textwidget.setObjectName("TextWidget")
        self.textwidget.setHtml(self.helpText)
        #
        self.vlayout.addWidget(self.textwidget)
        #
        self.setCentralWidget(self.centralwidget)

    def closeEvent(self, *args, **kwargs):
        log.debug("Closing help window...")
        self.settings.setValue("helpwindowposition", self.pos())
        QtGui.QMainWindow.closeEvent(self, *args, **kwargs)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    generic_data = {
        "type": "Parent",
        "object": "active object1",
        "target": ["sel obj 1", "sel obj 2"],
        "con_node": "con node name"
    }

    win = QtGui.QApplication([])
    _CMan = ConManWindow()
    _CMan.show()
    _CMan.populate_list(generic_data)

    win.exec_()
