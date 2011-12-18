"""
/***************************************************************************
 QuantumFtDialog
                                 A QGIS plugin
 Tool to export data from the bench to Fusion Tables
                             -------------------
        begin                : 2011-12-17
        copyright            : (C) 2011 by Jude Mwenda/AfriGeo
        email                : jude@afrigeo.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_quantumft import Ui_QuantumFt
# create the dialog for zoom to point
class QuantumFtDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_QuantumFt()
        self.ui.setupUi(self)
