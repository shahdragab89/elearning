from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLineEdit,
    QInputDialog,
    QApplication,
    QLabel,
)
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class login_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 20, 1200, 1000)
        self.setWindowTitle("Edraak")
        self.UiComponents()
        self.show()

    def UiComponents(self):
        QFontDatabase.addApplicationFont("./ProtestRiot-Regular.ttf")
        p = QPalette()
        gradient = QLinearGradient(0, 0, 200, 800)
        gradient.setColorAt(0.25, QColor(234, 218, 222))
        gradient.setColorAt(0.5, QColor(200, 186, 211))
        gradient.setColorAt(0.75, QColor(166, 149, 183))
        # gradient.setColorAt(0.75, QColor(178, 214, 205))
        gradient.setColorAt(1.0, QColor(122, 135, 184))


        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

        self.label = QLabel(self)
        self.label.setStyleSheet(
            "border-radius : 80px; background-color: rgba(255, 255, 255,0.3);"
        )
        self.label.move(510, 165)
        self.label.resize(515, 755)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(100)
        shadow.setOffset(0, 0)
        self.label.setGraphicsEffect(shadow)

        self.label0 = QLabel(self)
        self.label0.setStyleSheet(
            "border-radius : 100px; background-color: rgba(63,71,105)"
        )
        self.pixmap = QPixmap("person.png")
        self.label0.setPixmap(self.pixmap)
        self.label0.move(670, 50)
        self.label0.resize(200, 200)
        self.label0.setAlignment(QtCore.Qt.AlignCenter)


        self.textbox1 = QLabel(self)
        self.textbox1.move(620, 305)
        self.textbox1.resize(300, 50)
        self.textbox1.setText("Shahd")
        self.textbox1.setFont(QFont("Protest Riot", 12))
        self.textbox1.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(620, 385)
        self.textbox2.resize(300, 50)
        self.textbox2.setPlaceholderText("Last Name")
        self.textbox2.setFont(QFont("Protest Riot", 12))
        self.textbox2.setStyleSheet(
            "border-radius : 25px;background-color: rgba(255,255,255,0.7) ; padding-left: 65px"
        )
        #self.textbox2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.ageBox = QLineEdit(self)
        self.ageBox.move(620, 465)
        self.ageBox.resize(145, 50)
        self.ageBox.setPlaceholderText("Age")
        self.ageBox.setFont(QFont("Protest Riot", 12))
        self.ageBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )


        self.modBox = QLineEdit(self)
        self.modBox.move(620, 545)
        self.modBox.resize(300, 50)
        self.modBox.setPlaceholderText("Phone Number")
        self.modBox.setFont(QFont("Protest Riot", 12))
        self.modBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )


        self.mailBox = QLineEdit(self)
        self.mailBox.move(620, 625)
        self.mailBox.resize(300, 50)
        self.mailBox.setPlaceholderText("Email")
        self.mailBox.setFont(QFont("Protest Riot", 12))
        self.mailBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )


        self.gradeBox = QLineEdit(self)
        self.gradeBox.move(775, 465)
        self.gradeBox.resize(145, 50)
        self.gradeBox.setPlaceholderText("Grade")
        self.gradeBox.setFont(QFont("Protest Riot", 12))
        self.gradeBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )

        self.DepBox = QLineEdit(self)
        self.DepBox.move(620, 705)
        self.DepBox.resize(300, 50)
        self.DepBox.setPlaceholderText("Department")
        self.DepBox.setFont(QFont("Protest Riot", 12))
        self.DepBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )



        self.btn = QPushButton(self)
        self.btn.setText("Add")
        self.btn.setFont(QFont("Protest Riot", 15))
        self.btn.resize(190, 50)
        self.btn.move(670, 800)
        self.btn.setStyleSheet(
            "border-radius : 25px;background-color: rgba(63,71,105) ;color:white; bold"
        )
        self.btn.setCursor(Qt.PointingHandCursor)


        self.label1 = QLabel(self)
        self.label1.setStyleSheet(
            "border-radius : 30px; background-color: rgba(63,71,105)"
        )
        self.pixmap = QPixmap("./images\person1.png")
        self.label1.setPixmap(self.pixmap)
        self.label1.move(620, 400)
        self.label1.resize(60, 60)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)



        self.label4 = QLabel(self)
        self.pixmap = QPixmap("./images\download-removebg-preview.png")
        self.label4.setPixmap(self.pixmap)
        self.label4.move(40, 40)
        self.label4.resize(150, 90)


app = QApplication(sys.argv)
window = login_window()
sys.exit(app.exec_())