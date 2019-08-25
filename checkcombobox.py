from PyQt5 import QtGui, QtCore, QtWidgets
from First import *
from JobSearch import *
import sys, os

row_table = {"Job File No":True, "JJ No":True, "Shipper":True, "Consignee":True,
             "Booking No":True,"BL/AWB":True,"Origin":True,"Destination":True,"Container No":True}

class CheckableComboBox(QtWidgets.QComboBox):
    def additem(self, item, check):
        if(check):
            super(CheckableComboBox, self).addItem(item)
            item = self.model().item(self.count()-1,0)
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.Unchecked)
        else:
            super(CheckableComboBox, self).addItem(item)

    def itemChecked(self, index):
        item = self.model().item(index,0)
        return item.checkState() == QtCore.Qt.Checked

    def hidePopup(self):
        access = {}
        
        length = self.count()
        for i in range(1,self.count()):
            access[self.itemText(i)] = self.itemChecked(i)

        for i in range(self.count()):
            self.removeItem(0)

        self.additem("SORT", False)

        for item in access:
            if(access[item] == True):
                self.addItem(item)
                item = self.model().item(self.count()-1,0)
                item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item.setCheckState(QtCore.Qt.Checked)
            else:
                row_table[item] = False
                self.additem(item, True)
        
        QtWidgets.QComboBox.hidePopup(self)
            
    def showPopup(self):
        for i in range(self.count()):
            self.removeItem(0)
            
        self.additem("", False)
        
        for row_item in row_table.keys():
            self.additem(row_item, True)
            item = self.model().item(self.count()-1,0)
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)

            if(row_table[row_item]):
                item.setCheckState(QtCore.Qt.Checked)

        QtWidgets.QComboBox.showPopup(self)

