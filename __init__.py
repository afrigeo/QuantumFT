"""
/***************************************************************************
 QuantumFt
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
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "Q-GIS Export to Fusion Tables"
def description():
    return "Tool to export data from the bench to Fusion Tables"
def version():
    return "Version 0.1"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.0"
def classFactory(iface):
    # load QuantumFt class from file QuantumFt
    from quantumft import QuantumFt
    return QuantumFt(iface)
