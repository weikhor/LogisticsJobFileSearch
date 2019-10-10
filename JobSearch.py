import sys
import os
import shutil

from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem, QMessageBox, QMainWindow, QTableWidgetItem, QTextEdit,QFileDialog,QSizePolicy, QMessageBox,QCompleter
from PyQt5 import QtCore
from First import *
from Second import *
from Third import *
from Fourth import *
from Fifth import *
from Sixth import *
from Seventh import *

from checkcombobox import *
import datetime
import sqlite3

import os

#MAINPATH = r"D:"
#MAINPATH = os.getcwd()
MAINPATH = r"C:\Users\CheanHui\Desktop"
#MAINPATH = r"\\EDI-PC\Job Search"

class Main:
    def __init__(self):
        self.FirstPage = FirstPage()
        self.SecondPage = SecondPage()
        self.ThirdPage = ThirdPage()
        self.FourthPage = FourthPage()

        self.FirstPage.FirstPageUi.createtask.clicked.connect(self.show_SecondPage)
        #########################
        """
        for i in range(self.FirstPage.FirstPageUi.sort.count()):
            self.FirstPage.FirstPageUi.sort.removeItem(0)
            
        self.FirstPage.FirstPageUi.sort.additem("", False)
        
        for row_item in row_table.keys():
            self.FirstPage.FirstPageUi.sort.additem(row_item, True)
            item = self.FirstPage.FirstPageUi.sort.model().item(self.FirstPage.FirstPageUi.sort.count()-1,0)
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)

            if(row_table[row_item]):
                item.setCheckState(QtCore.Qt.Checked)
        """
        #########################
        
        self.SecondPage.SecondPageUi.back.clicked.connect(self.back_to_firstpage)
        self.SecondPage.SecondPageUi.done.clicked.connect(self.Done2)

        self.ThirdPage.ThirdPageUi.back.clicked.connect(self.back_to_firstpage)
        self.ThirdPage.ThirdPageUi.done.clicked.connect(self.Done3)

        self.FourthPage.FourthPageUi.back.clicked.connect(self.back_to_firstpage)
        self.FourthPage.FourthPageUi.done.clicked.connect(self.Done4)

        #########################
        self.FirstPage.FirstPageUi.edit.clicked.connect( self.FirstPage.editinformation)

    def back_to_firstpage(self):
        if(self.SecondPage.isVisible()):
            buttonReply = QMessageBox.question(self.SecondPage, 'Message !!!', "Want to back?", QMessageBox.Yes | QMessageBox.No)
            if(buttonReply == QMessageBox.Yes):
                self.SecondPage.deleteitems()
                self.SecondPage.close()
                self.FirstPage.FirstPageUi.tableWidget.setRowCount(0)
                self.FirstPage.show()
            
        elif(self.ThirdPage.isVisible()):
            buttonReply = QMessageBox.question(self.ThirdPage, 'Message !!!', "Want to back?", QMessageBox.Yes | QMessageBox.No)
            if(buttonReply == QMessageBox.Yes):
                self.ThirdPage.deleteitems()
                self.ThirdPage.close()
                self.FirstPage.FirstPageUi.tableWidget.setRowCount(0)
                self.FirstPage.show()

        else:
            buttonReply = QMessageBox.question(self.FourthPage, 'Message !!!', "Want to back?", QMessageBox.Yes | QMessageBox.No)
            if(buttonReply == QMessageBox.Yes):
                self.FourthPage.deleteitems()
                self.FourthPage.close()
                self.FirstPage.FirstPageUi.tableWidget.setRowCount(0)
                self.FirstPage.show()

    def show_FirstPage(self):
        self.SecondPage.SecondPageUi.transfer.setCurrentIndex(0)

        self.SecondPage.close()
        self.ThirdPage.close()
        self.FourthPage.close()
        self.FirstPage.show()

    def show_SecondPage(self):
        self.SecondPage.SecondPageUi.transfer.setCurrentIndex(0)
        
        self.FirstPage.close()
        self.ThirdPage.close()
        self.FourthPage.close()
        self.SecondPage.show()

    def show_ThirdPage(self):
        self.FirstPage.close()
        self.SecondPage.close()
        self.FourthPage.close()
        self.ThirdPage.show()

    def show_FourthPage(self):
        self.SecondPage.close()
        self.ThirdPage.close()
        self.FourthPage.close()
        self.ThirdPage.show()

    def Done2(self):
        if(self.SecondPage.SecondPageUi.transfer.currentText() == "SI"):
            self.SecondPage.SecondPageUi.transfer.setCurrentIndex(0)
            self.SecondPage.donetoupload = True
            QMessageBox.about(self.SecondPage, "Message!!!", "Insert Sea Import Task" )
        elif(self.SecondPage.SecondPageUi.transfer.currentText() == "SE"):
            self.SecondPage.SecondPageUi.transfer.setCurrentIndex(1)
            self.SecondPage.donetoupload = True
            QMessageBox.about(self.SecondPage, "Message!!!", "Insert Sea Export Task")
        elif(self.SecondPage.SecondPageUi.transfer.currentText() == "AI"):
            self.ThirdPage.ThirdPageUi.transfer.setCurrentIndex(2)
            self.SecondPage.close()
            self.SecondPage.deleteitems()
            self.ThirdPage.show()
            self.ThirdPage.donetoupload = True
            QMessageBox.about(self.ThirdPage, "Message!!!", "Insert Air Import Task")
        elif(self.SecondPage.SecondPageUi.transfer.currentText() == "AE"):
            self.ThirdPage.ThirdPageUi.transfer.setCurrentIndex(3)
            self.SecondPage.close()
            self.SecondPage.deleteitems()
            self.ThirdPage.show()
            self.ThirdPage.donetoupload = True
            QMessageBox.about(self.ThirdPage, "Message!!!", "Insert Air Export Task")
        else:
            self.FourthPage.FourthPageUi.transfer.setCurrentIndex(4)
            self.SecondPage.close()
            self.SecondPage.deleteitems()
            self.FourthPage.show()
            self.FourthPage.donetoupload = True
            QMessageBox.about(self.FourthPage, "Message!!!", "Insert Truck Task")

    def Done3(self):
        if(self.ThirdPage.ThirdPageUi.transfer.currentText() == "SI"):
            self.SecondPage.SecondPageUi.transfer.setCurrentIndex(0)
            self.ThirdPage.close()
            self.ThirdPage.deleteitems()
            self.SecondPage.show()
            self.SecondPage.donetoupload = True
            QMessageBox.about(self.SecondPage, "Message!!!", "Insert Sea Import Task")
        elif(self.ThirdPage.ThirdPageUi.transfer.currentText() == "SE"):
            self.SecondPage.SecondPageUi.transfer.setCurrentIndex(1)
            self.ThirdPage.close()
            self.ThirdPage.deleteitems()
            self.SecondPage.show()
            self.SecondPage.donetoupload = True
            QMessageBox.about(self.SecondPage, "Message!!!", "Insert Sea Export Task")
        elif(self.ThirdPage.ThirdPageUi.transfer.currentText() == "AI"):
            self.ThirdPage.ThirdPageUi.transfer.setCurrentIndex(2)
            self.ThirdPage.donetoupload = True
            QMessageBox.about(self.ThirdPage, "Message!!!", "Insert Air Import Task")
        elif(self.ThirdPage.ThirdPageUi.transfer.currentText() == "AE"):
            self.ThirdPage.ThirdPageUi.transfer.setCurrentIndex(3)
            self.ThirdPage.donetoupload = True
            QMessageBox.about(self.ThirdPage, "Message!!!", "Insert Air Export Task")
        else:
            self.FourthPage.FourthPageUi.transfer.setCurrentIndex(4)
            self.ThirdPage.close()
            self.ThirdPage.deleteitems()
            self.FourthPage.show()
            self.FourthPage.donetoupload = True
            QMessageBox.about(self.FourthPage, "Message!!!", "Insert Truck Task")
            
    def Done4(self):
        if(self.FourthPage.FourthPageUi.transfer.currentText() == "SI"):
            self.SecondPage.SecondPageUi.transfer.setCurrentIndex(0)
            self.FourthPage.close()
            self.FourthPage.deleteitems()
            self.SecondPage.show()
            self.SecondPage.donetoupload = True
            QMessageBox.about(self.SecondPage, "Message!!!", "Insert Sea Import Task")
        elif(self.FourthPage.FourthPageUi.transfer.currentText() == "SE"):
            self.SecondPage.SecondPageUi.transfer.setCurrentIndex(1)
            self.FourthPage.close()
            self.FourthPage.deleteitems()
            self.SecondPage.show()
            self.SecondPage.donetoupload = True
            QMessageBox.about(self.SecondPage, "Message!!!", "Insert Sea Export Task")
        elif(self.FourthPage.FourthPageUi.transfer.currentText() == "AI"):
            self.ThirdPage.ThirdPageUi.transfer.setCurrentIndex(2)
            self.FourthPage.close()
            self.FourthPage.deleteitems()
            self.ThirdPage.show()
            self.ThirdPage.donetoupload = True
            QMessageBox.about(self.ThirdPage, "Message!!!", "Insert Air Import Task")
        elif(self.FourthPage.FourthPageUi.transfer.currentText() == "AE"):
            self.ThirdPage.ThirdPageUi.transfer.setCurrentIndex(3)
            self.FourthPage.close()
            self.FourthPage.deleteitems()
            self.ThirdPage.show()
            self.ThirdPage.donetoupload = True
            QMessageBox.about(self.ThirdPage, "Message!!!", "Insert Air Export Task")
        else:
            self.FourthPage.FourthPageUi.transfer.setCurrentIndex(4)
            self.FourthPage.donetoupload = True
            QMessageBox.about(self.FourthPage, "Message!!!", "Insert Truck Task")

