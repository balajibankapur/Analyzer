from PyQt4.QtGui import * 
from PyQt4.QtCore import * 

import csv
import sys

def main():
    app	     = QApplication(sys.argv)
    analyzerWidget = Analyzer()
    
    screen_resolution = app.desktop().screenGeometry()
    screenWidth, screenHeight = screen_resolution.width(), screen_resolution.height()

    analyzerWidget.setGeometry(0, 0, screenWidth, screenHeight)
    analyzerWidget.show()
    return app.exec_()

class Analyzer(QWidget):
	
	def __init__(self, parent = None):
		QWidget.__init__(self, parent)
		self.rowCount = 8
		self.colCount = 8
		self.details = []
		self.details.append([])
		self.details.append([])
		self.details.append([])
		self.table  = QTableWidget(self)
		self.setupUi()
		self.Analyze()
		self.detaillabel = QTextEdit(self)

	def setupUi(self):
		# initiate table
		self.table.setWindowTitle("Details")
		self.table.setColumnCount(self.colCount)
	
	def resizeEvent (self, event):
		self.screenWidth = self.size().width()
		self.table.setGeometry(0, 0, self.screenWidth, 400)
		colWidth = self.screenWidth/self.colCount
		for index in xrange(0, self.colCount):
			self.table.setColumnWidth(index, colWidth)
		self.detaillabel.setGeometry(0,410,self.size().width()/2,200)
	
	def Analyze(self):
		#Remove all items
		self.table.clearContents()

		#Set row count to 0 (remove rows)
		self.table.setRowCount(0)

		self.table.cellClicked.connect(self.cell_was_clicked)

		#Display the table
		with open('input.csv') as csvDataFile:
			csvReader = csv.reader(csvDataFile)
			for row in csvReader:
				rowPosition = self.table.rowCount()
				self.table.insertRow(rowPosition)
				self.details[rowPosition].append(row)
				for index in xrange(0, self.colCount):
					self.table.setItem(rowPosition,index, QTableWidgetItem(row[index]))
      				#print(rowPosition)
      				#print(index)
      			

	def cell_was_clicked(self, row, col):
		rowItems = self.details[row]
		print(col)
		self.detaillabel.setText(rowItems[col])
#		print(self.details[0][7])

if __name__ == '__main__':
    main()