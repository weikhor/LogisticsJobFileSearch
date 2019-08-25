import sys
import os
import shutil

from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem, QMessageBox, QMainWindow, QTableWidgetItem, QTextEdit,QFileDialog,QSizePolicy, QMessageBox
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

#MAINPATH = r"D:"
MAINPATH = os.getcwd()

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
            QMessageBox.about(self.SecondPage, "Message!!!", "Sea Import")
        elif(self.SecondPage.SecondPageUi.transfer.currentText() == "SE"):
            self.SecondPage.SecondPageUi.transfer.setCurrentIndex(1)
            self.SecondPage.donetoupload = True
            QMessageBox.about(self.SecondPage, "Message!!!", "Sea Export")
        elif(self.SecondPage.SecondPageUi.transfer.currentText() == "AI"):
            self.ThirdPage.ThirdPageUi.transfer.setCurrentIndex(2)
            self.SecondPage.close()
            self.SecondPage.deleteitems()
            self.ThirdPage.show()
            self.ThirdPage.donetoupload = True
            QMessageBox.about(self.ThirdPage, "Message!!!", "Air Import")
        elif(self.SecondPage.SecondPageUi.transfer.currentText() == "AE"):
            self.ThirdPage.ThirdPageUi.transfer.setCurrentIndex(3)
            self.SecondPage.close()
            self.SecondPage.deleteitems()
            self.ThirdPage.show()
            self.ThirdPage.donetoupload = True
            QMessageBox.about(self.ThirdPage, "Message!!!", "Air Export")
        else:
            self.FourthPage.FourthPageUi.transfer.setCurrentIndex(4)
            self.SecondPage.close()
            self.SecondPage.deleteitems()
            self.FourthPage.show()
            self.FourthPage.donetoupload = True
            QMessageBox.about(self.FourthPage, "Message!!!", "Truck")

    def Done3(self):
        if(self.ThirdPage.ThirdPageUi.transfer.currentText() == "SI"):
            self.SecondPage.SecondPageUi.transfer.setCurrentIndex(0)
            self.ThirdPage.close()
            self.ThirdPage.deleteitems()
            self.SecondPage.show()
            self.SecondPage.donetoupload = True
            QMessageBox.about(self.SecondPage, "Message!!!", "Sea Import")
        elif(self.ThirdPage.ThirdPageUi.transfer.currentText() == "SE"):
            self.SecondPage.SecondPageUi.transfer.setCurrentIndex(1)
            self.ThirdPage.close()
            self.ThirdPage.deleteitems()
            self.SecondPage.show()
            self.SecondPage.donetoupload = True
            QMessageBox.about(self.SecondPage, "Message!!!", "Sea Export")
        elif(self.ThirdPage.ThirdPageUi.transfer.currentText() == "AI"):
            self.ThirdPage.ThirdPageUi.transfer.setCurrentIndex(2)
            self.ThirdPage.donetoupload = True
            QMessageBox.about(self.ThirdPage, "Message!!!", "Air Import")
        elif(self.ThirdPage.ThirdPageUi.transfer.currentText() == "AE"):
            self.ThirdPage.ThirdPageUi.transfer.setCurrentIndex(3)
            self.ThirdPage.donetoupload = True
            QMessageBox.about(self.ThirdPage, "Message!!!", "Air Export")
        else:
            self.FourthPage.FourthPageUi.transfer.setCurrentIndex(4)
            self.ThirdPage.close()
            self.ThirdPage.deleteitems()
            self.FourthPage.show()
            self.FourthPage.donetoupload = True
            QMessageBox.about(self.FourthPage, "Message!!!", "Truck")
            
    def Done4(self):
        if(self.FourthPage.FourthPageUi.transfer.currentText() == "SI"):
            self.SecondPage.SecondPageUi.transfer.setCurrentIndex(0)
            self.FourthPage.close()
            self.FourthPage.deleteitems()
            self.SecondPage.show()
            self.SecondPage.donetoupload = True
            QMessageBox.about(self.SecondPage, "Message!!!", "Sea Import")
        elif(self.FourthPage.FourthPageUi.transfer.currentText() == "SE"):
            self.SecondPage.SecondPageUi.transfer.setCurrentIndex(1)
            self.FourthPage.close()
            self.FourthPage.deleteitems()
            self.SecondPage.show()
            self.SecondPage.donetoupload = True
            QMessageBox.about(self.SecondPage, "Message!!!", "Sea Export")
        elif(self.FourthPage.FourthPageUi.transfer.currentText() == "AI"):
            self.ThirdPage.ThirdPageUi.transfer.setCurrentIndex(2)
            self.FourthPage.close()
            self.FourthPage.deleteitems()
            self.ThirdPage.show()
            self.ThirdPage.donetoupload = True
            QMessageBox.about(self.ThirdPage, "Message!!!", "Air Import")
        elif(self.FourthPage.FourthPageUi.transfer.currentText() == "AE"):
            self.ThirdPage.ThirdPageUi.transfer.setCurrentIndex(3)
            self.FourthPage.close()
            self.FourthPage.deleteitems()
            self.ThirdPage.show()
            self.ThirdPage.donetoupload = True
            QMessageBox.about(self.ThirdPage, "Message!!!", "Air Export")
        else:
            self.FourthPage.FourthPageUi.transfer.setCurrentIndex(4)
            self.FourthPage.donetoupload = True
            QMessageBox.about(self.FourthPage, "Message!!!", "Truck")