class FirstPage(QMainWindow):
    def __init__(self):
        super().__init__()
        #super().setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.FirstPageUi =  FirstMainWindow()
        self.FirstPageUi.first_setupUi(self)
        self.secondpage = SecondPage()
        #booking combo box
        self.FirstPageUi.bookingNo.addItem("Job File No", True)
        self.FirstPageUi.bookingNo.addItem("JJ No", True)
        self.FirstPageUi.bookingNo.addItem("Sea/Truck Booking No", True)
        self.FirstPageUi.bookingNo.addItem("Container No", True)
        self.FirstPageUi.bookingNo.addItem("Sea BL No", True)
        self.FirstPageUi.bookingNo.addItem("AWB No", True)
        #sort button
        #self.FirstPageUi.sort.additem("SORT", True)
        #done button
        self.FirstPageUi.done.clicked.connect(self.doneclick)
        #table widget
        self.FirstPageUi.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.FirstPageUi.tableWidget.cellClicked.connect(self.singleclick)
        self.FirstPageUi.tableWidget.cellDoubleClicked.connect(self.doubleclick)
        #all button
        self.FirstPageUi.all.clicked.connect(self.allinformation)
        #numberofcolumn for database
        self.num_column = 0
        #data for seadatabase, airdatabase, truckdatabase
        self.data = []
    
        self.path = MAINPATH + "\ ".strip() + "Job Database"
        if not os.path.exists(self.path):
            os.mkdir(self.path)
            
        ###resize###
        self.FirstPageUi.createtask.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        ###resize###
        ###edit###
        self.allrow = 0
        self.FifthPage = FifthPage()
        self.SixthPage = SixthPage()
        self.SeventhPage = SeventhPage()
        ###edit###
        ###back###
        self.FifthPage.FifthPageUi.back.clicked.connect(self.back_to_firstpage)
        self.FifthPage.FifthPageUi.deleteall.clicked.connect(self.fifthdeleteall)
        
        self.SixthPage.SixthPageUi.back.clicked.connect(self.back_to_firstpage)
        self.SixthPage.SixthPageUi.deleteall.clicked.connect(self.sixthdeleteall)
        
        self.SeventhPage.SeventhPageUi.back.clicked.connect(self.back_to_firstpage)
        self.SeventhPage.SeventhPageUi.deleteall.clicked.connect(self.seventhdeleteall)
        ###back###
        ###header###
        self.FirstPageUi.tableWidget.horizontalHeader().sectionClicked.connect(self.allsortinformation)
        self.sortinformation = "YEAR DESC,MONTH DESC,DAY DESC,JOB_NUMBER ASC"
        ###########
        self.openalldatabase()
        ###########
        self.done = False
        ###########
        self.clip = QtWidgets.QApplication.clipboard()
        self.show()

        self.changeText(0)
        self.FirstPageUi.bookingNo.currentIndexChanged.connect(self.changeText)

    def changeText(self, index):
        booking_Number = self.FirstPageUi.bookingNo.currentText()

        pathtransfer = MAINPATH +"\ ".strip()+ "Job Database" +"\ ".strip() + "database.db"
        conn = sqlite3.connect(pathtransfer)
        c = conn.cursor()

        data = []

        
        if(booking_Number == "Job File No"):
            c.execute('SELECT Job_File_No FROM database')
            data = data + c.fetchall()
                
        if(booking_Number == "JJ No"):
            c.execute('SELECT JJ_No FROM database')
            data = data + c.fetchall()
                
        if(booking_Number == "Sea/Truck Booking No"):
            c.execute('SELECT Booking_No_Sea FROM database')
            data = data + c.fetchall()

        if(booking_Number == "Sea/Truck Booking No"):
            c.execute('SELECT Booking_No_Truck No FROM database')
            data = data + c.fetchall()

        if(booking_Number == "Container No"):
            c.execute('SELECT CONTAINER_NO FROM database')
            data = data + c.fetchall()

        if(booking_Number == "Sea BL No"):
            c.execute('SELECT BL FROM database')
            data = data + c.fetchall()

        if(booking_Number == "AWB No"):
            c.execute('SELECT AWB No FROM database')
            data = data + c.fetchall()

        DATA = []
        for d in data:
            DATA.append(d[0])

        #DATA.sort()
        
        completer = QCompleter(DATA, self.FirstPageUi.lineEdit)
        self.FirstPageUi.lineEdit.setCompleter(completer)
        

    def allsortinformation(self, column):
        p = self.path+"\ ".strip()+"database.db"
        conn = sqlite3.connect(p)
        c = conn.cursor()
        
        if(self.done == True):
            access = {0:"Job_File_No",1:"JJ_No",2:"Shipper",3:"Consignee",4:"Booking_No_Sea",5:"AWB",6:"Booking_No_Truck",7:"BL",8:"ORIGIN",
                  9:"DESTINATION",10:"CONTAINER_NO",11:"Transfer"}

            c.execute("SELECT * FROM database ORDER BY " + access[column])
            data = c.fetchall()

            ACCESS = ["Job File No","JJ No","Shipper","Consignee","Sea Booking No","Air AWB","Truck Booking No","Sea BL No ","Origin",
                      "Destination","Container No","Transport"]

            self.FirstPageUi.tableWidget.setColumnCount(len(ACCESS))
            self.FirstPageUi.tableWidget.setRowCount(len(data))
            self.FirstPageUi.tableWidget.setHorizontalHeaderLabels(ACCESS)


            for i in range(len(data)):
                for j in range(11):
                    self.FirstPageUi.tableWidget.setItem(i,j, QTableWidgetItem(data[i][j]))
                    self.FirstPageUi.tableWidget.setItem(i, 11, QTableWidgetItem(data[i][15]))
                    
            self.data = data
            
        else:
            transfer = self.FirstPageUi.transfer.currentText()
            DATA = None
            
            if(self.FirstPageUi.tableWidget.columnCount() == 10):
                access1 = {0:"Job_File_No",1:"JJ_No",2:"Shipper",3:"Consignee",4:"Booking_No_Sea",5:"BL",6:"ORIGIN",
                  7:"DESTINATION",8:"CONTAINER_NO",9:"Transfer"}
                Access1 = ["Job File No","JJ No","Shipper","Consignee","Sea Booking No","Sea BL No","Origin",
                  "Destination","Container No","Transport"]
                data_col1 = access1[column]
                
                if(transfer == "SI"):
                    c.execute("SELECT * FROM database WHERE Transfer='SI' ORDER BY " + data_col1
                              + " ASC,YEAR DESC,MONTH DESC,DAY DESC,JOB_NUMBER ASC")
                    DATA = c.fetchall()
                else:
                    c.execute("SELECT * FROM database WHERE Transfer='SE' ORDER BY " + data_col1
                              + " ASC,YEAR DESC,MONTH DESC,DAY DESC,JOB_NUMBER ASC")
                    DATA = c.fetchall()
               
                self.FirstPageUi.tableWidget.setColumnCount(len(access1))
                self.FirstPageUi.tableWidget.setRowCount(len(DATA))
                self.FirstPageUi.tableWidget.setHorizontalHeaderLabels(Access1)
                

                for i in range(len(DATA)):
                    for j in range(5):
                        self.FirstPageUi.tableWidget.setItem(i,j, QTableWidgetItem(DATA[i][j]))
                    
                    self.FirstPageUi.tableWidget.setItem(i, 5, QTableWidgetItem(DATA[i][7]))
                    self.FirstPageUi.tableWidget.setItem(i, 6, QTableWidgetItem(DATA[i][8]))
                    self.FirstPageUi.tableWidget.setItem(i, 7, QTableWidgetItem(DATA[i][9]))
                    self.FirstPageUi.tableWidget.setItem(i, 8, QTableWidgetItem(DATA[i][10]))
                    self.FirstPageUi.tableWidget.setItem(i, 9, QTableWidgetItem(transfer))

                self.data = DATA
                
                    
            elif(self.FirstPageUi.tableWidget.columnCount() == 8):
                access2 = {0:"Job_File_No",1:"JJ_No",2:"Shipper",3:"Consignee",4:"AWB",5:"ORIGIN",6:"DESTINATION",7:"Transfer"}
                Access2 = ["Job File No","JJ No","Shipper","Consignee","Air AWB","Origin","Destination","Transport"]
                data_col2 = access2[column]

                if(transfer == "AI"):
                    c.execute("SELECT * FROM database WHERE Transfer='AI' ORDER BY " + data_col2
                              + " ASC,YEAR DESC,MONTH DESC,DAY DESC,JOB_NUMBER ASC")
                    DATA = c.fetchall()
                else:
                    c.execute("SELECT * FROM database WHERE Transfer='AE' ORDER BY " + data_col2)
                    DATA = c.fetchall()

                self.FirstPageUi.tableWidget.setColumnCount(len(access2))
                self.FirstPageUi.tableWidget.setRowCount(len(DATA))
                self.FirstPageUi.tableWidget.setHorizontalHeaderLabels(Access2)
                

                for i in range(len(DATA)):
                    for j in range(4):
                        self.FirstPageUi.tableWidget.setItem(i,j, QTableWidgetItem(DATA[i][j]))
                    
                        self.FirstPageUi.tableWidget.setItem(i, 4, QTableWidgetItem(DATA[i][5]))
                        self.FirstPageUi.tableWidget.setItem(i, 5, QTableWidgetItem(DATA[i][8]))
                        self.FirstPageUi.tableWidget.setItem(i, 6, QTableWidgetItem(DATA[i][9]))
                        self.FirstPageUi.tableWidget.setItem(i, 7, QTableWidgetItem(transfer))

                self.data = DATA

            else:
                access3 = {0:"Job_File_No",1:"JJ_No",2:"Shipper",3:"Consignee",4:"Booking_No_Truck",5:"ORIGIN",6:"DESTINATION",
                           7:"CONTAINER_NO",8:"Transfer"}
                Access3 = ["Job File No","JJ No","Shipper","Consignee","Truck Booking No","Origin","Destination",
                           "Container No","Transport"]
                data_col3 = access3[column]
                c.execute("SELECT * FROM database WHERE Transfer='TE' ORDER BY " + data_col3)
                DATA = c.fetchall()

                self.FirstPageUi.tableWidget.setColumnCount(len(access3))
                self.FirstPageUi.tableWidget.setRowCount(len(DATA))
                self.FirstPageUi.tableWidget.setHorizontalHeaderLabels(Access3)

                for i in range(len(DATA)):
                    for j in range(4):
                        self.FirstPageUi.tableWidget.setItem(i,j, QTableWidgetItem(DATA[i][j]))
                    
                    self.FirstPageUi.tableWidget.setItem(i, 4, QTableWidgetItem(DATA[i][6]))
                    self.FirstPageUi.tableWidget.setItem(i, 5, QTableWidgetItem(DATA[i][8]))
                    self.FirstPageUi.tableWidget.setItem(i, 6, QTableWidgetItem(DATA[i][9]))
                    self.FirstPageUi.tableWidget.setItem(i, 7, QTableWidgetItem(DATA[i][10]))
                    self.FirstPageUi.tableWidget.setItem(i, 8, QTableWidgetItem(transfer))

                self.data = DATA

        c.close()       
        #self.sortinformation = "YEAR DESC,MONTH DESC,DAY DESC,JOB_NUMBER ASC"
            
    def fifthdeleteall(self):
        self.FirstPageUi.tableWidget.setRowCount(0)
        self.FifthPage.deleteall()
        self.FifthPage.close()
        self.show()

    def sixthdeleteall(self):
        self.FirstPageUi.tableWidget.setRowCount(0)
        self.SixthPage.deleteall()
        self.SixthPage.close()
        self.show()

    def seventhdeleteall(self):
        self.FirstPageUi.tableWidget.setRowCount(0)
        self.SeventhPage.deleteall()
        self.SeventhPage.close()
        self.show()
    
    def back_to_firstpage(self):
        self.FifthPage.close()
        self.SixthPage.close()
        self.SeventhPage.close()

        self.FifthPage.deleteitems()
        self.SixthPage.deleteitems()
        self.SeventhPage.deleteitems()

        self.FirstPageUi.tableWidget.setRowCount(0)

        self.show()

        
    def editinformation(self):
       p = self.path+"\ ".strip()+"database.db"
       conn = sqlite3.connect(p)
       c = conn.cursor()
       
       if(self.done == True and len(self.data) != 0):
            currentdata = self.data[self.allrow]
            transfer = currentdata[15]

            if(transfer == "SI" or transfer == "SE"):
                booking_no_sea = currentdata[4]
                
                c.execute("select * from database where Booking_No_Sea = ?", (booking_no_sea,))
                DATA = c.fetchall()

                c.execute("select rowid from database where Booking_No_Sea = ?", (booking_no_sea,))
                ROWID = c.fetchone()
                ROWID = int(ROWID[0])

                jobfileno = str(DATA[0][0])
                self.FifthPage.FifthPageUi.jobfileno.setText(jobfileno)
                jjno = str(DATA[0][1])
                self.FifthPage.FifthPageUi.jjno.setText(jjno)
                shipper = str(DATA[0][2])
                self.FifthPage.FifthPageUi.shipper.setText(shipper)
                consignee = str(DATA[0][3])
                self.FifthPage.FifthPageUi.consignee.setText(consignee)
                sea_booking_no = str(DATA[0][4])
                self.FifthPage.FifthPageUi.bookingno.setText(sea_booking_no)
                bl = str(DATA[0][7])
                self.FifthPage.FifthPageUi.bl_alb.setText(bl)
                origin = str(DATA[0][8])
                self.FifthPage.FifthPageUi.origin.setText(origin)
                destination = str(DATA[0][9])
                self.FifthPage.FifthPageUi.destination.setText(destination)
                
                self.FifthPage.sea_booking_no = sea_booking_no
                
                self.FifthPage.year = DATA[0][11]
                self.FifthPage.month = DATA[0][12]
                self.FifthPage.day = DATA[0][13]
                self.FifthPage.job_no = DATA[0][14]
                self.FifthPage.transfer = DATA[0][15]

                self.FifthPage.allcontainerdata = []
                self.FifthPage.FifthPageUi.listWidget.clear()
                for i in range(len(DATA)):
                    container_no = str(DATA[i][10])
                    self.FifthPage.FifthPageUi.listWidget.addItem(container_no)
                    self.FifthPage.allcontainerdata.append(ROWID)
                    ROWID = ROWID + 1

                #self.FifthPage.allowdelete = True
                self.close()
                self.FifthPage.show()
                
                c.close()

            elif(transfer == "AI" or transfer == "AE"):
                awb = currentdata[5]

                c.execute("select * from database where AWB = ?", (awb,))
                DATA = c.fetchall()

                c.execute("select rowid from database where AWB = ?", (awb,))
                ROWID = c.fetchone()
                ROWID = int(ROWID[0])
                #self.SixthPage.rowdata.append(ROWID)
                #########################################
                jobfileno = str(DATA[0][0])
                self.SixthPage.SixthPageUi.jobfileno.setText(jobfileno)
                jjno = str(DATA[0][1])
                self.SixthPage.SixthPageUi.jjno.setText(jjno)
                shipper = str(DATA[0][2])
                self.SixthPage.SixthPageUi.shipper.setText(shipper)
                consignee = str(DATA[0][3])
                self.SixthPage.SixthPageUi.consignee.setText(consignee)
                awb = str(DATA[0][5])
                self.SixthPage.SixthPageUi.awb.setText(awb)
                origin = str(DATA[0][8])
                self.SixthPage.SixthPageUi.origin.setText(origin)
                destination = str(DATA[0][9])
                self.SixthPage.SixthPageUi.destination.setText(destination)
                #########################################
                self.SixthPage.awb = awb

                self.SixthPage.year = DATA[0][11]
                self.SixthPage.month = DATA[0][12]
                self.SixthPage.day = DATA[0][13]
                self.SixthPage.job_no = DATA[0][14]
                self.SixthPage.transfer = DATA[0][15]
                ########################################
                #self.SixthPage.allowdelete = True
                ########################################
                self.close()
                self.SixthPage.show()
                c.close()
                
            else:
                
                booking_no_truck = currentdata[6]

                c.execute("select * from database where Booking_No_Truck = ?", (booking_no_truck,))
                DATA = c.fetchall()

                c.execute("select rowid from database where Booking_No_Truck = ?", (booking_no_truck,))
                ROWID = c.fetchone()
                ROWID = int(ROWID[0])

                
                ########################################
                jobfileno = str(DATA[0][0])
                self.SeventhPage.SeventhPageUi.jobfileno.setText(jobfileno)
                jjno = str(DATA[0][1])
                self.SeventhPage.SeventhPageUi.jjno.setText(jjno)
                shipper = str(DATA[0][2])
                self.SeventhPage.SeventhPageUi.shipper.setText(shipper)
                consignee = str(DATA[0][3])
                self.SeventhPage.SeventhPageUi.consignee.setText(consignee)
                truck_booking_no  = str(DATA[0][6])
                self.SeventhPage.SeventhPageUi.bookingno.setText(truck_booking_no)
                origin = str(DATA[0][8])
                self.SeventhPage.SeventhPageUi.origin.setText(origin)
                destination = str(DATA[0][9])
                self.SeventhPage.SeventhPageUi.destination.setText(destination)
                ########################################
                self.SeventhPage.truck_booking_no = truck_booking_no

                self.SeventhPage.year = DATA[0][11]
                self.SeventhPage.month = DATA[0][12]
                self.SeventhPage.day = DATA[0][13]
                self.SeventhPage.job_no = DATA[0][14]
                self.SeventhPage.transfer = DATA[0][15]
                
                self.SeventhPage.allcontainerdata = []
                self.SeventhPage.SeventhPageUi.listWidget.clear()
                for i in range(len(DATA)):
                    container_no = str(DATA[i][10])
                    self.SeventhPage.SeventhPageUi.listWidget.addItem(container_no)
                    self.SeventhPage.allcontainerdata.append(ROWID)
                    ROWID = ROWID + 1

                ########################################
                self.SeventhPage.allowdelete = True
                ########################################
                self.close()
                self.SeventhPage.show()
                c.close()

       else:
            QMessageBox.about(self, "Messages", "Please press Done for editing !!!")
        
        
    def allinformation(self):
        
        self.done = False
            
        self.openalldatabase()
        
        transfer = self.FirstPageUi.transfer.currentText()
        self.data = []
        
        access1 = ["Job File No","JJ No","Shipper","Consignee","Sea Booking No","Sea BL No","Origin","Destination","Container No","Transport"]
        access2 = ["Job File No","JJ No","Shipper","Consignee","Air AWB","Origin","Destination","Transport"]
        access3 = ["Job File No","JJ No","Shipper","Consignee","Truck Booking No","Origin","Destination","Container No","Transport"]
        
        data = []
        if(transfer == "SI" or transfer == "SE"):
            pathtransfer = MAINPATH +"\ ".strip()+ "Job Database" +"\ ".strip() + "database.db"
            conn = sqlite3.connect(pathtransfer)
            c = conn.cursor()

            if(transfer == "SI"):
                c.execute("SELECT * FROM database WHERE Transfer='SI' ORDER BY " + self.sortinformation)
            else:
                c.execute("SELECT * FROM database WHERE Transfer='SE' ORDER BY " + self.sortinformation)
            

            data = c.fetchall()
            self.data = data
            
            self.FirstPageUi.tableWidget.setColumnCount(len(access1))
            self.FirstPageUi.tableWidget.setRowCount(len(data))
            self.FirstPageUi.tableWidget.setHorizontalHeaderLabels(access1)

            
            for i in range(len(data)):
                for j in range(5):
                    self.FirstPageUi.tableWidget.setItem(i,j, QTableWidgetItem(data[i][j]))
                    
                self.FirstPageUi.tableWidget.setItem(i, 5, QTableWidgetItem(data[i][7]))
                self.FirstPageUi.tableWidget.setItem(i, 6, QTableWidgetItem(data[i][8]))
                self.FirstPageUi.tableWidget.setItem(i, 7, QTableWidgetItem(data[i][9]))
                self.FirstPageUi.tableWidget.setItem(i, 8, QTableWidgetItem(data[i][10]))
                self.FirstPageUi.tableWidget.setItem(i, 9, QTableWidgetItem(transfer))
            
            c.close()
            
        elif(transfer == "AI" or transfer == "AE"):
            pathtransfer = MAINPATH +"\ ".strip()+ "Job Database" +"\ ".strip() + "database.db"
            conn = sqlite3.connect(pathtransfer)
            c = conn.cursor()

            if(transfer == "AI"):
                c.execute(" SELECT * FROM database WHERE Transfer='AI' ORDER BY " + self.sortinformation)    
            else:
                c.execute(" SELECT * FROM database WHERE Transfer='AE' ORDER BY " + self.sortinformation)
               
            data = c.fetchall()
            self.data = data
             
            self.FirstPageUi.tableWidget.setColumnCount(len(access2))
            self.FirstPageUi.tableWidget.setRowCount(len(data))
            self.FirstPageUi.tableWidget.setHorizontalHeaderLabels(access2)

            for i in range(len(data)):
                for j in range(4):
                    self.FirstPageUi.tableWidget.setItem(i,j, QTableWidgetItem(data[i][j]))
                    
                self.FirstPageUi.tableWidget.setItem(i, 4, QTableWidgetItem(data[i][5]))
                self.FirstPageUi.tableWidget.setItem(i, 5, QTableWidgetItem(data[i][8]))
                self.FirstPageUi.tableWidget.setItem(i, 6, QTableWidgetItem(data[i][9]))
                self.FirstPageUi.tableWidget.setItem(i, 7, QTableWidgetItem(transfer))
                
            c.close()
            
        else:
            pathtransfer = MAINPATH +"\ ".strip()+ "Job Database" +"\ ".strip() + "database.db"
            conn = sqlite3.connect(pathtransfer)
            c = conn.cursor()

            if(self.sortinformation == "YEAR DESC,MONTH DESC,DAY DESC,JOB_NUMBER ASC"):
                c.execute(" SELECT * FROM database WHERE Transfer='TE' ORDER BY " + self.sortinformation)
            else:
                c.execute(" SELECT * FROM database WHERE Transfer='TE' ORDER BY " + self.sortinformation + ",YEAR DESC,MONTH DESC,DAY DESC,JOB_NUMBER ASC")

            data = c.fetchall()
            self.data = data

            self.FirstPageUi.tableWidget.setColumnCount(len(access3))
            self.FirstPageUi.tableWidget.setRowCount(len(data))
            self.FirstPageUi.tableWidget.setHorizontalHeaderLabels(access3)

        
            for i in range(len(data)):
                for j in range(4):
                    self.FirstPageUi.tableWidget.setItem(i,j, QTableWidgetItem(data[i][j]))
                    
                self.FirstPageUi.tableWidget.setItem(i, 4, QTableWidgetItem(data[i][6]))
                self.FirstPageUi.tableWidget.setItem(i, 5, QTableWidgetItem(data[i][8]))
                self.FirstPageUi.tableWidget.setItem(i, 6, QTableWidgetItem(data[i][9]))
                self.FirstPageUi.tableWidget.setItem(i, 7, QTableWidgetItem(data[i][10]))
                self.FirstPageUi.tableWidget.setItem(i, 8, QTableWidgetItem(transfer))
                
            c.close()

        self.sortinformation = "YEAR DESC,MONTH DESC,DAY DESC,JOB_NUMBER ASC"

        
    def openalldatabase(self):
        conn = sqlite3.connect(MAINPATH +"\ ".strip()+ "Job Database" +"\ ".strip() + "database.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS database"+
              "(Job_File_No TEXT, JJ_No TEXT, Shipper TEXT, Consignee TEXT,Booking_No_Sea TEXT, AWB TEXT, Booking_No_Truck TEXT, BL TEXT , ORIGIN TEXT, DESTINATION TEXT, CONTAINER_NO TEXT,"+
              "YEAR TEXT, MONTH TEXT, DAY TEXT, JOB_NUMBER TEXT, Transfer TEXT)")
        c.close()

    def keyPressEvent(self, e):
        if (e.modifiers() & QtCore.Qt.ControlModifier):
            selected = self.FirstPageUi.tableWidget.selectedRanges()

            
            if e.key() == QtCore.Qt.Key_V:
                print("hdhgfhf")
                first_row = selected[0].topRow()
                first_col = selected[0].leftColumn()

                for r, row in enumerate(self.clip.text().split('\n')):
                    for c, text in enumerate(row.split('\t')):
                        self.table.setItem(first_row+r, first_col+c, QtGui.QTableWidgetItem(text))

            elif e.key() == QtCore.Qt.Key_C:
                f = open("note.txt","w+")

                s = ""
                for r in range(selected[0].topRow(),selected[0].bottomRow()+1):
                    for c in range(selected[0].leftColumn(),selected[0].rightColumn()+1):
                        f.write(self.data[r][c])
                        f.write("\n")

                        s = s + self.data[r][c]
                        s = s + "\n"


                self.clip.setText(s)
                os.startfile('note.txt')
                f.close() 

    def doneclick(self):
        self.done = True
        self.changeText(0)
        if (len(self.FirstPageUi.lineEdit.text()) == 0):
            access = ["Job File No","JJ No","Shipper","Consignee","Sea Booking No","AWB","Truck Booking No","Sea BL No","Origin",
                      "Destination","Container No","Transport"]

            pathtransfer = MAINPATH +"\ ".strip()+ "Job Database" +"\ ".strip() + "database.db"
            conn = sqlite3.connect(pathtransfer)
            c = conn.cursor()
            c.execute(" SELECT * FROM database ORDER BY YEAR DESC,MONTH DESC,DAY DESC,JJ_No ASC")
            data = c.fetchall()

            self.FirstPageUi.tableWidget.setColumnCount(len(access))
            self.FirstPageUi.tableWidget.setRowCount(len(data))
            self.FirstPageUi.tableWidget.setHorizontalHeaderLabels(access)

            for i in range(len(data)):
                for j in range(11):
                    self.FirstPageUi.tableWidget.setItem(i,j, QTableWidgetItem(data[i][j]))
                    self.FirstPageUi.tableWidget.setItem(i,11, QTableWidgetItem(data[i][15]))

            c.close()
            self.data = data
        else:
            access = ["Job File No","JJ No","Shipper","Consignee","Sea Booking No","AWB","Truck Booking No","Sea BL No","Origin",
                      "Destination","Container No","Transport"]

            booking_Number = self.FirstPageUi.bookingNo.currentText()
            booking_Text = self.FirstPageUi.lineEdit.text()

            pathtransfer = MAINPATH +"\ ".strip()+ "Job Database" +"\ ".strip() + "database.db"
            conn = sqlite3.connect(pathtransfer)
            c = conn.cursor()

            get_all_data = []

            if(booking_Number == "Job File No"):
                c.execute('SELECT * FROM database WHERE Job_File_No=?', (booking_Text,))
                data = c.fetchall()
                get_all_data =  get_all_data + data
                
            if(booking_Number == "JJ No"):
                c.execute('SELECT * FROM database WHERE JJ_No=?', (booking_Text,))
                data = c.fetchall()
                get_all_data =  get_all_data + data
                
            if(booking_Number == "Sea/Truck Booking No"):
                c.execute('SELECT * FROM database WHERE Booking_No_Sea=?', (booking_Text,))
                data = c.fetchall()
                get_all_data =  get_all_data + data

            if(booking_Number == "Sea/Truck Booking No"):
                c.execute('SELECT * FROM database WHERE Booking_No_Truck=?', (booking_Text,))
                data = c.fetchall()
                get_all_data =  get_all_data + data

            if(booking_Number == "Container No"):
                c.execute('SELECT * FROM database WHERE CONTAINER_No=?', (booking_Text,))
                data = c.fetchall()
                get_all_data =  get_all_data + data

            if(booking_Number == "Sea BL No"):
                c.execute('SELECT * FROM database WHERE BL=?', (booking_Text,))
                data = c.fetchall()
                get_all_data =  get_all_data + data

            if(booking_Number == "AWB No"):
                c.execute('SELECT * FROM database WHERE AWB=?', (booking_Text,))
                data = c.fetchall()
                get_all_data =  get_all_data + data

           
            self.FirstPageUi.tableWidget.setColumnCount(len(access))
            self.FirstPageUi.tableWidget.setRowCount(len(get_all_data))
            self.FirstPageUi.tableWidget.setHorizontalHeaderLabels(access)

            
            for i in range(len(get_all_data)):
                for j in range(11):
                    self.FirstPageUi.tableWidget.setItem(i,j, QTableWidgetItem(get_all_data[i][j]))
                    self.FirstPageUi.tableWidget.setItem(i,11, QTableWidgetItem(get_all_data[i][15]))
                    
            c.close()
            self.data = get_all_data

            if(len(get_all_data) == 0):
                QMessageBox.about(self, "Messages", booking_Number + " = " + booking_Text + " not existed !!!")

        #self.FirstPageUi.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        

    def singleclick(self, row, column):
        self.FirstPageUi.tableWidget.selectRow(row)
        self.allrow = row

    def doubleclick(self, row, column):
        
        if(self.data[row][15] == "SI" or self.data[row][15] == "SE"):
            os.startfile(self.path+"\ ".strip()+self.data[row][11]+"\ ".strip()+self.data[row][12]+
                             "\ ".strip()+self.data[row][13]+"\ ".strip()+"sea"+ "\ ".strip()+self.data[row][14])
        elif(self.data[row][15] == "AI" or self.data[row][15] == "AE"):
            os.startfile(self.path+"\ ".strip()+self.data[row][11]+"\ ".strip()+self.data[row][12]+
                             "\ ".strip()+self.data[row][13]+"\ ".strip()+"air"+ "\ ".strip()+self.data[row][14])
        else:
            os.startfile(self.path+"\ ".strip()+self.data[row][11]+"\ ".strip()+self.data[row][12]+
                             "\ ".strip()+self.data[row][13]+"\ ".strip()+"truck"+ "\ ".strip()+self.data[row][14])
       
        
