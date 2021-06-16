import sys
from PyQt5.QtWidgets import * 
                    
   
#Main Window
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Component Library Editor'
        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 600
   
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
   
        self.createTable()
   
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)
   
        #Show window
        self.show()
   
    #Create table
    def createTable(self):
        self.tableWidget = QTableWidget()
  
        #Row count
        self.tableWidget.setRowCount(4) 
  
        #Column count
        self.tableWidget.setColumnCount(9)  
  
        self.tableWidget.setItem(0,0, QTableWidgetItem("Part Name"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Part Type"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("Part Number"))
        self.tableWidget.setItem(0,3, QTableWidgetItem("Intput(s)"))
        self.tableWidget.setItem(0,4, QTableWidgetItem("Outputs"))
        self.tableWidget.setItem(0,5, QTableWidgetItem("Min Voltage(V)"))
        self.tableWidget.setItem(0,6, QTableWidgetItem("Max Voltage(V)"))
        self.tableWidget.setItem(0,7, QTableWidgetItem("Min Current(A)"))
        self.tableWidget.setItem(0,8, QTableWidgetItem("Max Current(A)"))
        self.tableWidget.setItem(1,0, QTableWidgetItem("VCC"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Power Source"))
        self.tableWidget.setItem(1,2, QTableWidgetItem("vcc"))
        self.tableWidget.setItem(1,3, QTableWidgetItem("None"))
        self.tableWidget.setItem(1,4, QTableWidgetItem("Vout"))
        self.tableWidget.setItem(1,5, QTableWidgetItem("Predetermined"))
        self.tableWidget.setItem(1,6, QTableWidgetItem("Predetermined"))
        self.tableWidget.setItem(1,7, QTableWidgetItem("Predetermined"))
        self.tableWidget.setItem(1,8, QTableWidgetItem("Predetermined"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("D Flip-Flop"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("IC"))
        self.tableWidget.setItem(2,2, QTableWidgetItem("74LS74N"))
        self.tableWidget.setItem(2,3, QTableWidgetItem("D, CLK"))
        self.tableWidget.setItem(2,4, QTableWidgetItem("Q, Q~"))
        self.tableWidget.setItem(2,5, QTableWidgetItem("2"))
        self.tableWidget.setItem(2,6, QTableWidgetItem("15"))
        self.tableWidget.setItem(2,7, QTableWidgetItem("0.004"))
        self.tableWidget.setItem(2,8, QTableWidgetItem("0.008"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("LED"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("LEDs"))
        self.tableWidget.setItem(2,2, QTableWidgetItem("led-green"))
        self.tableWidget.setItem(2,3, QTableWidgetItem("cathode"))
        self.tableWidget.setItem(2,4, QTableWidgetItem("anode"))
        self.tableWidget.setItem(2,5, QTableWidgetItem("1.7"))
        self.tableWidget.setItem(2,6, QTableWidgetItem("3.1"))
        self.tableWidget.setItem(2,7, QTableWidgetItem("0.01"))
        self.tableWidget.setItem(2,8, QTableWidgetItem("0.03"))
   
        #Table will fit the screen horizontally
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
   
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())