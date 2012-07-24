#!/usr/bin/python
#coding:utf-8
# Author:  Dan-Erik Lindberg -- <aideasypea@dan-erik.com>
# Created: 2012-07-12
# License: GPL-3

# Main window class

# First, and before importing any Enthought packages, set the ETS_TOOLKIT
# environment variable to qt4, to tell Traits that we will use Qt.
import os
os.environ["ETS_TOOLKIT"] = "qt4"
from pyface.qt import QtCore, QtGui

# These are the major Mayavi2 classes
from traits.api import HasTraits, Instance, on_trait_change, \
    Int, Dict
from traitsui.api import View, Item
from mayavi.core.ui.api import MayaviScene, MlabSceneModel, \
        SceneEditor

################################################################################
#The Mayavi 3D visualization
class Visualization(HasTraits):
    scene = Instance(MlabSceneModel, ())

    #----------------------------------------------------------------------
    @on_trait_change('scene.activated')
    def update_plot(self):
        # This function is called when the view is opened. We don't
        # populate the scene when the view is not yet open, as some
        # VTK features require a GLContext.

        # We can do normal mlab calls on the embedded scene.
        self.scene.mlab.test_points3d()

    # the layout of the dialog screated
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=250, width=300, show_label=False),
                resizable=True # We need this to resize with the parent widget
                )


################################################################################
# The QWidget containing the visualization, this is pure PyQt4 code.
# Just copied from the Mayavi Wiki page, but changed to OO code (super()).
class MayaviQWidget(QtGui.QWidget):
    #----------------------------------------------------------------------
    def __init__(self, parent=None):
        super(MayaviQWidget, self).__init__()
        layout = QtGui.QVBoxLayout(self)
        layout.setSpacing(0)
        self.visualization = Visualization()

        # If you want to debug, beware that you need to remove the Qt
        # input hook.
        #QtCore.pyqtRemoveInputHook()
        #import pdb ; pdb.set_trace()
        #QtCore.pyqtRestoreInputHook()

        # The edit_traits call will generate the widget to embed.
        self.ui = self.visualization.edit_traits(parent=self,
                                                 kind='subpanel').control
        layout.addWidget(self.ui)
        self.ui.setParent(self)

########################################################################
class MainWindow(QtGui.QMainWindow):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent=None):
        """Constructor"""
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("AidEasyPea")
        self.central = QtGui.QWidget()
        self.layout = QtGui.QGridLayout(self.central)

        # put some stuff around mayavi
        label_list = []
        for i in range(3):
            for j in range(3):
                if (i==1) and (j==1):continue
                label = QtGui.QLabel(self.central)
                label.setText("(%d, %d)" % (i,j))
                label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.layout.addWidget(label, i, j)
                label_list.append(label)
        self.mayavi_widget = MayaviQWidget(self.central)

        self.layout.addWidget(self.mayavi_widget, 1, 1)
        self.setCentralWidget(self.central)
        self.central.show()

