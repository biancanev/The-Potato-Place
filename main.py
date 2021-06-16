#!/usr/bin/python
"""
DevElec Main GUI

Author: Ryan Kwong
"""

#Import modules for use
import os
import sys#import the sys module for file operations
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication, QFileDialog, QLabel, QVBoxLayout, QInputDialog#import QT5 for GUI design


#Circuitry class for utility
class Circuit:
  #Initialize a circuit class with the basic components
  def __init__(self):
    #default name for circuits is untitled
    self.file = "untitled"
    #set empty dictionaries to store component ata
    self.components = {
      "power": {},#VCC, battery
      "ground": {},#GND
      "resistors": {}, #resistor
      "capacitors": {},#capacitor
      "ics": {
        "ttl":{},
        "cmos": {}
      }
    }
  #place componenet funtion
  def placeComponent(self):
    try:
      items = ("Power","Ground","Resistor", "Capacitor", "TTL", "CMOS", "Electromechanical")
      cat, okPressed = QInputDialog.getItem(self, "Select Item Category","Category:", items, 0, False)
      if okPressed and cat:
        if cat == "Resistor":
          comp = "resistors"
        elif cat == "Capacitor":
          comp = "capacitors"
        elif cat == "Power":
          pass
        elif cat == "Ground":
          pass
        elif cat == "TTL":
          pass
        elif cat == "CMOS":
          pass
        elif cat == "Electromechanical":
          pass
      path = os.path.dirname(os.path.realpath(__file__)) + "\lib\\" + comp + ".dvlc"#find file called <path of file>\lib\comp.dvlc
      name = str(len(self.components[comp]) + 1)
      self.components[comp][name] = "test"
      print(path)
      main()
    except:
      print("Error: unable to get component from library. Check to make sure the file directory is correct")
	#save file function
  def saveFile(self):
    try:
      file = QFileDialog.getSaveFileName(MainWindow(), "Save File", os.path.dirname(os.path.realpath(__file__)), "*.dvlschm")
      f = open(file, "w")
      f.write(self.components)
      f.close()
      main()
    except:
      os.system("error.vbs")
  #open file function
  def openFile(self):
    try:
      open(QFileDialog.getOpenFileName(MainWindow(), 'Open file', os.path.dirname(os.path.realpath(__file__)),"DevElec Files (*.dvlschm *.dvlgschm *.dvlpdschm *.dvlpj)"), "r+")
      main()
    except:
      os.system("error.vbs")
		
#define the import window
class importWindow:
  def __init__(self):
    pass

class errorWindow:
  def __init__(self, error):
    super().__init__()
    layout = QVBoxLayout()
    self.label = QLabel("An error occured... \n Error Message: " + error)
    layout.addWidget(self.label)
    self.setLayout(layout)

#define the main window
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    circuit = Circuit()
  	#set menubar items
    menubar = self.menuBar()
    fileMenu = menubar.addMenu('&File')
    simMenu = menubar.addMenu('&Simulate')
    libMenu = menubar.addMenu('&Library')
    globMenu = menubar.addMenu('&Global')
		#buttons under file
    saveFile = QAction('Save File', self)
    saveFileAs = QAction('Save File As', self)
		#buttons under import
    importMenu = QMenu('Import', self)
    importComp = QAction('Import Component', self)
    importDes = QAction('Import Design', self)
		#buttons under new
    newFile = QMenu('New', self)
    newSchem = QAction('New Schematic', self)
    newGSchem = QAction('New Guided Schematic', self)
    newPLD = QAction('New Programmable Device', self)
    newDoc = QAction('New Documentation', self)
    openFile = QAction('Open', self)
		#buttons under simulation
    simStart = QAction('Start Simulation', self)
    simStop = QAction('Stop Simulation', self)
	  #buttons under library
    libEdit = QAction('Edit Library', self)
	  #buttons under Global
    globEdit = QAction('Global Options', self)
		#add menubar items
    importMenu.addAction(importComp)
    importMenu.addAction(importDes)
    newFile.addAction(newSchem)
    newFile.addAction(newGSchem)
    newFile.addAction(newPLD)
    newFile.addAction(newDoc)
    simMenu.addAction(simStart)
    simMenu.addAction(simStop)
    libMenu.addAction(libEdit)
    globMenu.addAction(globEdit)
    fileMenu.addMenu(newFile)
    fileMenu.addMenu(importMenu)
    fileMenu.addAction(openFile)
    fileMenu.addAction(saveFile)
    fileMenu.addAction(saveFileAs)
		#button functionality
    saveFile.triggered.connect(lambda:circuit.saveFile())
    openFile.triggered.connect(lambda:circuit.openFile())
    importComp.triggered.connect(lambda:circuit.placeComponent())
    self.showMaximized()
    self.setWindowTitle('DevElec 2021 Version')
    self.show()
	

#Define main functions
def main():
  app = QApplication(sys.argv)
  ex = MainWindow()
  sys.exit(app.exec_())


if __name__ == '__main__':
  try:
    main()
  except:
    print(WindowsError)