class SecondPage(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.SecondPageUi = SecondMainWindow()
        self.SecondPageUi.second_setupUi(self)

        self.SecondPageUi.add.clicked.connect(self.addlist)
        self.SecondPageUi.edit.clicked.connect(self.editlist)
        self.SecondPageUi.delete_.clicked.connect(self.delitem)
        self.SecondPageUi.deleteall.clicked.connect(self.deleteitems)
        self.SecondPageUi.upload.clicked.connect(self.upload)
        
        find = False
        for i in os.listdir(MAINPATH):
            if("Job Database" in i):
                find = True
                
        if(find == False):
            os.mkdir(MAINPATH + "\ ".strip() + "Job Database")
            
        self.path = MAINPATH + "\ ".strip() + "Job Database"

        self.donetoupload = True

    def upload(self):
        transfer = str(self.SecondPageUi.transfer.currentText())
        
        if((transfer == "SI" or transfer == "SE") and self.donetoupload == True):
            
            year = int(str(datetime.datetime.now())[0:4])
            month = int(str(datetime.datetime.now())[5:7])
            day = int(str(datetime.datetime.now())[8:10])
            ##########################
            find_year = False
            cur_find_year = self.path + "\ ".strip() + str(year)
    
            for x in os.walk(self.path):
                if(cur_find_year == x[0]):
                    find_year = True

            if(find_year == False):
                os.mkdir(cur_find_year)
            ##########################
            find_month = False
            cur_find_month = cur_find_year + "\ ".strip() + str(month)
            
            for x in os.walk(cur_find_year):
                if(cur_find_month == x[0]):
                    find_month = True

            if(find_month == False):
                os.mkdir(cur_find_month)
            ##########################
            find_day = False
            cur_find_day = cur_find_month + "\ ".strip() + str(day)
            for x in os.walk(cur_find_day):
                if(cur_find_day == x[0]):
                    find_day = True
            if(find_day == False):
                os.mkdir(cur_find_day)

            
            cur_find_day = cur_find_day + "\ ".strip() + "sea"
            if not os.path.exists(cur_find_day):
                os.mkdir(cur_find_day)

            ##########################
            #creating database for ship if not exists
            conn = sqlite3.connect(self.path+ "\ ".strip() +"database.db")
            c = conn.cursor()

            jobfileno = str(self.SecondPageUi.jobfileno.text())
            jjno = str(self.SecondPageUi.jjno.text())
            shipper = str(self.SecondPageUi.shipper.text())
            consignee = str(self.SecondPageUi.consignee.text())
            bookingno = str(self.SecondPageUi.bookingno.text())
            bl_alb = str(self.SecondPageUi.bl_alb.text())
            origin = str(self.SecondPageUi.origin.text())
            destination = str(self.SecondPageUi.destination.text())

            upload = True
            if(len(jobfileno)==0 or len(jjno)==0 or len(shipper)==0 or len(consignee)==0 or len(bookingno)==0 or len(bl_alb)==0
               or len(origin)==0 or len(destination)==0 or self.SecondPageUi.listWidget.count()==0):
               buttonReply = QMessageBox.question(self, 'Message !!!', "Form is not completed! Want to upload?", QMessageBox.Yes | QMessageBox.No)
               if buttonReply == QMessageBox.No:
                   upload = False
               if(len(bookingno)==0):
                   QMessageBox.about(self, "Warning!!!", "Please insert Sea Booking No.")
                   upload = False

            if(upload == True):
                if (len(jobfileno)==0): jobfileno = "-"
                if (len(jjno)==0): jjno = "-"
                if (len(shipper)==0): shipper = "-"
                if (len(consignee)==0): consignee = "-"
                if (len(bl_alb)==0): bl_alb = "-"
                if (len(origin)==0): origin = "-"
                if (len(destination)==0): destination = "-"

                length = len(os.listdir(cur_find_day))
                list_int = [int(i) for i in os.listdir(cur_find_day)]
                list_int.sort()

                jj = 0
                if(len(list_int) == 0):
                    jj = 0
                else:
                    jj = list_int[len(list_int)-1]
                     
                jj = jj + 1
                ##############################

                make = []
                c.execute("select rowid from database where Booking_No_Sea = ?", (bookingno,))
                row = c.fetchone()

                if(row):
                    make.append(False)

                if False not in make:
                    os.mkdir(cur_find_day + "\ ".strip() + str(jj))
                    os.startfile(cur_find_day + "\ ".strip() + str(jj))
                    for i in range(self.SecondPageUi.listWidget.count()):
                        container_no = self.SecondPageUi.listWidget.item(i).text()
                        if (len(container_no)==0): container_no = "-"
                        item = (jobfileno,jjno,shipper,consignee,bookingno,"-","-",bl_alb,origin,destination,container_no,year,month,day,jj,transfer,)
                        c.execute("INSERT INTO database (Job_File_No,JJ_No,Shipper,Consignee,Booking_No_Sea,AWB,Booking_No_Truck,BL,ORIGIN,DESTINATION,CONTAINER_NO,"+
                                  "YEAR,MONTH,DAY,JOB_NUMBER,Transfer) "+
                                  "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", item)
                        conn.commit()
                        
                    if(self.SecondPageUi.listWidget.count() == 0):
                        container_no = "-"
                        item = (jobfileno,jjno,shipper,consignee,bookingno,"-","-",bl_alb,origin,destination,container_no,year,month,day,jj,transfer,)
                        c.execute("INSERT INTO database (Job_File_No,JJ_No,Shipper,Consignee,Booking_No_Sea,AWB,Booking_No_Truck,BL,ORIGIN,DESTINATION,CONTAINER_NO,"+
                                  "YEAR,MONTH,DAY,JOB_NUMBER,Transfer) "+
                                  "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", item)
                        conn.commit()
                else:
                    QMessageBox.about(self, "Warning", "This information already exists!!!")

            
            
                self.donetoupload = False

                c.close()
                conn.close()
        else:
            QMessageBox.about(self, "Warning", "Please press DONE button!!!")
            
        
    def addlist(self):
        if(len(self.SecondPageUi.containerno.text()) != 0):
            self.SecondPageUi.listWidget.addItem(self.SecondPageUi.containerno.text())
            self.SecondPageUi.containerno.clear()
    
    def editlist(self):
        row = self.SecondPageUi.listWidget.currentRow()
        if(str(row) != str(-1)):
            newtext, ok = QInputDialog.getText(self, "Message!!!","Enter new text")

            if ok and (len(newtext) !=0):
                self.SecondPageUi.listWidget.takeItem(self.SecondPageUi.listWidget.currentRow())
                self.SecondPageUi.listWidget.insertItem(row, QListWidgetItem(newtext))

    def delitem(self):
        self.SecondPageUi.listWidget.takeItem(self.SecondPageUi.listWidget.currentRow())

    def deleteitems(self):
        self.SecondPageUi.listWidget.clear()
        self.SecondPageUi.jobfileno.clear()
        self.SecondPageUi.jjno.clear()
        self.SecondPageUi.shipper.clear()
        self.SecondPageUi.consignee.clear()
        self.SecondPageUi.bookingno.clear()
        self.SecondPageUi.bl_alb.clear()
        self.SecondPageUi.origin.clear()
        self.SecondPageUi.destination.clear()
        self.SecondPageUi.containerno.clear()

class ThirdPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ThirdPageUi = ThirdMainWindow()
        self.ThirdPageUi.third_setupUi(self)

        self.ThirdPageUi.upload.clicked.connect(self.upload)
        self.ThirdPageUi.deleteall.clicked.connect(self.deleteitems)
        
        find = False
        for i in os.listdir(MAINPATH):
            if("Job Database" in i):
                find = True
                
        if(find == False):
            os.mkdir(MAINPATH + "\ ".strip() + "Job Database")
            
        self.path = MAINPATH + "\ ".strip() + "Job Database"

        self.donetoupload = True

    def upload(self):
        transfer = self.ThirdPageUi.transfer.currentText()
        if((transfer == "AI" or transfer == "AE") and self.donetoupload == True):
            year = int(str(datetime.datetime.now())[0:4])
            month = int(str(datetime.datetime.now())[5:7])
            day = int(str(datetime.datetime.now())[8:10])
            ##########################
            find_year = False
            cur_find_year = self.path + "\ ".strip() + str(year)
            
            for x in os.walk(self.path):
                if(cur_find_year == x[0]):
                    find_year = True
        
            if(find_year == False):
                os.mkdir(cur_find_year)
        
            ##########################
            find_month = False
            cur_find_month = cur_find_year + "\ ".strip() + str(month)
            
            for x in os.walk(cur_find_year):
                if(cur_find_month == x[0]):
                    find_month = True

            if(find_month == False):
                os.mkdir(cur_find_month)
            ##########################
            find_day = False
            cur_find_day = cur_find_month + "\ ".strip() + str(day)
            for x in os.walk(cur_find_day):
                if(cur_find_day == x[0]):
                    find_day = True
            if(find_day == False):
                os.mkdir(cur_find_day)

            cur_find_day = cur_find_day + "\ ".strip() + "air"
            if not os.path.exists(cur_find_day):
                os.mkdir(cur_find_day)
            ##########################
            
            #creating database for ship if not exists
            conn = sqlite3.connect(self.path+ "\ ".strip() +"database.db")
            c = conn.cursor()

            jobfileno = str(self.ThirdPageUi.jobfileno.text())
            jjno = str(self.ThirdPageUi.jjno.text())
            shipper = str(self.ThirdPageUi.shipper.text())
            consignee = str(self.ThirdPageUi.consignee.text())
            awb = str(self.ThirdPageUi.awb.text())
            origin = str(self.ThirdPageUi.origin.text())
            destination = str(self.ThirdPageUi.destination.text())
            
            ############################
            upload = True
            if(len(jobfileno)==0 or len(jjno)==0 or len(shipper)==0 or len(consignee)==0 or len(awb)==0
               or len(origin)==0 or len(destination)==0):
               buttonReply = QMessageBox.question(self, 'Message !!!', "Form is not completed! Want to upload?", QMessageBox.Yes | QMessageBox.No)
               if buttonReply == QMessageBox.No:
                   upload = False
               if(len(awb)==0):
                   QMessageBox.about(self, "Warning!!!", "Please insert air waybill.")
                   upload = False

            if(upload == True):
                if (len(jobfileno)==0): jobfileno = "-"
                if (len(jjno)==0): jjno = "-"
                if (len(shipper)==0): shipper = "-"
                if (len(consignee)==0): consignee = "-"
                if (len(origin)==0): origin = "-"
                if (len(destination)==0): destination = "-"
                
                length = len(os.listdir(cur_find_day))
                list_int = [int(i) for i in os.listdir(cur_find_day)]
                list_int.sort()

                jj = 0
                if(len(list_int) == 0):
                    jj = 0
                else:
                    jj = list_int[len(list_int)-1]
                     
                jj = jj + 1
                ##############################
                make = []
                
                c.execute("select rowid from database where AWB = ?", (awb,))
                row = c.fetchone()
                
                if(row):
                    make.append(False)

                
                if False not in make:
                    os.mkdir(cur_find_day + "\ ".strip() + str(jj))
                    os.startfile(cur_find_day + "\ ".strip() + str(jj))
                    
                    item = (jobfileno,jjno,shipper,consignee,"-",awb,"-","-",origin,destination,"-",year,month,day,jj,transfer,)
                    c.execute("INSERT INTO database (Job_File_No,JJ_No,Shipper,Consignee,Booking_No_Sea,AWB,Booking_No_Truck,BL,ORIGIN,DESTINATION,CONTAINER_NO,"+
                                  "YEAR,MONTH,DAY,JOB_NUMBER,Transfer) "+
                                  "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", item)
                    conn.commit()

                else:
                    QMessageBox.about(self, "Warning", "This information already exists!!!")

                c.close()
                conn.close()
                self.donetoupload = False

        else:
            QMessageBox.about(self, "Warning", "Please press DONE button!!!")
                
    ##########################
    def deleteitems(self):
        self.ThirdPageUi.jobfileno.clear()
        self.ThirdPageUi.jjno.clear()
        self.ThirdPageUi.shipper.clear()
        self.ThirdPageUi.consignee.clear()
        self.ThirdPageUi.awb.clear()
        self.ThirdPageUi.origin.clear()
        self.ThirdPageUi.destination.clear()

class FourthPage(QMainWindow):
    def __init__(self):
        super().__init__()
        #super().setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.FourthPageUi = FourthMainWindow()
        self.FourthPageUi.fourth_setupUi(self)
        find = False
        for i in os.listdir(MAINPATH):
            if("Job Database" in i):
                find = True
        if(find == False):
            os.mkdir(MAINPATH + "\ ".strip() + "Job Database")
            
        self.path = MAINPATH + "\ ".strip() + "Job Database"

        self.FourthPageUi.add.clicked.connect(self.addlist)
        self.FourthPageUi.edit.clicked.connect(self.editlist)
        self.FourthPageUi.delete_.clicked.connect(self.delitem)
        self.FourthPageUi.deleteall.clicked.connect(self.deleteitems)
        self.FourthPageUi.upload.clicked.connect(self.upload)
 
        self.donetoupload = True

    def upload(self):
        transfer = self.FourthPageUi.transfer.currentText()
        if(transfer == "TE" and self.donetoupload == True):
            year = int(str(datetime.datetime.now())[0:4])
            month = int(str(datetime.datetime.now())[5:7])
            day = int(str(datetime.datetime.now())[8:10])
            ##########################
            find_year = False
            cur_find_year = self.path + "\ ".strip() + str(year)
            
            for x in os.walk(self.path):
                if(cur_find_year == x[0]):
                    find_year = True

            if(find_year == False):
                os.mkdir(cur_find_year)
            ##########################
            find_month = False
            cur_find_month = cur_find_year + "\ ".strip() + str(month)
            
            for x in os.walk(cur_find_year):
                if(cur_find_month == x[0]):
                    find_month = True

            if(find_month == False):
                os.mkdir(cur_find_month)
            ##########################
            find_day = False
            cur_find_day = cur_find_month + "\ ".strip() + str(day)
            for x in os.walk(cur_find_day):
                if(cur_find_day == x[0]):
                    find_day = True
            if(find_day == False):
                os.mkdir(cur_find_day)

            cur_find_day = cur_find_day + "\ ".strip() + "truck"
            if not os.path.exists(cur_find_day):
                os.mkdir(cur_find_day)
            ##########################
            #creating database for ship if not exists
            conn = sqlite3.connect(self.path+ "\ ".strip() +"database.db")
            c = conn.cursor()

            jobfileno = str(self.FourthPageUi.jobfileno.text())
            jjno = str(self.FourthPageUi.jjno.text())
            shipper = str(self.FourthPageUi.shipper.text())
            consignee = str(self.FourthPageUi.consignee.text())
            bookingno = str(self.FourthPageUi.bookingno.text())
            origin = str(self.FourthPageUi.origin.text())
            destination = str(self.FourthPageUi.destination.text())
            ############################
            upload = True
            if(len(jobfileno)==0 or len(jjno)==0 or len(shipper)==0 or len(consignee)==0 or len(bookingno)==0 
               or len(origin)==0 or len(destination)==0 or self.FourthPageUi.listWidget.count()==0):
               buttonReply = QMessageBox.question(self, 'Message !!!', "Form is not completed! Want to upload?", QMessageBox.Yes | QMessageBox.No)
               if buttonReply == QMessageBox.No:
                   upload = False
               if(len(bookingno)==0):
                   QMessageBox.about(self, "Warning!!!", "Please insert Truck Booking No.")
                   upload = False
            
            if(upload == True):
                if (len(jobfileno)==0): jobfileno = "-"
                if (len(jjno)==0): jjno = "-"
                if (len(shipper)==0): shipper = "-"
                if (len(consignee)==0): consignee = "-"
                if (len(origin)==0): origin = "-"
                if (len(destination)==0): destination = "-"
                
                length = len(os.listdir(cur_find_day))
                list_int = [int(i) for i in os.listdir(cur_find_day)]
                list_int.sort()

                jj = 0
                if(len(list_int) == 0):
                    jj = 0
                else:
                    jj = list_int[len(list_int)-1]
                     
                jj = jj + 1
                ##############################
                make = []
                
                c.execute("select rowid from database where Booking_No_Truck = ?", (bookingno,))
                row = c.fetchone()

                if(row):
                    make.append(False)

                if False not in make:
                    os.mkdir(cur_find_day + "\ ".strip() + str(jj))
                    os.startfile(cur_find_day + "\ ".strip() + str(jj))

                    for i in range(self.FourthPageUi.listWidget.count()):
                        container_no = self.FourthPageUi.listWidget.item(i).text()
                        
                        item = (jobfileno,jjno,shipper,consignee,"-","-",bookingno,"-",origin,destination,container_no,year,month,day,jj,transfer,)
                        c.execute("INSERT INTO database (Job_File_No,JJ_No,Shipper,Consignee,Booking_No_Sea,AWB,Booking_No_Truck,BL,ORIGIN,DESTINATION,CONTAINER_NO,"+
                                  "YEAR,MONTH,DAY,JOB_NUMBER,Transfer) "+
                                  "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", item)
                        
                        conn.commit()
                        
                    if(self.FourthPageUi.listWidget.count() == 0):
                        container_no = "-"
                    
                        item = (jobfileno,jjno,shipper,consignee,"-","-",bookingno,"-",origin,destination,container_no,year,month,day,jj,transfer,)
                        c.execute("INSERT INTO database (Job_File_No,JJ_No,Shipper,Consignee,Booking_No_Sea,AWB,Booking_No_Truck,BL,ORIGIN,DESTINATION,CONTAINER_NO,"+
                                  "YEAR,MONTH,DAY,JOB_NUMBER,Transfer) "+
                                  "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", item)
                        conn.commit()
                        
                else:
                    QMessageBox.about(self, "Warning", "This information already exists!!!")


                c.close()
                conn.close()
                self.donetoupload = False
                ###############################
        else:
            QMessageBox.about(self, "Warning", "Please press DONE button!!!")
            
    def addlist(self):
        if(len(self.FourthPageUi.containerno.text()) != 0):
            self.FourthPageUi.listWidget.addItem(self.FourthPageUi.containerno.text())
            self.FourthPageUi.containerno.clear()
    
    def editlist(self):
        row = self.FourthPageUi.listWidget.currentRow()
        if(str(row) != str(-1)):
            newtext, ok = QInputDialog.getText(self, "Message!!!","Enter new text")

            if ok and (len(newtext) !=0):
                self.FourthPageUi.listWidget.takeItem(self.FourthPageUi.listWidget.currentRow())
                self.FourthPageUi.listWidget.insertItem(row, QListWidgetItem(newtext))

    def delitem(self):
        self.FourthPageUi.listWidget.takeItem(self.FourthPageUi.listWidget.currentRow())

    def deleteitems(self):
        self.FourthPageUi.listWidget.clear()
        self.FourthPageUi.jobfileno.clear()
        self.FourthPageUi.jjno.clear()
        self.FourthPageUi.shipper.clear()
        self.FourthPageUi.consignee.clear()
        self.FourthPageUi.bookingno.clear()
        self.FourthPageUi.origin.clear()
        self.FourthPageUi.destination.clear()
        self.FourthPageUi.containerno.clear()

class FifthPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.FifthPageUi = FifthMainWindow()
        self.FifthPageUi.fifth_setupUi(self)

        ############################
        self.sea_booking_no = ""
        self.year = 0
        self.month = 0
        self.day = 0
        self.job_no = 0
        self.transfer = ""

        self.allcontainerdata = []

        ############################
        self.allowdelete = True
        ############################
        self.FifthPageUi.update.clicked.connect(self.update)
        ############################
        self.FifthPageUi.add.clicked.connect(self.addlist)
        self.FifthPageUi.edit.clicked.connect(self.editlist)
        self.FifthPageUi.delete_.clicked.connect(self.delitem)
        ############################
        self.path = MAINPATH + "\ ".strip() + "Job Database"

    def addlist(self):
        if(len(self.FifthPageUi.containerno.text()) != 0):
            self.FifthPageUi.listWidget.addItem(self.FifthPageUi.containerno.text())
            self.FifthPageUi.containerno.clear()
    
    def editlist(self):
        row = self.FifthPageUi.listWidget.currentRow()
        if(str(row) != str(-1)):
            newtext, ok = QInputDialog.getText(self, "Message!!!","Enter new text")

            if ok and (len(newtext) !=0):
                self.FifthPageUi.listWidget.takeItem(self.FifthPageUi.listWidget.currentRow())
                self.FifthPageUi.listWidget.insertItem(row, QListWidgetItem(newtext))

    def delitem(self):
        self.FifthPageUi.listWidget.takeItem(self.FifthPageUi.listWidget.currentRow())
        
    def update(self):
        conn = sqlite3.connect(self.path  + "\ ".strip()+"database.db")
        c = conn.cursor()

        ####################
        cur_find_day = self.path+ "\ ".strip()+str(self.year)+ "\ ".strip()+self.month+ "\ ".strip()+self.day

        jobfileno = str(self.FifthPageUi.jobfileno.text())
        jjno = str(self.FifthPageUi.jjno.text())
        shipper = str(self.FifthPageUi.shipper.text())
        consignee = str(self.FifthPageUi.consignee.text())
        bookingno = str(self.FifthPageUi.bookingno.text())
        bl_alb = str(self.FifthPageUi.bl_alb.text())
        origin = str(self.FifthPageUi.origin.text())
        destination = str(self.FifthPageUi.destination.text())

        upload = True
        if(len(jobfileno)==0 or len(jjno)==0 or len(shipper)==0 or len(consignee)==0 or len(bookingno)==0 or len(bl_alb)==0
            or len(origin)==0 or len(destination)==0 or self.FifthPageUi.listWidget.count()==0):
            buttonReply = QMessageBox.question(self, 'Message !!!', "Form is not completed! Want to upload?", QMessageBox.Yes | QMessageBox.No)
            if buttonReply == QMessageBox.No:
                upload = False
            if(len(bookingno)==0):
                   QMessageBox.about(self, "Warning!!!", "Please insert Sea Booking No")
                   upload = False

        if(upload == True):
            c.execute("delete from database where Booking_No_Sea = ?", (self.sea_booking_no,))
            conn.commit()
            self.sea_booking_no = bookingno

            if (len(jobfileno)==0): jobfileno = "-"
            if (len(jjno)==0): jjno = "-"
            if (len(shipper)==0): shipper = "-"
            if (len(consignee)==0): consignee = "-"
            if (len(bl_alb)==0): bl_alb = "-"
            if (len(origin)==0): origin = "-"
            if (len(destination)==0): destination = "-"
                
            make = []
            c.execute("select rowid from database where Booking_No_Sea = ?", (bookingno,))
            row = c.fetchone()

            if(row):
                make.append(False)
            
            if False not in make:
                for i in range(self.FifthPageUi.listWidget.count()):
                    container_no = self.FifthPageUi.listWidget.item(i).text()
                    item = (jobfileno,jjno,shipper,consignee,bookingno,"-","-",bl_alb,origin,destination,container_no,
                            self.year,self.month,self.day,self.job_no,self.transfer,)
                    c.execute("INSERT INTO database (Job_File_No,JJ_No,Shipper,Consignee,Booking_No_Sea,"+
                              "AWB,Booking_No_Truck,BL,ORIGIN,DESTINATION,CONTAINER_NO,"+
                                "YEAR,MONTH,DAY,JOB_NUMBER,Transfer) "+
                                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", item)
                    conn.commit()

                if(self.FifthPageUi.listWidget.count() == 0):
                    container_no = "-"
                    item = (jobfileno,jjno,shipper,consignee,bookingno,"-","-",bl_alb,origin,destination,container_no,year,month,day,jj,transfer,)
                    c.execute("INSERT INTO database (Job_File_No,JJ_No,Shipper,Consignee,Booking_No_Sea,AWB,Booking_No_Truck,BL,ORIGIN,DESTINATION,CONTAINER_NO,"+
                                "YEAR,MONTH,DAY,JOB_NUMBER,Transfer) "+
                                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", item)
                    conn.commit()
            else:
                QMessageBox.about(self, "Warning", "This information already exists!!!")
        

        os.startfile(cur_find_day + "\ ".strip() + "sea"+ "\ ".strip() + str(self.job_no))
        c.close()
        

    def deleteall(self):
        conn = sqlite3.connect(self.path+ "\ ".strip()+"database.db")
        c = conn.cursor()

        upload = True
        if(self.allowdelete == True):
            buttonReply = QMessageBox.question(self, 'Message !!!', "Are you sure you want to delete this job document?", QMessageBox.Yes | QMessageBox.No)
            if buttonReply == QMessageBox.No:
                upload = False

        if(upload == True and self.allowdelete == True):
            c.execute("select rowid from database where Booking_No_Sea = ? ", (self.sea_booking_no,))
            all_job_no = c.fetchall()

            c.execute("select * from database where Booking_No_Sea = ? ", (self.sea_booking_no,))
            sea_information = c.fetchall()

            p = self.path+ "\ ".strip()+self.year+ "\ ".strip()+self.month+ "\ ".strip()+self.day+ "\ ".strip()+"sea"

            new_sea_information = {}
            if(len(sea_information) != 0 ):
                current = sea_information[0]
                i = 1
                for information in sea_information:
                    if(current[4] == information[4] and current[5] == information[5]):
                        if(i not in new_sea_information):
                            new_sea_information[i] = []
                            new_sea_information[i].append(information)
                        else:
                            new_sea_information[i].append(information)
                    else:
                        i = i + 1
                        if(i not in new_sea_information):
                            new_sea_information[i] = []
                            new_sea_information[i].append(information)
                        else:
                            new_sea_information[i].append(information)

                    current = information


            c.execute("delete from database where Booking_No_Sea = ?", (self.sea_booking_no,))
            conn.commit()
            self.sea_booking_no = ""

            s = self.path+ "\ ".strip()+self.year+ "\ ".strip()+self.month+ "\ ".strip()+self.day+"\ ".strip()+"sea"+"\ ".strip()+self.job_no
            if os.path.exists(s):
                shutil.rmtree(s)
                
            curr = self.path+"\ ".strip()+self.year+"\ ".strip()+self.month+"\ ".strip()+self.day+"\ ".strip()+"sea"+"\ ".strip()
            for folderjobno in os.listdir(p)[int(self.job_no)-1:]:
                c.execute("update database set JOB_NUMBER=? where (YEAR=? AND MONTH=? AND DAY=? AND JOB_NUMBER=? AND AWB=? AND Booking_No_Truck=?)",
                          (str(int(folderjobno)-1),self.year,self.month,self.day,str(int(folderjobno)),"-","-"))


                conn.commit()
                os.rename(curr+folderjobno, curr+str(int(folderjobno)-1))

            buttonReply = QMessageBox.about(self, "Message!!!", "Deleted successfully.")
            self.deleteitems()

            self.allowdelete = True
            
        c.close()
            
    def deleteitems(self):
        self.FifthPageUi.listWidget.clear()
        self.FifthPageUi.jobfileno.clear()
        self.FifthPageUi.jjno.clear()
        self.FifthPageUi.shipper.clear()
        self.FifthPageUi.consignee.clear()
        self.FifthPageUi.bookingno.clear()
        self.FifthPageUi.bl_alb.clear()
        self.FifthPageUi.origin.clear()
        self.FifthPageUi.destination.clear()
        self.FifthPageUi.containerno.clear()

class SixthPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.SixthPageUi = SixthMainWindow()
        self.SixthPageUi.sixth_setupUi(self)

        ############################
        self.awb = ""
        self.year = 0
        self.month = 0
        self.day = 0
        self.job_no = 0
        self.transfer = ""
        
        #self.transfer = 0
        self.rowdata = []
        ############################
        self.allowdelete = True
        ############################
        self.SixthPageUi.update.clicked.connect(self.update)
        ############################
        self.path = MAINPATH + "\ ".strip() + "Job Database"

    def update(self):
        conn = sqlite3.connect(self.path  + "\ ".strip()+"database.db")
        c = conn.cursor()

        ####################
        cur_find_day = self.path+ "\ ".strip()+str(self.year)+ "\ ".strip()+self.month+ "\ ".strip()+self.day
        
        jobfileno = str(self.SixthPageUi.jobfileno.text())
        jjno = str(self.SixthPageUi.jjno.text())
        shipper = str(self.SixthPageUi.shipper.text())
        consignee = str(self.SixthPageUi.consignee.text())
        awb = str(self.SixthPageUi.awb.text())
        origin = str(self.SixthPageUi.origin.text())
        destination = str(self.SixthPageUi.destination.text())

        upload = True
        if(len(jobfileno)==0 or len(jjno)==0 or len(shipper)==0 or len(consignee)==0 or len(awb)==0
               or len(origin)==0 or len(destination)==0):
            buttonReply = QMessageBox.question(self, 'Message !!!', "Form is not completed! Want to upload?", QMessageBox.Yes | QMessageBox.No)
            if buttonReply == QMessageBox.No:
                upload = False
            if(len(awb)==0):
                QMessageBox.about(self, "Warning!!!", "Please insert air waybill.")
                upload = False

        if(upload == True):
            c.execute("delete from database where AWB = ?", (self.awb,))
            conn.commit()
            self.awb = awb
            
            if (len(jobfileno)==0): jobfileno = "-"
            if (len(jjno)==0): jjno = "-"
            if (len(shipper)==0): shipper = "-"
            if (len(consignee)==0): consignee = "-"
            if (len(origin)==0): origin = "-"
            if (len(destination)==0): destination = "-"

            make = []

            c.execute("select rowid from database where AWB = ?", (awb,))
            row = c.fetchone()
                    
            if(row):
                make.append(False)
            
            if False not in make:

                item = (jobfileno,jjno,shipper,consignee,"-",awb,"-","-",origin,destination,"-",
                            self.year,self.month,self.day,self.job_no,self.transfer,)
                c.execute("INSERT INTO database (Job_File_No,JJ_No,Shipper,Consignee,Booking_No_Sea,AWB,Booking_No_Truck,BL,ORIGIN,DESTINATION,CONTAINER_NO,"+
                            "YEAR,MONTH,DAY,JOB_NUMBER,Transfer) "+
                            "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", item)
                    
                conn.commit()
                
            else:
                QMessageBox.about(self, "Warning", "This information already exists!!!")

        os.startfile(cur_find_day + "\ ".strip() + "air"+ "\ ".strip() + str(self.job_no))
        c.close() 

    def deleteall(self):
        conn = sqlite3.connect(self.path+ "\ ".strip()+"database.db")
        c = conn.cursor()

        upload = True
        if(self.allowdelete == True):
            buttonReply = QMessageBox.question(self, 'Message !!!', "Are you sure you want to delete this job document?", QMessageBox.Yes | QMessageBox.No)
            if buttonReply == QMessageBox.No:
                upload = False
                   
        if(upload == True and self.allowdelete == True):

            c.execute("select rowid from database where AWB = ? ", (self.awb,))
            all_job_no = c.fetchall()

            c.execute("select * from database where AWB = ? ", (self.awb,))
            air_information = c.fetchall()

            p = self.path+ "\ ".strip()+self.year+ "\ ".strip()+self.month+ "\ ".strip()+self.day+ "\ ".strip()+"air"

            new_air_information = {}
            if(len(air_information) != 0 ):
                current = air_information[0]
                i = 1
                for information in air_information:
                    if(current[4] == information[4]):
                        if(i not in new_air_information):
                            new_air_information[i] = []
                            new_air_information[i].append(information)
                        else:
                            new_air_information[i].append(information)
                    else:
                        i = i + 1
                        if(i not in new_air_information):
                            new_air_information[i] = []
                            new_air_information[i].append(information)
                        else:
                            new_air_information[i].append(information)

                    current = information

            
            c.execute("delete from database where AWB = ?", (self.awb,))
            conn.commit()
            self.awb = ""

            s = self.path+ "\ ".strip()+self.year+ "\ ".strip()+self.month+ "\ ".strip()+self.day+"\ ".strip()+"air"+"\ ".strip()+self.job_no
            if os.path.exists(s):
                shutil.rmtree(s)
                
            curr = self.path+"\ ".strip()+self.year+"\ ".strip()+self.month+"\ ".strip()+self.day+"\ ".strip()+"air"+"\ ".strip() 
            for folderjobno in os.listdir(p)[int(self.job_no)-1:]:
                c.execute("update database set JOB_NUMBER=? where (YEAR=? AND MONTH=? AND DAY=? AND JOB_NUMBER=? AND Booking_No_Sea=? AND Booking_No_Truck=?)",
                          (str(int(folderjobno)-1),self.year,self.month,self.day,str(int(folderjobno)),"-","-"))
                conn.commit()
                os.rename(curr+folderjobno, curr+str(int(folderjobno)-1))

            buttonReply = QMessageBox.about(self, "Message!!!", "Deleted successfully.")
            self.deleteitems()
            self.allowdelete = True
            c.close()

    def deleteitems(self):
        self.SixthPageUi.jobfileno.clear()
        self.SixthPageUi.jjno.clear()
        self.SixthPageUi.shipper.clear()
        self.SixthPageUi.consignee.clear()
        self.SixthPageUi.awb.clear()
        self.SixthPageUi.origin.clear()
        self.SixthPageUi.destination.clear()


class SeventhPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.SeventhPageUi = SeventhMainWindow()
        self.SeventhPageUi.seventh_setupUi(self)

        ############################
        self.truck_booking_no = ""
        self.year = 0
        self.month = 0
        self.day = 0
        self.job_no = 0
        self.transfer = ""
        
        self.transfer = 0
        self.rowdata = []
        ###########################
        self.allowdelete = True
        ############################
        self.SeventhPageUi.update.clicked.connect(self.update)
        ############################
        self.SeventhPageUi.add.clicked.connect(self.addlist)
        self.SeventhPageUi.edit.clicked.connect(self.editlist)
        self.SeventhPageUi.delete_.clicked.connect(self.delitem)
        ############################
        self.path = MAINPATH + "\ ".strip() + "Job Database"

    def addlist(self):
        if(len(self.SeventhPageUi.containerno.text()) != 0):
            self.SeventhPageUi.listWidget.addItem(self.SeventhPageUi.containerno.text())
            self.SeventhPageUi.containerno.clear()
    
    def editlist(self):
        row = self.SeventhPageUi.listWidget.currentRow()
        if(str(row) != str(-1)):
            newtext, ok = QInputDialog.getText(self, "Message!!!",  "Enter new text")
            if ok and (len(newtext) !=0):
                self.SeventhPageUi.listWidget.takeItem(self.SeventhPageUi.listWidget.currentRow())
                self.SeventhPageUi.listWidget.insertItem(row, QListWidgetItem(newtext))

    def delitem(self):
        self.SeventhPageUi.listWidget.takeItem(self.SeventhPageUi.listWidget.currentRow())

    def update(self):
        conn = sqlite3.connect(self.path+ "\ ".strip()+"database.db")
        c = conn.cursor()

        ####################
        cur_find_day = self.path+ "\ ".strip()+str(self.year)+ "\ ".strip()+self.month+ "\ ".strip()+self.day
        ####################
        jobfileno = str(self.SeventhPageUi.jobfileno.text())
        jjno = str(self.SeventhPageUi.jjno.text())
        shipper = str(self.SeventhPageUi.shipper.text())
        consignee = str(self.SeventhPageUi.consignee.text())
        bookingno = str(self.SeventhPageUi.bookingno.text())
        origin = str(self.SeventhPageUi.origin.text())
        destination = str(self.SeventhPageUi.destination.text())

        upload = True
        if(len(jobfileno)==0 or len(jjno)==0 or len(shipper)==0 or len(consignee)==0 or len(bookingno)==0
            or len(origin)==0 or len(destination)==0 or self.SeventhPageUi.listWidget.count()==0):
            buttonReply = QMessageBox.question(self, 'Message !!!', "Form is not completed! Want to upload?", QMessageBox.Yes | QMessageBox.No)
            if buttonReply == QMessageBox.No:
                upload = False
            if(len(bookingno)==0):
                QMessageBox.about(self, "Warning!!!", "Please insert Truck Booking No.")
                upload = False

        if(upload == True):
            c.execute("delete from database where Booking_No_Truck = ?", (self.truck_booking_no,))
            conn.commit()
            self.truck_booking_no = bookingno
            
            if (len(jobfileno)==0): jobfileno = "-"
            if (len(jjno)==0): jjno = "-"
            if (len(shipper)==0): shipper = "-"
            if (len(consignee)==0): consignee = "-"
            if (len(origin)==0): origin = "-"
            if (len(destination)==0): destination = "-"
            ##############################
            make = []
                
            c.execute("select rowid from database where Booking_No_Truck = ?", (bookingno,))
            row = c.fetchone()
    
            if(row):
                make.append(False)

            if False not in make:
                for i in range(self.SeventhPageUi.listWidget.count()):
                    container_no = self.SeventhPageUi.listWidget.item(i).text()
                    
                    item = (jobfileno,jjno,shipper,consignee,"-","-",bookingno,"-",origin,destination,container_no,
                            self.year,self.month,self.day,self.job_no,self.transfer,)
                    c.execute("INSERT INTO database (Job_File_No,JJ_No,Shipper,Consignee,Booking_No_Sea,AWB,Booking_No_Truck,BL,ORIGIN,DESTINATION,CONTAINER_NO,"+
                                  "YEAR,MONTH,DAY,JOB_NUMBER,Transfer) "+
                                  "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", item)
                    conn.commit()

                if(self.SeventhPageUi.listWidget.count() == 0):
                    container_no = "-"
                    item = (jobfileno,jjno,shipper,consignee,"-","-",bookingno,"-",origin,destination,container_no,
                            self.year,self.month,self.day,self.job_no,self.transfer,)
                    c.execute("INSERT INTO database (Job_File_No,JJ_No,Shipper,Consignee,Booking_No_Sea,AWB,Booking_No_Truck,BL,ORIGIN,DESTINATION,CONTAINER_NO,"+
                                  "YEAR,MONTH,DAY,JOB_NUMBER,Transfer) "+
                                  "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", item)
                    conn.commit()
            else:
                QMessageBox.about(self, "Warning", "This information already exists!!!")

        os.startfile(cur_find_day + "\ ".strip() + "truck"+ "\ ".strip() + str(self.job_no))
        c.close()
        

    def deleteall(self):
        conn = sqlite3.connect(self.path+ "\ ".strip()+"database.db")
        c = conn.cursor()

        upload = True
        if(self.allowdelete == True):
            buttonReply = QMessageBox.question(self, 'Message !!!', "Are you sure you want to delete this job document?", QMessageBox.Yes | QMessageBox.No)
            if buttonReply == QMessageBox.No:
                upload = False
                   
        if(upload == True and self.allowdelete == True):

            c.execute("select rowid from database where Booking_No_Truck = ? ", (self.truck_booking_no,))
            all_job_no = c.fetchall()

            c.execute("select * from database where Booking_No_Truck = ? ", (self.truck_booking_no,))
            truck_information = c.fetchall()

            p = self.path+ "\ ".strip()+self.year+ "\ ".strip()+self.month+ "\ ".strip()+self.day+ "\ ".strip()+"truck"

            new_truck_information = {}
            
            if(len(truck_information) != 0 ):
                current = truck_information[0]
                i = 1
                for information in truck_information:
                    if(current[4] == information[4]):
                        if(i not in new_truck_information):
                            new_truck_information[i] = []
                            new_truck_information[i].append(information)
                        else:
                            new_truck_information[i].append(information)
                    else:
                        i = i + 1
                        if(i not in new_truck_information):
                            new_truck_information[i] = []
                            new_truck_information[i].append(information)
                        else:
                            new_truck_information[i].append(information)

                    current = information

            
            c.execute("delete from database where Booking_No_Truck = ?", (self.truck_booking_no,))
            conn.commit()
            self.truck_booking_no = ""

            s = self.path+ "\ ".strip()+self.year+ "\ ".strip()+self.month+ "\ ".strip()+self.day+"\ ".strip()+"truck"+"\ ".strip()+self.job_no
            if os.path.exists(s):
                shutil.rmtree(s)
                
            curr = self.path+"\ ".strip()+self.year+"\ ".strip()+self.month+"\ ".strip()+self.day+"\ ".strip()+"truck"+"\ ".strip()
            for folderjobno in os.listdir(p)[int(self.job_no)-1:]:
                c.execute("update database set JOB_NUMBER=? where (YEAR=? AND MONTH=? AND DAY=? AND JOB_NUMBER=? AND Booking_No_Sea=? AND AWB=?)",
                          (str(int(folderjobno)-1),self.year,self.month,self.day,str(int(folderjobno)),"-","-"))
                conn.commit()
                os.rename(curr+folderjobno, curr+str(int(folderjobno)-1))

                
            buttonReply = QMessageBox.about(self, "Message!!!", "Deleted successfully.")
            self.deleteitems()
            self.allowdelete = True
            c.close()
            

    def deleteitems(self):
        self.SeventhPageUi.listWidget.clear()
        self.SeventhPageUi.jobfileno.clear()
        self.SeventhPageUi.jjno.clear()
        self.SeventhPageUi.shipper.clear()
        self.SeventhPageUi.consignee.clear()
        self.SeventhPageUi.bookingno.clear()
        self.SeventhPageUi.origin.clear()
        self.SeventhPageUi.destination.clear()
        self.SeventhPageUi.containerno.clear()

if __name__== "__main__":
    app = QApplication(sys.argv)
    main_page = Main()
    main_page.show_FirstPage()
    sys.exit(app.exec_())







