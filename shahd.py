import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys

# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from PyQt5.uic.properties import QtCore


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Students ")

        self.setStyleSheet("background-color: #faf5f2;")

        self.setGeometry(100, 100, 600, 400)

        # calling method
        self.UiComponents()

        self.show()

    def UiComponents(self):

        # for corners

        pinkLabel = QLabel(self)
        pinkLabel.setStyleSheet("background-color: #eadade;")
        pinkLabel.setGeometry(0, 0, 300, 1000)

        pinkLabel2 = QLabel(self)
        pinkLabel2.setStyleSheet("background-color: #eadade;")
        pinkLabel2.setGeometry(1400, 0, 550, 1000)


        # student word label

        studentWordLabel = QLabel(self)
        studentWordLabel.setText("Students")
        studentWordLabel.setFont(QFont('Arial', 30))
        studentWordLabel.setStyleSheet("color: #536e8f;")
        studentWordLabel.setGeometry(340, 40, 200, 100)


        # statistic word label

        statisticWordLabel = QLabel(self)
        statisticWordLabel.setText("Statistics")
        statisticWordLabel.setFont(QFont('Arial', 30))
        statisticWordLabel.setStyleSheet("background-color: #eadade;  color: #536e8f;")
        statisticWordLabel.setGeometry(1550, 40, 200, 100)


        # the two buttons label above

        btLabel = QLabel(self)
        btLabel.setStyleSheet("border-radius : 20px; background-color: #c8bad3;")
        btLabel.setGeometry(1200, 130, 120, 40)


        # add student butten

        addStudent = QPushButton(self)
        addStudent.setText("Add Student")
        addStudent.setFont(QFont('Arial', 11))
        addStudent.setGeometry(1050, 130, 120, 40)
        addStudent.setStyleSheet("border-radius : 20px; background-color: #c8bad3; color: #536e8f;")
        #label0 = QLabel(self)
        #label0.setStyleSheet("border-radius : 100px; background-color: white")
        #pixmap = QPixmap("img.png")
        #label0.setPixmap(pixmap)
        #label0.move(670, 150)
        #label0.resize(200, 200)



        # search textbox

        searchBox = QLineEdit(self)
        searchBox.setPlaceholderText("Search")
        searchBox.setFont(QFont('Arial', 12))
        searchBox.move(620, 405)
        searchBox.setGeometry(1050, 70, 280, 40)
        searchBox.setStyleSheet("border-radius : 20px; background-color: #eadade; color: #536e8f; padding-left: 20px")


        # the table

        headertabel = QTableWidget(self)
        headertabel.setColumnCount(4)
        headertabel.setRowCount(1)
        headertabel.setItem(0,0, QTableWidgetItem("Student ID"))
        headertabel.setItem(0,1, QTableWidgetItem("Student Name"))
        headertabel.setItem(0,2, QTableWidgetItem("Student Year"))
        headertabel.setItem(0,3, QTableWidgetItem("Student Department"))
        headertabel.resizeRowToContents(4)
        headertabel.setFont(QFont("Times", 10))
        headertabel.setGeometry(340, 250, 1010, 46)

        headertabel.setStyleSheet("QTableWidget { border: 0px; background-color: white; color: #536e8f; border-radius : 20px;}")
        headertabel.horizontalHeader().setVisible(False)
        headertabel.verticalHeader().setVisible(False)
        headertabel.setShowGrid(False)

        tableWidget = QTableWidget(self)
        tableWidget.setRowCount(5)
        tableWidget.setColumnCount(4)
        tableWidget.setItem(0,0, QTableWidgetItem("11067"))
        tableWidget.setItem(0,1, QTableWidgetItem("Shahd Ahmed Ragab"))
        tableWidget.setItem(1,0, QTableWidgetItem("14675"))
        tableWidget.setItem(1,1, QTableWidgetItem("Hassnaa hussam"))
        tableWidget.setItem(2,0, QTableWidgetItem("14789"))
        tableWidget.setItem(2,1, QTableWidgetItem("Ayat Tarek"))
        tableWidget.setItem(3,0, QTableWidgetItem("10923"))
        tableWidget.setItem(3,1, QTableWidgetItem("Eman Abd El-Azeem"))

        tableWidget.setItem(0,2, QTableWidgetItem("second"))
        tableWidget.setItem(1,2, QTableWidgetItem("third"))
        tableWidget.setItem(2,2, QTableWidgetItem("first"))
        tableWidget.setItem(3,2, QTableWidgetItem("fourth"))
        tableWidget.setItem(0,3, QTableWidgetItem("SBE"))
        tableWidget.setItem(2,3, QTableWidgetItem("ARC"))
        tableWidget.setItem(1,3, QTableWidgetItem("CMP"))
        tableWidget.setItem(3,3, QTableWidgetItem("CVE"))
        tableWidget.resizeColumnToContents(10)
        tableWidget.resizeColumnToContents(5)

        tableWidget.setFont(QFont("Times", 10))
        tableWidget.horizontalHeader().setVisible(False)
        tableWidget.verticalHeader().setVisible(False)
        tableWidget.setShowGrid(False)


        # Table will fit the screen horizontally
        tableWidget.setGeometry(340, 310, 1010, 600)
        tableWidget.setStyleSheet("QTableWidget { border: 0px; background-color: white; color: #536e8f; border-radius : 15px;}")


        self.showMaximized()






App = QApplication(sys.argv)


window = Window()


sys.exit(App.exec())