class FirstPage(QMainWindow):
    def __init__(self):
        super().__init__()
        #super().setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.FirstPageUi =  FirstMainWindow()
        self.FirstPageUi.first_setupUi(self)
        self.secondpage = SecondPage()
        #booking combo box
        self.FirstPageUi.bookingNo.addItem("Booking No", True)
        self.FirstPageUi.bookingNo.addItem("Container No", True)
        self.FirstPageUi.bookingNo.addItem("BL No", True)
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
        #allinformation
        self.all = False
        
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
        self.show()

    def allsortinformation(self, column):
        access1 = {0:"Job_File_No",1:"JJ_No",2:"Shipper",3:"Consignee",4:"Booking_No",5:"BL",6:"ORIGIN",7:"DESTINATION",8:"CONTAINER_NO",9:"Transfer"}
        access2 = {0:"Job_File_No",1:"JJ_No",2:"Shipper",3:"Consignee",4:"AWB",5:"ORIGIN",6:"DESTINATION",7:"Transfer"}
        access3 = {0:"Job_File_No",1:"JJ_No",2:"Shipper",3:"Consignee",4:"Booking_No",5:"ORIGIN",6:"DESTINATION",7:"CONTAINER_NO",8:"Transfer"}

        
        if(self.FirstPageUi.tableWidget.columnCount() == 10):
            self.sortinformation = access1[column]
            self.allinformation()
        if(self.FirstPageUi.tableWidget.columnCount() == 8):
            self.sortinformation = access2[column]
            self.allinformation()
        if(self.FirstPageUi.tableWidget.columnCount() == 9):
            self.sortinformation = access3[column]
            self.allinformation()

        self.sortinformation = "YEAR DESC,MONTH DESC,DAY DESC,JOB_NUMBER ASC"
            
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
        if(len(self.data) != 0):
            currentdata = self.data[self.allrow]
            transfer = self.FirstPageUi.transfer.currentText()
            numcolum = len(self.data[0])
            if(numcolum == 14):
                year = currentdata[9]
                p = self.path+"\ ".strip()+"sea.db"

                conn = sqlite3.connect(p)
                c = conn.cursor()
                bookingno = currentdata[4]
                
                c.execute("select * from seadatabase where Booking_No = ?", (bookingno,))
                DATA = c.fetchall()

                c.execute("select rowid from seadatabase where Booking_No = ?", (bookingno,))
                ROWID = c.fetchone()
                ROWID = int(ROWID[0])

                ########################################
                jobfileno = str(DATA[0][0])
                self.FifthPage.FifthPageUi.jobfileno.setText(jobfileno)
                jjno = str(DATA[0][1])
                self.FifthPage.FifthPageUi.jjno.setText(jjno)
                shipper = str(DATA[0][2])
                self.FifthPage.FifthPageUi.shipper.setText(shipper)
                consignee = str(DATA[0][3])
                self.FifthPage.FifthPageUi.consignee.setText(consignee)
                bookingno = str(DATA[0][4])
                self.FifthPage.FifthPageUi.bookingno.setText(bookingno)
                bl = str(DATA[0][5])
                self.FifthPage.FifthPageUi.bl_alb.setText(bl)
                origin = str(DATA[0][6])
                self.FifthPage.FifthPageUi.origin.setText(origin)
                destination = str(DATA[0][7])
                self.FifthPage.FifthPageUi.destination.setText(destination)

                ########################################
                self.FifthPage.year = str(DATA[0][9])
                self.FifthPage.month = str(DATA[0][10])
                self.FifthPage.day = str(DATA[0][11])
                self.FifthPage.job_no = str(DATA[0][12])
                self.FifthPage.transfer = str(DATA[0][13])

                self.FifthPage.allcontainerdata = []
                
                for i in range(len(DATA)):
                    container_no = str(DATA[i][8])
                    self.FifthPage.FifthPageUi.listWidget.addItem(container_no)
                    self.FifthPage.allcontainerdata.append(ROWID)
                    ROWID = ROWID + 1

                ########################################
                self.FifthPage.allowdelete = True
                ########################################
                self.close()
                self.FifthPage.show()
                
                c.close()
            
            elif(numcolum == 12):
                year = currentdata[7]
                p = self.path+"\ ".strip()+"air.db"
                
                conn = sqlite3.connect(p)
                c = conn.cursor()
                awb = currentdata[4]
                
                c.execute("select * from airdatabase where AWB = ?", (awb,))
                DATA = c.fetchall()

                c.execute("select rowid from airdatabase where AWB = ?", (awb,))
                ROWID = c.fetchone()
                ROWID = int(ROWID[0])
                self.SixthPage.rowdata.append(ROWID)
                #########################################
                jobfileno = str(DATA[0][0])
                self.SixthPage.SixthPageUi.jobfileno.setText(jobfileno)
                jjno = str(DATA[0][1])
                self.SixthPage.SixthPageUi.jjno.setText(jjno)
                shipper = str(DATA[0][2])
                self.SixthPage.SixthPageUi.shipper.setText(shipper)
                consignee = str(DATA[0][3])
                self.SixthPage.SixthPageUi.consignee.setText(consignee)
                awb = str(DATA[0][4])
                self.SixthPage.SixthPageUi.awb.setText(awb)
                origin = str(DATA[0][5])
                self.SixthPage.SixthPageUi.origin.setText(origin)
                destination = str(DATA[0][6])
                self.SixthPage.SixthPageUi.destination.setText(destination)
                #########################################
                self.SixthPage.year = str(DATA[0][7])
                self.SixthPage.month = str(DATA[0][8])
                self.SixthPage.day = str(DATA[0][9])
                self.SixthPage.job_no = str(DATA[0][10])
                self.SixthPage.transfer = str(DATA[0][11])
                ########################################
                self.SixthPage.allowdelete = True
                ########################################
                self.close()
                self.SixthPage.show()
                c.close()
            else:
                year = currentdata[8]
                p = self.path+"\ ".strip()+"truck.db"

                conn = sqlite3.connect(p)

                c = conn.cursor()
                bookingno = currentdata[4]

                c.execute("select * from truckdatabase where Booking_No = ?", (bookingno,))
                DATA = c.fetchall()

                c.execute("select rowid from truckdatabase where Booking_No = ?", (bookingno,))
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
                bookingno = str(DATA[0][4])
                self.SeventhPage.SeventhPageUi.bookingno.setText(bookingno)
                origin = str(DATA[0][5])
                self.SeventhPage.SeventhPageUi.origin.setText(origin)
                destination = str(DATA[0][6])
                self.SeventhPage.SeventhPageUi.destination.setText(destination)
                ########################################
                self.SeventhPage.year = str(DATA[0][8])
                self.SeventhPage.month = str(DATA[0][9])
                self.SeventhPage.day = str(DATA[0][10])
                self.SeventhPage.job_no = str(DATA[0][11])
                self.SeventhPage.transfer = str(DATA[0][12])
                self.SeventhPage.allcontainerdata = []
                
                for i in range(len(DATA)):
                    container_no = str(DATA[i][7])
                    self.SeventhPage.SeventhPageUi.listWidget.addItem(container_no)
                    self.SeventhPage.allcontainerdata.append(ROWID)
                    ROWID = ROWID + 1

                ########################################
                self.SeventhPage.allowdelete = True
                ########################################
                self.close()
                self.SeventhPage.show()
                c.close()
        
    def allinformation(self):
        self.all = True

        self.openalldatabase()
        
        transfer = self.FirstPageUi.transfer.currentText()
        self.data = []
        
        access1 = ["Job File No","JJ No","Shipper","Consignee","Booking No","BL/AWB","Origin","Destination","Container No","Transport"]
        access2 = ["Job File No","JJ No","Shipper","Consignee","BL/AWB","Origin","Destination","Transport"]
        access3 = ["Job File No","JJ No","Shipper","Consignee","Booking No","Origin","Destination","Container No","Transport"]

        data = []
        
        if(transfer == "SI" or transfer == "SE"):
            pathtransfer = MAINPATH +"\ ".strip()+ "Job Database" +"\ ".strip() + "sea.db"
            conn = sqlite3.connect(pathtransfer)
            c = conn.cursor()

            if(transfer == "SI"):
                if(self.sortinformation == "YEAR DESC,MONTH DESC,DAY DESC,JOB_NUMBER ASC"):
                    c.execute("SELECT * FROM seadatabase WHERE Transfer='SI' ORDER BY " + self.sortinformation)
                else:
                    c.execute("SELECT * FROM seadatabase WHERE Transfer='SI' ORDER BY " + self.sortinformation + " ASC,YEAR DESC,MONTH DESC,DAY DESC,JOB_NUMBER ASC")
            else:
                if(self.sortinformation == "YEAR DESC,MONTH DESC,DAY DESC,JOB_NUMBER ASC"):
                    c.execute("SELECT * FROM seadatabase WHERE Transfer='SE' ORDER BY " + self.sortinformation)
                else:
                    c.execute("SELECT * FROM seadatabase WHERE Transfer='SE' ORDER BY " + self.sortinformation + " ASC,YEAR DESC,MONTH DESC,DAY DESC,JOB_NUMBER ASC")
            

            data = c.fetchall()
            self.data = data
            
            self.FirstPageUi.tableWidget.setColumnCount(len(access1))
            self.FirstPageUi.tableWidget.setRowCount(len(data))
            self.FirstPageUi.tableWidget.setHorizontalHeaderLabels(access1)

            for i in range(len(data)):
                for j in range(len(access1)-1):
                    self.FirstPageUi.tableWidget.setItem(i,j, QTableWidgetItem(data[i][j]))
                    self.FirstPageUi.tableWidget.setItem(i, 9, QTableWidgetItem(transfer))
                    
            c.close()
        elif(transfer == "AI" or transfer == "AE"):
            pathtransfer = MAINPATH +"\ ".strip()+ "Job Database" +"\ ".strip() + "air.db"
            conn = sqlite3.connect(pathtransfer)
            c = conn.cursor()

            if(transfer == "AI"):
                if(self.sortinformation == "YEAR DESC,MONTH DESC,DAY DESC,JOB_NUMBER ASC"):
                    c.execute(" SELECT * FROM airdatabase WHERE Transfer='AI' ORDER BY " + self.sortinformation)
                else:
                    c.execute(" SELECT * FROM airdatabase WHERE Transfer='AI' ORDER BY " + self.sortinformation + " ASC,YEAR DESC,MONTH DESC,DAY DESC,JOB_NUMBER ASC")
            else:
                if(self.sortinformation == "YEAR DESC,MONTH DESC,DAY DESC,JOB_NUMBER ASC"):
                    c.execute(" SELECT * FROM airdatabase WHERE Transfer='AE' ORDER BY " + self.sortinformation)
                else:
                    c.execute(" SELECT * FROM airdatabase WHERE Transfer='AE' ORDER BY " + self.sortinformation + " ASC,YEAR DESC,MONTH DESC,DAY DESC,JOB_NUMBER ASC")

            data = c.fetchall()
            self.data = data
             
            self.FirstPageUi.tableWidget.setColumnCount(len(access2))
            self.FirstPageUi.tableWidget.setRowCount(len(data))
            self.FirstPageUi.tableWidget.setHorizontalHeaderLabels(access2)

            for i in range(len(data)):
                for j in range(len(access2)-1):
                    self.FirstPageUi.tableWidget.setItem(i,j, QTableWidgetItem(data[i][j]))
                    self.FirstPageUi.tableWidget.setItem(i, 7, QTableWidgetItem(transfer))

            c.close()
        else:
            pathtransfer = MAINPATH +"\ ".strip()+ "Job Database" +"\ ".strip() + "truck.db"
            conn = sqlite3.connect(pathtransfer)
            c = conn.cursor()

            if(self.sortinformation == "YEAR DESC,MONTH DESC,DAY DESC,JOB_NUMBER ASC"):
                c.execute(" SELECT * FROM truckdatabase WHERE Transfer='TE' ORDER BY " + self.sortinformation)
            else:
                c.execute(" SELECT * FROM truckdatabase WHERE Transfer='TE' ORDER BY " + self.sortinformation + ",YEAR DESC,MONTH DESC,DAY DESC,JOB_NUMBER ASC")

            data = c.fetchall()
            self.data = data

            self.FirstPageUi.tableWidget.setColumnCount(len(access3))
            self.FirstPageUi.tableWidget.setRowCount(len(data))
            self.FirstPageUi.tableWidget.setHorizontalHeaderLabels(access3)

            for i in range(len(data)):
                for j in range(len(access3)-1):
                    self.FirstPageUi.tableWidget.setItem(i,j, QTableWidgetItem(data[i][j]))
                    self.FirstPageUi.tableWidget.setItem(i, 7, QTableWidgetItem(transfer))
                
            c.close()

        self.sortinformation = "YEAR DESC,MONTH DESC,DAY DESC,JOB_NUMBER ASC"

        """

        current = 0
            pathyear = MAINPATH+"\ ".strip()+year
            if(transfer == "SI" or transfer == "SE"):
                self.FirstPageUi.tableWidget.setColumnCount(len(access1))
                self.FirstPageUi.tableWidget.setRowCount(SUM)
                self.FirstPageUi.tableWidget.setHorizontalHeaderLabels(access1)
            
                pathtransfer = MAINPATH +"\ ".strip()+ "Job Database" +"\ ".strip() + "sea.db"
                conn = sqlite3.connect(pathtransfer)
                c = conn.cursor()

                if(transfer == "SI"):
                    c.execute(" SELECT * FROM seadatabase WHERE Transfer='SI' ORDER BY " + self.sortinformation)
                else:
                    c.execute(" SELECT * FROM seadatabase WHERE Transfer='SE' ORDER BY " + self.sortinformation)
                
                data = c.fetchall()
                data.reverse()
                
                for i in range(len(data)):
                    for j in range(len(access1)-1):
                        self.FirstPageUi.tableWidget.setItem(curr+i,j, QTableWidgetItem(data[i][j]))

                for i in range(len(data)):
                    self.FirstPageUi.tableWidget.setItem(curr+i, 9, QTableWidgetItem(transfer))

                curr = curr + len(data)
                
                for d in data:
                    self.data.append(d)
                    
                c.close()                                                           
                                                    
            elif(transfer == "AI" or transfer == "AE"):
                self.FirstPageUi.tableWidget.setColumnCount(len(access2))
                self.FirstPageUi.tableWidget.setRowCount(SUM)
                self.FirstPageUi.tableWidget.setHorizontalHeaderLabels(access2)

                
                pathtransfer = MAINPATH +"\ ".strip()+ "Job Database" +"\ ".strip() + "air.db"
                conn = sqlite3.connect(pathtransfer)
                c = conn.cursor()

                if(transfer == "AI"):
                    c.execute(" SELECT * FROM airdatabase WHERE Transfer='AI' ORDER BY " + self.sortinformation)
                else:
                    c.execute(" SELECT * FROM airdatabase WHERE Transfer='AE' ORDER BY " + self.sortinformation)
                
                data = c.fetchall()
                data.reverse()
            
                for i in range(len(data)):
                    for j in range(len(access2)-1):
                        self.FirstPageUi.tableWidget.setItem(curr+i,j, QTableWidgetItem(data[i][j]))

                for i in range(len(data)):
                    self.FirstPageUi.tableWidget.setItem(curr+i, 7, QTableWidgetItem(transfer))

                curr = curr + len(data)
                
                for d in data:
                    self.data.append(d)
                
                c.close()
            
            else:
                self.FirstPageUi.tableWidget.setColumnCount(len(access3))
                self.FirstPageUi.tableWidget.setRowCount(SUM)
                self.FirstPageUi.tableWidget.setHorizontalHeaderLabels(access3)
                
                pathtransfer = MAINPATH +"\ ".strip()+ "Job Database" +"\ ".strip() + "truck.db"
                conn = sqlite3.connect(pathtransfer)
                c = conn.cursor()
                c.execute(" SELECT * FROM truckdatabase WHERE Transfer='TE' ORDER BY " + self.sortinformation)
                
                data = c.fetchall()
                data.reverse()

                for i in range(len(data)):
                    for j in range(len(access3)-1):
                        self.FirstPageUi.tableWidget.setItem(curr+i,j, QTableWidgetItem(data[i][j]))

                for i in range(len(data)):
                    self.FirstPageUi.tableWidget.setItem(curr+i, 8, QTableWidgetItem(transfer))

                curr = curr + len(data)

                for d in data:
                    self.data.append(d)
                
                c.close()
        """
        
    def openalldatabase(self):
        conn1 = sqlite3.connect(MAINPATH +"\ ".strip()+ "Job Database" +"\ ".strip() + "sea.db")
        c1 = conn1.cursor()
        c1.execute("CREATE TABLE IF NOT EXISTS seadatabase"+
              "(Job_File_No TEXT, JJ_No TEXT, Shipper TEXT, Consignee TEXT,Booking_No TEXT, BL TEXT, ORIGIN TEXT, DESTINATION TEXT, CONTAINER_NO TEXT,"+
              "YEAR TEXT, MONTH TEXT, DAY TEXT, JOB_NUMBER TEXT, Transfer TEXT)")
        c1.close()
        
        conn2 = sqlite3.connect(MAINPATH +"\ ".strip()+ "Job Database" +"\ ".strip() + "air.db")
        c2 = conn2.cursor()
        c2.execute("CREATE TABLE IF NOT EXISTS airdatabase"+
              "(Job_File_No TEXT, JJ_No TEXT, Shipper TEXT, Consignee TEXT,AWB TEXT, ORIGIN TEXT, DESTINATION TEXT,"+
              "YEAR TEXT, MONTH TEXT, DAY TEXT, JOB_NUMBER TEXT, Transfer TEXT,"+
                      "UNIQUE(Job_File_No, JJ_No, Shipper, Consignee, AWB, ORIGIN, DESTINATION))")
        c2.close()
        
        conn3 = sqlite3.connect(MAINPATH +"\ ".strip()+ "Job Database" +"\ ".strip() + "truck.db")
        c3 = conn3.cursor()
        c3.execute("CREATE TABLE IF NOT EXISTS truckdatabase"+
              "(Job_File_No TEXT,JJ_No TEXT,Shipper TEXT,Consignee TEXT,Booking_No TEXT,ORIGIN TEXT,DESTINATION TEXT,CONTAINER_NO TEXT,"+
              "YEAR TEXT,MONTH TEXT,DAY TEXT,JOB_NUMBER TEXT,Transfer TEXT)")
        c3.close()

    def doneclick(self):
        self.data = []
        self.all = False
        get_all_data = []
        
        self.FirstPageUi.tableWidget.setColumnCount(0)
        self.FirstPageUi.tableWidget.setRowCount(0)

        access1 = ["Job File No","JJ No","Shipper","Consignee","Booking No","BL/AWB","Origin","Destination","Container No"]
        access2 = ["Job File No","JJ No","Shipper","Consignee","BL/AWB","Origin","Destination"]
        access3 = ["Job File No","JJ No","Shipper","Consignee","Booking No","Origin","Destination","Container No"]

        booking_Number = self.FirstPageUi.bookingNo.currentText()
        booking_Text = self.FirstPageUi.lineEdit.text()

        pathyear = MAINPATH+"\ ".strip()+"Job Database"

        show = True
        ###############################
        if(show == True and len(booking_Text) != 0):
            pathtransfer = pathyear+"\ ".strip()+"sea.db"
            conn = sqlite3.connect(pathtransfer)
            c = conn.cursor()

            
            if(booking_Number == "Booking No"):
                c.execute('SELECT * FROM seadatabase WHERE Booking_No=?', (booking_Text,))
                get_all_data = c.fetchall()
                
            if(booking_Number == "Container No"):
                c.execute('SELECT * FROM seadatabase WHERE CONTAINER_No=?', (booking_Text,))
                get_all_data = c.fetchall()
                
            if(booking_Number == "BL No"):
                c.execute('SELECT * FROM seadatabase WHERE BL=?', (booking_Text,))
                get_all_data = c.fetchall()

            if(len(get_all_data) != 0):
                self.FirstPageUi.tableWidget.setColumnCount(len(access1))
                self.FirstPageUi.tableWidget.setRowCount(len(get_all_data))
                self.FirstPageUi.tableWidget.setHorizontalHeaderLabels(access1)
                show = False

            for i in range(len(get_all_data)):
                for j in range(len(access1)):
                    self.FirstPageUi.tableWidget.setItem(i,j, QTableWidgetItem(get_all_data[i][j]))

            if(len(get_all_data) != 0):
                show = False
                
            c.close()
        ###############################
        
        if(show == True and len(booking_Text) != 0):
            pathtransfer = pathyear+"\ ".strip()+"air.db"
            conn = sqlite3.connect(pathtransfer)
            c = conn.cursor()

            if(booking_Number == "AWB No"):
                c.execute('SELECT * FROM airdatabase WHERE AWB=?', (booking_Text,))
                get_all_data = c.fetchall()

            if(len(get_all_data) != 0):
                self.FirstPageUi.tableWidget.setColumnCount(len(access2))
                self.FirstPageUi.tableWidget.setRowCount(len(get_all_data))
                self.FirstPageUi.tableWidget.setHorizontalHeaderLabels(access2)
                show = False

            for i in range(len(get_all_data)):
                for j in range(len(access2)):
                    self.FirstPageUi.tableWidget.setItem(i,j, QTableWidgetItem(get_all_data[i][j]))
                
            c.close()
        ###############################
        if(show == True and len(booking_Text) != 0):
            pathtransfer = pathyear+"\ ".strip()+"truck.db"
            conn = sqlite3.connect(pathtransfer)
            c = conn.cursor()
                        
            if(booking_Number == "Booking No"):
                c.execute('SELECT * FROM truckdatabase WHERE Booking_No=?', (booking_Text,))
                get_all_data = c.fetchall()
                        
            if(booking_Number == "Container No"):
                c.execute('SELECT * FROM truckdatabase WHERE CONTAINER_No=?', (booking_Text,))
                get_all_data = c.fetchall()

            if(len(get_all_data) != 0):
                self.FirstPageUi.tableWidget.setColumnCount(len(access3))
                self.FirstPageUi.tableWidget.setRowCount(len(get_all_data))
                self.FirstPageUi.tableWidget.setHorizontalHeaderLabels(access3)
                show = False
            
            for i in range(len(get_all_data)):
                for j in range(len(access3)):
                    self.FirstPageUi.tableWidget.setItem(i,j, QTableWidgetItem(get_all_data[i][j]))
                    
            c.close()
        ###############################
        for d in get_all_data:
            self.data.append(d)

        self.num_column = 0
        if(len(self.data) != 0):
            self.num_column = len(self.data[0])

        #if(self.num_column == 14):
            #for i in range(len(self.data)):
                #for j in range(len(access)):
                    #z = sort_dict1[access[j]]
                    #self.FirstPageUi.tableWidget.setItem(i,j, QTableWidgetItem(self.data[i][z]))

        self.FirstPageUi.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        """
        if(self.num_column == 12):
            for i in range(len(self.data)):
                for j in range(len(access)):
                    z = sort_dict2[access[j]]
                    self.FirstPageUi.tableWidget.setItem(i,j, QTableWidgetItem(self.data[i][z]))
        
        if(self.num_column == 13):
            for i in range(len(self.data)):
                for j in range(len(access)):
                    z = sort_dict3[access[j]]
                    self.FirstPageUi.tableWidget.setItem(i,j, QTableWidgetItem(self.data[i][z]))

        """


        """
        access = []

        self.num_column = 0
        
        if(len(self.data) != 0):
            self.num_column = len(self.data[0])

        
        for i in range(self.FirstPageUi.sort.count()):
            if(self.FirstPageUi.sort.itemChecked(i)):
                if(self.num_column == 14):
                    access.append(self.FirstPageUi.sort.itemText(i))
                if(self.num_column == 12):
                    if(self.FirstPageUi.sort.itemText(i) != "Booking No" and self.FirstPageUi.sort.itemText(i) != "Container No"):
                        access.append(self.FirstPageUi.sort.itemText(i))
                if(self.num_column == 13):
                    if(self.FirstPageUi.sort.itemText(i) != "BL/AWB"):
                        access.append(self.FirstPageUi.sort.itemText(i))
       
        if(len(access) != 0):
            self.FirstPageUi.tableWidget.setColumnCount(len(access))
            self.FirstPageUi.tableWidget.setRowCount(len(self.data))
            self.FirstPageUi.tableWidget.setHorizontalHeaderLabels(access)

        sort_dict1 = {"Job File No":0,"JJ No":1,"Shipper":2,"Consignee":3,"Booking No":4,"BL/AWB":5,"Origin":6,"Destination":7,"Container No":8}
        sort_dict2 = {"Job File No":0,"JJ No":1,"Shipper":2,"Consignee":3,"BL/AWB":4,"Origin":5,"Destination":6}
        sort_dict3 = {"Job File No":0,"JJ No":1,"Shipper":2,"Consignee":3,"Booking No":4,"Origin":5,"Destination":6,"Container No":7}

        if(self.num_column == 14):
            for i in range(len(self.data)):
                for j in range(len(access)):
                    z = sort_dict1[access[j]]
                    self.FirstPageUi.tableWidget.setItem(i,j, QTableWidgetItem(self.data[i][z]))
        
        if(self.num_column == 12):
            for i in range(len(self.data)):
                for j in range(len(access)):
                    z = sort_dict2[access[j]]
                    self.FirstPageUi.tableWidget.setItem(i,j, QTableWidgetItem(self.data[i][z]))
        
        if(self.num_column == 13):
            for i in range(len(self.data)):
                for j in range(len(access)):
                    z = sort_dict3[access[j]]
                    self.FirstPageUi.tableWidget.setItem(i,j, QTableWidgetItem(self.data[i][z]))
                    
        self.FirstPageUi.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        """

    def singleclick(self, row, column):
        self.FirstPageUi.tableWidget.selectRow(row)
        self.allrow = row

    def doubleclick(self, row, column):
        if(self.all == True and len(self.data) != 0):
            num_column_all = len(self.data[0])
            if(num_column_all == 14):
                os.startfile(self.path+"\ ".strip()+self.data[row][9]+"\ ".strip()+self.data[row][10]+
                         "\ ".strip()+self.data[row][11]+"\ ".strip()+"sea"+ "\ ".strip()+self.data[row][12])
            if(num_column_all == 12 and len(self.data) != 0):
                os.startfile(self.path+"\ ".strip()+self.data[row][7]+"\ ".strip()+self.data[row][8]+
                         "\ ".strip()+self.data[row][9] +"\ ".strip()+"air"+ "\ ".strip()+self.data[row][10] )
            if(num_column_all == 13 and len(self.data) != 0):
                os.startfile(self.path+"\ ".strip()+self.data[row][8]+"\ ".strip()+self.data[row][9]+
                         "\ ".strip()+self.data[row][10]+"\ ".strip()+"truck"+ "\ ".strip()+self.data[row][11] )

        if(self.num_column == 14 and len(self.data) != 0):
            os.startfile(self.path+"\ ".strip()+self.data[row][9]+"\ ".strip()+self.data[row][10]+
                         "\ ".strip()+self.data[row][11]+"\ ".strip()+"sea"+ "\ ".strip()+self.data[row][12])
        if(self.num_column == 12 and len(self.data) != 0):
            os.startfile(self.path+"\ ".strip()+self.data[row][7]+"\ ".strip()+self.data[row][8]+
                         "\ ".strip()+self.data[row][9]+"\ ".strip()+"air"+ "\ ".strip()+self.data[row][10] )
        if(self.num_column == 13 and len(self.data) != 0):
            os.startfile(self.path+"\ ".strip()+self.data[row][8]+"\ ".strip()+self.data[row][9]+
                         "\ ".strip()+self.data[row][10]+"\ ".strip()+"truck"+ "\ ".strip()+self.data[row][11] )
        
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
            conn = sqlite3.connect(self.path+ "\ ".strip() +"sea.db")
            c = conn.cursor()

            c.execute("CREATE TABLE IF NOT EXISTS seadatabase"+
              "(Job_File_No TEXT, JJ_No TEXT, Shipper TEXT, Consignee TEXT,Booking_No TEXT, BL TEXT, ORIGIN TEXT, DESTINATION TEXT, CONTAINER_NO TEXT,"+
              "YEAR TEXT, MONTH TEXT, DAY TEXT, JOB_NUMBER TEXT, Transfer TEXT)")

            
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

            
            if(upload == True):
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
                c.execute("select rowid from seadatabase where Booking_No = ?", (bookingno,))
                row = c.fetchone()
                if(row):
                    make.append(False)
                        
                c.execute("select rowid from seadatabase where BL = ?", (bl_alb,))
                row = c.fetchone()
                if(row):
                    make.append(False)

            
                if False not in make:
                    os.mkdir(cur_find_day + "\ ".strip() + str(jj))
                    os.startfile(cur_find_day + "\ ".strip() + str(jj))
                    
                    for i in range(self.SecondPageUi.listWidget.count()):
                        container_no = self.SecondPageUi.listWidget.item(i).text()
                        item = (jobfileno,jjno,shipper,consignee,bookingno,bl_alb,origin,destination,container_no,year,month,day,jj,transfer,)
                        c.execute("INSERT INTO seadatabase (Job_File_No,JJ_No,Shipper,Consignee,Booking_No,BL,ORIGIN,DESTINATION,CONTAINER_NO,"+
                                  "YEAR,MONTH,DAY,JOB_NUMBER,Transfer) "+
                                  "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);", item)
                        conn.commit()
                else:
                    QMessageBox.about(self, "Warning", "This information already exists!!!")

                self.donetoupload = False

                c.close()
                conn.close()
                
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
            conn = sqlite3.connect(self.path+ "\ ".strip() +"air.db")
            c = conn.cursor()
            
            c.execute("CREATE TABLE IF NOT EXISTS airdatabase"+
              "(Job_File_No TEXT, JJ_No TEXT, Shipper TEXT, Consignee TEXT,AWB TEXT, ORIGIN TEXT, DESTINATION TEXT,"+
              "YEAR TEXT, MONTH TEXT, DAY TEXT, JOB_NUMBER TEXT, Transfer TEXT)")

            jobfileno = str(self.ThirdPageUi.jobfileno.text())
            jjno = str(self.ThirdPageUi.jjno.text())
            shipper = str(self.ThirdPageUi.shipper.text())
            consignee = str(self.ThirdPageUi.consignee.text())
            bl_alb = str(self.ThirdPageUi.awb.text())
            origin = str(self.ThirdPageUi.origin.text())
            destination = str(self.ThirdPageUi.destination.text())
            ############################
            upload = True
            if(len(jobfileno)==0 or len(jjno)==0 or len(shipper)==0 or len(consignee)==0 or len(bl_alb)==0
               or len(origin)==0 or len(destination)==0):
               buttonReply = QMessageBox.question(self, 'Message !!!', "Form is not completed! Want to upload?", QMessageBox.Yes | QMessageBox.No)
               if buttonReply == QMessageBox.No:
                   upload = False

            if(upload == True):
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
                
                c.execute("select rowid from airdatabase where AWB = ?", (bl_alb,))
                row = c.fetchone()
                if(row):
                    make.append(False)

                
                if False not in make:
                    os.mkdir(cur_find_day + "\ ".strip() + str(jj))
                    os.startfile(cur_find_day + "\ ".strip() + str(jj))
                    
                    item = (jobfileno,jjno,shipper,consignee,bl_alb,origin,destination,year,month,day,jj,transfer,)
                    c.execute("INSERT INTO airdatabase (Job_File_No,JJ_No,Shipper,Consignee,AWB,ORIGIN,DESTINATION,"+
                        "YEAR, MONTH, DAY, JOB_NUMBER, Transfer) "+
                        "VALUES (?,?,?,?,?,?,?,?,?,?,?,?);", item)
                       
                    conn.commit()
            
                else:
                    QMessageBox.about(self, "Warning", "This information already exists!!!")

                c.close()
                conn.close()
                self.donetoupload = False
                
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
            conn = sqlite3.connect(self.path+ "\ ".strip() +"truck.db")
            c = conn.cursor()

            c.execute("CREATE TABLE IF NOT EXISTS truckdatabase"+
              "(Job_File_No TEXT,JJ_No TEXT,Shipper TEXT,Consignee TEXT,Booking_No TEXT,ORIGIN TEXT,DESTINATION TEXT,CONTAINER_NO TEXT,"+
              "YEAR TEXT,MONTH TEXT,DAY TEXT,JOB_NUMBER TEXT,Transfer TEXT)")

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
            
            if(upload == True):
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
                
                c.execute("select rowid from truckdatabase where Booking_No = ?", (bookingno,))
                row = c.fetchone()
                if(row):
                    make.append(False)
                
                if False not in make:
                    os.mkdir(cur_find_day + "\ ".strip() + str(jj))
                    os.startfile(cur_find_day + "\ ".strip() + str(jj))
                    
                    for i in range(self.FourthPageUi.listWidget.count()):
                        container_No = self.FourthPageUi.listWidget.item(i).text()
                        
                        item = (jobfileno,jjno,shipper,consignee,bookingno,origin,destination,container_No,year,month,day,jj,transfer,)
                        c.execute("INSERT INTO truckdatabase (Job_File_No,JJ_No,Shipper,Consignee,Booking_No,ORIGIN,DESTINATION,CONTAINER_NO,"+
                              "YEAR, MONTH, DAY, JOB_NUMBER,Transfer) "+
                              "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);", item)
                        conn.commit()
            
                else:
                    QMessageBox.about(self, "Warning", "This information already exists!!!")
                
                
                c.close()
                conn.close()
                self.donetoupload = False
                ###############################
            
            
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
        self.year = 0
        self.month = 0
        self.day = 0
        self.job_no = 0
        self.transfer = 0
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
        conn = sqlite3.connect(self.path+ "\ ".strip()+"sea.db")
        c = conn.cursor()
        
        c.execute("delete from seadatabase" +
                    " where ("+"YEAR="+self.year +" AND MONTH="+self.month+" AND DAY="+self.day+" AND JOB_NUMBER="+self.job_no+")")
        conn.commit()

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
                
        if(upload == True):
            make = []
            c.execute("select rowid from seadatabase where Booking_No = ?", (bookingno,))
            row = c.fetchone()
            if(row):
                make.append(False)
                        
            c.execute("select rowid from seadatabase where BL = ?", (bl_alb,))
            row = c.fetchone()
            if(row):
                make.append(False)

            
            if False not in make:
                for i in range(self.FifthPageUi.listWidget.count()):
                    container_no = self.FifthPageUi.listWidget.item(i).text()
                    item = (jobfileno,jjno,shipper,consignee,bookingno,bl_alb,origin,destination,container_no,self.year,self.month,self.day,self.job_no,self.transfer,)
            
                    c.execute("INSERT INTO seadatabase (Job_File_No,JJ_No,Shipper,Consignee,Booking_No,BL,ORIGIN,DESTINATION,CONTAINER_NO,"+
                                "YEAR,MONTH,DAY,JOB_NUMBER,Transfer) "+
                                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);", item)
                    conn.commit()
                
            else:
                QMessageBox.about(self, "Warning", "This information already exists!!!")

        os.startfile(cur_find_day + "\ ".strip() + "sea"+ "\ ".strip() + str(self.job_no))
        c.close()

    def deleteall(self):
        conn = sqlite3.connect(self.path+ "\ ".strip()+"sea.db")
        c = conn.cursor()

        upload = True
        if(self.allowdelete == True):
            buttonReply = QMessageBox.question(self, 'Message !!!', "Are you sure you want to delete this job document?", QMessageBox.Yes | QMessageBox.No)
            if buttonReply == QMessageBox.No:
                upload = False
                   
        if(upload == True and self.allowdelete == True):
            c.execute("select rowid  from seadatabase where ("+"YEAR="+self.year +" AND MONTH="+self.month+" AND DAY="+self.day+")")
            all_job_no = c.fetchall()

            c.execute("select * from seadatabase where ("+"YEAR="+self.year +" AND MONTH="+self.month+" AND DAY="+self.day+")")
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

            c.execute("delete from seadatabase" +
                    " where ("+"YEAR="+self.year +" AND MONTH="+self.month+" AND DAY="+self.day+" AND JOB_NUMBER="+self.job_no+")")
            conn.commit()

            s = self.path+ "\ ".strip()+self.year+ "\ ".strip()+self.month+ "\ ".strip()+self.day+"\ ".strip()+"sea"+"\ ".strip()+self.job_no
            if os.path.exists(s):
                shutil.rmtree(s)
                
            curr = self.path+"\ ".strip()+self.year+"\ ".strip()+self.month+"\ ".strip()+self.day+"\ ".strip()+"sea"+"\ ".strip()
            for folderjobno in os.listdir(p)[int(self.job_no)-1:]:
                c.execute("update seadatabase set JOB_NUMBER="+str(int(folderjobno)-1)+
                          " where ("+"YEAR="+self.year +" AND MONTH="+self.month+" AND DAY="+self.day+" AND JOB_NUMBER="+str(int(folderjobno))+")")
                conn.commit()
                os.rename(curr+folderjobno, curr+str(int(folderjobno)-1))

            buttonReply = QMessageBox.about(self, "Message!!!", "Deleted successfully.")
            self.deleteitems()

            self.allowdelete = False
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
        self.year = 0
        self.month = 0
        self.day = 0
        self.job_no = 0
        self.transfer = 0
        self.rowdata = []
        ############################
        self.allowdelete = True
        ############################
        self.SixthPageUi.update.clicked.connect(self.update)
        ############################
        self.path = MAINPATH + "\ ".strip() + "Job Database"

    def update(self):
        conn = sqlite3.connect(self.path+ "\ ".strip()+"air.db")
        c = conn.cursor()

        c.execute("delete from airdatabase" +
                  " where ("+"YEAR="+self.year +" AND MONTH="+self.month+" AND DAY="+self.day+" AND JOB_NUMBER="+self.job_no+")")
        conn.commit()

        ####################
        cur_find_day = self.path+ "\ ".strip()+self.year+ "\ ".strip()+self.month+ "\ ".strip()+self.day

        
        jobfileno = str(self.SixthPageUi.jobfileno.text())
        jjno = str(self.SixthPageUi.jjno.text())
        shipper = str(self.SixthPageUi.shipper.text())
        consignee = str(self.SixthPageUi.consignee.text())
        awb = str(self.SixthPageUi.awb.text())
        origin = str(self.SixthPageUi.origin.text())
        destination = str(self.SixthPageUi.destination.text())

        ###################
        upload = True
        if(len(jobfileno)==0 or len(jjno)==0 or len(shipper)==0 or len(consignee)==0 or len(awb)==0
               or len(origin)==0 or len(destination)==0):
            buttonReply = QMessageBox.question(self, 'Message !!!', "Form is not completed! Want to upload?", QMessageBox.Yes | QMessageBox.No)
            if buttonReply == QMessageBox.No:
                upload = False

        if(upload == True):
            make = []
            c.execute("select rowid from airdatabase where AWB = ?", (awb,))
            row = c.fetchone()
            if(row):
                make.append(False)

            if False not in make:
                item = (jobfileno,jjno,shipper,consignee,awb,origin,destination,self.year,self.month,self.day,self.job_no,self.transfer,)
                c.execute("INSERT INTO airdatabase (Job_File_No,JJ_No,Shipper,Consignee,AWB,ORIGIN,DESTINATION,"+
                         "YEAR, MONTH, DAY, JOB_NUMBER, Transfer) "+
                        "VALUES (?,?,?,?,?,?,?,?,?,?,?,?);", item)
                       
                conn.commit()
            
            else:
                QMessageBox.about(self, "Warning", "This information already exists!!!")

        os.startfile(cur_find_day + "\ ".strip() + "air"+ "\ ".strip() + str(self.job_no))
        c.close() 
        ###################

    def deleteall(self):
        conn = sqlite3.connect(self.path+ "\ ".strip()+"air.db")
        c = conn.cursor()

        upload = True
        if(self.allowdelete == True):
            buttonReply = QMessageBox.question(self, 'Message !!!', "Are you sure you want to delete this job document?", QMessageBox.Yes | QMessageBox.No)
            if buttonReply == QMessageBox.No:
                upload = False
                   
        if(upload == True and self.allowdelete == True):
            c.execute("select rowid  from airdatabase where ("+"YEAR="+self.year +" AND MONTH="+self.month+" AND DAY="+self.day+")")
            all_job_no = c.fetchall()

            c.execute("select * from airdatabase where ("+"YEAR="+self.year +" AND MONTH="+self.month+" AND DAY="+self.day+")")
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

            
            c.execute("delete from airdatabase" +
                    " where ("+"YEAR="+self.year +" AND MONTH="+self.month+" AND DAY="+self.day+" AND JOB_NUMBER="+self.job_no+")")
            conn.commit()

            s = self.path+ "\ ".strip()+self.year+ "\ ".strip()+self.month+ "\ ".strip()+self.day+"\ ".strip()+"air"+"\ ".strip()+self.job_no
            if os.path.exists(s):
                shutil.rmtree(s)
                
            curr = self.path+"\ ".strip()+self.year+"\ ".strip()+self.month+"\ ".strip()+self.day+"\ ".strip()+"air"+"\ ".strip() 
            for folderjobno in os.listdir(p)[int(self.job_no)-1:]:
                c.execute("update airdatabase set JOB_NUMBER="+str(int(folderjobno)-1)+
                          " where ("+"YEAR="+self.year +" AND MONTH="+self.month+" AND DAY="+self.day+" AND JOB_NUMBER="+str(int(folderjobno))+")")
                conn.commit()
                os.rename(curr+folderjobno, curr+str(int(folderjobno)-1))

            buttonReply = QMessageBox.about(self, "Message!!!", "Deleted successfully.")
            self.deleteitems()
            self.allowdelete = False
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
        self.year = 0
        self.month = 0
        self.day = 0
        self.job_no = 0
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
        conn = sqlite3.connect(self.path+ "\ ".strip()+"truck.db")
        c = conn.cursor()

        c.execute("delete from truckdatabase" +
                    " where ("+"YEAR="+self.year +" AND MONTH="+self.month+" AND DAY="+self.day+" AND JOB_NUMBER="+self.job_no+")")
        conn.commit()
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
                
        if(upload == True):
            ##############################
            make = []
            c.execute("select rowid from truckdatabase where Booking_No = ?", (bookingno,))
            row = c.fetchone()
            if(row):
                make.append(False)

            if False not in make:
                for i in range(self.SeventhPageUi.listWidget.count()):
                    container_no = self.SeventhPageUi.listWidget.item(i).text()
                    item = (jobfileno,jjno,shipper,consignee,bookingno,origin,destination,container_no,self.year,self.month,self.day,self.job_no,self.transfer,)
                    c.execute("INSERT INTO truckdatabase (Job_File_No,JJ_No,Shipper,Consignee,Booking_No,ORIGIN,DESTINATION,CONTAINER_NO,"+
                                "YEAR,MONTH,DAY,JOB_NUMBER,Transfer) "+
                                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);", item)
                    conn.commit()
            else:
                QMessageBox.about(self, "Warning", "This information already exists!!!")

        os.startfile(cur_find_day + "\ ".strip() + "truck"+ "\ ".strip() + str(self.job_no))
        c.close()

    def deleteall(self):
        conn = sqlite3.connect(self.path+ "\ ".strip()+"truck.db")
        c = conn.cursor()

        upload = True
        if(self.allowdelete == True):
            buttonReply = QMessageBox.question(self, 'Message !!!', "Are you sure you want to delete this job document?", QMessageBox.Yes | QMessageBox.No)
            if buttonReply == QMessageBox.No:
                upload = False
                   
        if(upload == True and self.allowdelete == True):
            c.execute("select rowid from truckdatabase where ("+"YEAR="+self.year +" AND MONTH="+self.month+" AND DAY="+self.day+")")
            all_job_no = c.fetchall()

            c.execute("select * from truckdatabase where ("+"YEAR="+self.year +" AND MONTH="+self.month+" AND DAY="+self.day+")")
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

            c.execute("delete from truckdatabase" +
                    " where ("+"YEAR="+self.year +" AND MONTH="+self.month+" AND DAY="+self.day+" AND JOB_NUMBER="+self.job_no+")")
            conn.commit()

            s = self.path+ "\ ".strip()+self.year+ "\ ".strip()+self.month+ "\ ".strip()+self.day+"\ ".strip()+"truck"+"\ ".strip()+self.job_no
            if os.path.exists(s):
                shutil.rmtree(s)
                
            curr = self.path+"\ ".strip()+self.year+"\ ".strip()+self.month+"\ ".strip()+self.day+"\ ".strip()+"truck"+"\ ".strip()
            for folderjobno in os.listdir(p)[int(self.job_no)-1:]:
                c.execute("update truckdatabase set JOB_NUMBER="+str(int(folderjobno)-1)+
                          " where ("+"YEAR="+self.year +" AND MONTH="+self.month+" AND DAY="+self.day+" AND JOB_NUMBER="+str(int(folderjobno))+")")
                conn.commit()
                os.rename(curr+folderjobno, curr+str(int(folderjobno)-1))

                
            buttonReply = QMessageBox.about(self, "Message!!!", "Deleted successfully.")
            self.deleteitems()
            self.allowdelete = False
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







