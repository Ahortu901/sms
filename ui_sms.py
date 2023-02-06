# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'smsGuOceO.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)
import src_rc

class Ui_SMS(object):
    def setupUi(self, SMS):
        if not SMS.objectName():
            SMS.setObjectName(u"SMS")
        SMS.setWindowModality(Qt.ApplicationModal)
        SMS.resize(1197, 700)
        SMS.setMinimumSize(QSize(1197, 700))
        SMS.setMaximumSize(QSize(1197, 700))
        icon = QIcon()
        icon.addFile(u"assets/imgs/myLogo2.jpg", QSize(), QIcon.Normal, QIcon.Off)
        SMS.setWindowIcon(icon)
        self.centralwidget = QWidget(SMS)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.verticalLayout_2 = QVBoxLayout(self.login)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.loginFrame = QFrame(self.login)
        self.loginFrame.setObjectName(u"loginFrame")
        self.loginFrame.setFrameShape(QFrame.NoFrame)
        self.loginFrame.setFrameShadow(QFrame.Raised)
        self.loginFrame.setLineWidth(0)
        self.label = QLabel(self.loginFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, -10, 1221, 701))
        self.label.setPixmap(QPixmap(u"assets/imgs/header.jpg"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.loginFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 150, 1191, 51))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(21)
        font.setBold(True)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 21pt \"Roboto\";")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.loginFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(410, 310, 101, 31))
        self.label_3.setStyleSheet(u"font: 700 14pt \"Sarai\";\n"
"color: rgb(238, 238, 236);")
        self.login_username = QLineEdit(self.loginFrame)
        self.login_username.setObjectName(u"login_username")
        self.login_username.setGeometry(QRect(520, 300, 191, 41))
        self.label_4 = QLabel(self.loginFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(410, 390, 101, 31))
        self.label_4.setStyleSheet(u"font: 700 14pt \"Sarai\";\n"
"color: rgb(238, 238, 236);")
        self.login_password = QLineEdit(self.loginFrame)
        self.login_password.setObjectName(u"login_password")
        self.login_password.setGeometry(QRect(520, 380, 191, 41))
        self.login_password.setEchoMode(QLineEdit.Password)
        self.login_2 = QPushButton(self.loginFrame)
        self.login_2.setObjectName(u"login_2")
        self.login_2.setGeometry(QRect(500, 450, 161, 41))
        self.login_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_2.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"	font: 700 20pt \"System-ui\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(78, 154, 6);\n"
"}")
        self.label_5 = QLabel(self.loginFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(470, 560, 251, 20))
        self.label_5.setStyleSheet(u"color: rgb(239, 41, 41);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.login_3 = QPushButton(self.loginFrame)
        self.login_3.setObjectName(u"login_3")
        self.login_3.setGeometry(QRect(500, 600, 201, 41))
        self.login_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(211, 215, 207);\n"
"	color: rgb(46, 52, 54);\n"
"	font: 700 12pt \"System-ui\";\n"
"border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(78, 154, 6);\n"
"}")
        icon1 = QIcon()
        iconThemeName = u"go-next"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.login_3.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.loginFrame)

        self.tabWidget.addTab(self.login, "")
        self.signUp = QWidget()
        self.signUp.setObjectName(u"signUp")
        self.label_6 = QLabel(self.signUp)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(-4, -14, 1211, 711))
        self.label_6.setPixmap(QPixmap(u"assets/imgs/header.jpg"))
        self.label_6.setScaledContents(True)
        self.label_7 = QLabel(self.signUp)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 130, 1191, 51))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 21pt \"Roboto\";")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.singup = QPushButton(self.signUp)
        self.singup.setObjectName(u"singup")
        self.singup.setGeometry(QRect(510, 500, 161, 41))
        self.singup.setCursor(QCursor(Qt.PointingHandCursor))
        self.singup.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"font: 700 15pt \"simple-line-icons\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(78, 154, 6);\n"
"}")
        self.login_password_2 = QLineEdit(self.signUp)
        self.login_password_2.setObjectName(u"login_password_2")
        self.login_password_2.setGeometry(QRect(580, 390, 191, 41))
        self.login_password_2.setEchoMode(QLineEdit.Password)
        self.label_8 = QLabel(self.signUp)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(430, 220, 101, 31))
        self.label_8.setStyleSheet(u"font: 700 14pt \"Sarai\";\n"
"color: rgb(238, 238, 236);")
        self.login_username_2 = QLineEdit(self.signUp)
        self.login_username_2.setObjectName(u"login_username_2")
        self.login_username_2.setGeometry(QRect(580, 210, 191, 41))
        self.label_9 = QLabel(self.signUp)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(430, 400, 101, 31))
        self.label_9.setStyleSheet(u"font: 700 14pt \"Sarai\";\n"
"color: rgb(238, 238, 236);")
        self.label_10 = QLabel(self.signUp)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(430, 280, 101, 31))
        self.label_10.setStyleSheet(u"font: 700 14pt \"Sarai\";\n"
"color: rgb(238, 238, 236);")
        self.login_username_3 = QLineEdit(self.signUp)
        self.login_username_3.setObjectName(u"login_username_3")
        self.login_username_3.setGeometry(QRect(580, 270, 191, 41))
        self.login_password_3 = QLineEdit(self.signUp)
        self.login_password_3.setObjectName(u"login_password_3")
        self.login_password_3.setGeometry(QRect(580, 450, 191, 41))
        self.login_password_3.setEchoMode(QLineEdit.Password)
        self.label_11 = QLabel(self.signUp)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(430, 460, 141, 31))
        self.label_11.setStyleSheet(u"font: 700 14pt \"Sarai\";\n"
"color: rgb(238, 238, 236);")
        self.label_12 = QLabel(self.signUp)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(480, 580, 251, 20))
        self.label_12.setStyleSheet(u"color: rgb(239, 41, 41);")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_43 = QLabel(self.signUp)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(430, 340, 101, 31))
        self.label_43.setStyleSheet(u"font: 700 14pt \"Sarai\";\n"
"color: rgb(238, 238, 236);")
        self.login_username_4 = QLineEdit(self.signUp)
        self.login_username_4.setObjectName(u"login_username_4")
        self.login_username_4.setGeometry(QRect(580, 330, 191, 41))
        self.login_4 = QPushButton(self.signUp)
        self.login_4.setObjectName(u"login_4")
        self.login_4.setGeometry(QRect(500, 610, 201, 41))
        self.login_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(211, 215, 207);\n"
"	color: rgb(46, 52, 54);\n"
"	font: 700 12pt \"System-ui\";\n"
"border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(78, 154, 6);\n"
"}")
        self.login_4.setIcon(icon1)
        self.tabWidget.addTab(self.signUp, "")
        self.mainDashboard = QWidget()
        self.mainDashboard.setObjectName(u"mainDashboard")
        self.verticalLayout_3 = QVBoxLayout(self.mainDashboard)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.main_framWork = QFrame(self.mainDashboard)
        self.main_framWork.setObjectName(u"main_framWork")
        self.main_framWork.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgba(100, 98, 157, 183);")
        self.main_framWork.setFrameShape(QFrame.NoFrame)
        self.main_framWork.setFrameShadow(QFrame.Raised)
        self.main_framWork.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.main_framWork)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 9, 9, 9)
        self.nav_Frame = QFrame(self.main_framWork)
        self.nav_Frame.setObjectName(u"nav_Frame")
        self.nav_Frame.setStyleSheet(u"border-radius: 0px;\n"
"background-color: transparent;")
        self.nav_Frame.setFrameShape(QFrame.NoFrame)
        self.nav_Frame.setFrameShadow(QFrame.Raised)
        self.label_13 = QLabel(self.nav_Frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, -30, 161, 141))
        self.label_13.setStyleSheet(u"background-color: transparent;")
        self.label_13.setPixmap(QPixmap(u"assets/imgs/myLogo.jpg"))
        self.label_13.setScaledContents(True)
        self.frame_7 = QFrame(self.nav_Frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 80, 251, 561))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"background-color:transparent ;\n"
"}\n"
"QPushButton{\n"
"selection-background-color: rgba(235, 166, 166, 194);\n"
"background-color:transparent ;\n"
"color: rgb(255, 255, 255);\n"
"font: 900 12pt \"Roboto\";\n"
"text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"	border-top-left-radius: 12px;\n"
"	background-color: rgb(115, 210, 22);\n"
"}")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.dashboard_2 = QPushButton(self.frame_7)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setGeometry(QRect(10, 60, 251, 41))
        self.dashboard_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.dashboard_2.setStyleSheet(u"selection-background-color: rgba(235, 166, 166, 194);")
        icon2 = QIcon()
        icon2.addFile(u"assets/buttons/grid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_2.setIcon(icon2)
        self.dashboard_2.setIconSize(QSize(30, 30))
        self.student_fees_2 = QPushButton(self.frame_7)
        self.student_fees_2.setObjectName(u"student_fees_2")
        self.student_fees_2.setGeometry(QRect(10, 310, 251, 41))
        self.student_fees_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.student_fees_2.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"assets/buttons/codesandbox.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.student_fees_2.setIcon(icon3)
        self.student_fees_2.setIconSize(QSize(30, 30))
        self.logout = QPushButton(self.frame_7)
        self.logout.setObjectName(u"logout")
        self.logout.setGeometry(QRect(10, 510, 251, 41))
        self.logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.logout.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"assets/buttons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logout.setIcon(icon4)
        self.logout.setIconSize(QSize(30, 30))
        self.student_fees = QPushButton(self.frame_7)
        self.student_fees.setObjectName(u"student_fees")
        self.student_fees.setGeometry(QRect(10, 260, 251, 41))
        self.student_fees.setCursor(QCursor(Qt.PointingHandCursor))
        self.student_fees.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"assets/buttons/command.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.student_fees.setIcon(icon5)
        self.student_fees.setIconSize(QSize(30, 30))
        self.student_marks = QPushButton(self.frame_7)
        self.student_marks.setObjectName(u"student_marks")
        self.student_marks.setGeometry(QRect(10, 210, 251, 41))
        self.student_marks.setCursor(QCursor(Qt.PointingHandCursor))
        self.student_marks.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u"assets/buttons/clipboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.student_marks.setIcon(icon6)
        self.student_marks.setIconSize(QSize(30, 30))
        self.expenses = QPushButton(self.frame_7)
        self.expenses.setObjectName(u"expenses")
        self.expenses.setGeometry(QRect(10, 430, 251, 41))
        self.expenses.setCursor(QCursor(Qt.PointingHandCursor))
        self.expenses.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u"assets/buttons/trending-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.expenses.setIcon(icon7)
        self.expenses.setIconSize(QSize(30, 30))
        self.add_student = QPushButton(self.frame_7)
        self.add_student.setObjectName(u"add_student")
        self.add_student.setGeometry(QRect(10, 110, 251, 41))
        self.add_student.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_student.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u"assets/buttons/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_student.setIcon(icon8)
        self.add_student.setIconSize(QSize(30, 30))
        self.edit_student = QPushButton(self.frame_7)
        self.edit_student.setObjectName(u"edit_student")
        self.edit_student.setGeometry(QRect(10, 160, 251, 41))
        self.edit_student.setCursor(QCursor(Qt.PointingHandCursor))
        self.edit_student.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u"assets/buttons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_student.setIcon(icon9)
        self.edit_student.setIconSize(QSize(30, 30))
        self.attendance = QPushButton(self.frame_7)
        self.attendance.setObjectName(u"attendance")
        self.attendance.setGeometry(QRect(10, 360, 251, 41))
        self.attendance.setCursor(QCursor(Qt.PointingHandCursor))
        self.attendance.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u"assets/buttons/layers.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.attendance.setIcon(icon10)
        self.attendance.setIconSize(QSize(30, 30))
        self.send_email = QPushButton(self.frame_7)
        self.send_email.setObjectName(u"send_email")
        self.send_email.setGeometry(QRect(10, 470, 251, 41))
        self.send_email.setCursor(QCursor(Qt.PointingHandCursor))
        self.send_email.setStyleSheet(u"")
        icon11 = QIcon()
        icon11.addFile(u"assets/buttons/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.send_email.setIcon(icon11)
        self.send_email.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.nav_Frame)

        self.frame_2 = QFrame(self.main_framWork)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(243, 243, 243);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2 = QTabWidget(self.frame_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setStyleSheet(u"border-radius: 0px;\n"
"background-color: rgb(238, 238, 236);")
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.frame_3 = QFrame(self.dashboard)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(70, 50, 501, 161))
        self.frame_3.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgba(214, 205, 205, 221);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_91 = QLabel(self.frame_3)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(190, 30, 211, 31))
        self.label_91.setStyleSheet(u"background-color: transparent;")
        self.label_91.setAlignment(Qt.AlignCenter)
        self.label_92 = QLabel(self.frame_3)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setGeometry(QRect(190, 70, 211, 31))
        self.label_92.setStyleSheet(u"background-color: transparent;")
        self.label_92.setAlignment(Qt.AlignCenter)
        self.label_93 = QLabel(self.frame_3)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setGeometry(QRect(190, 110, 211, 31))
        self.label_93.setStyleSheet(u"background-color: transparent;")
        self.label_93.setAlignment(Qt.AlignCenter)
        self.label_94 = QLabel(self.frame_3)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setGeometry(QRect(20, 30, 111, 91))
        self.label_94.setStyleSheet(u"background-color: transparent;")
        self.label_94.setPixmap(QPixmap(u"assets/imgs/icon.png"))
        self.label_94.setScaledContents(True)
        self.label_94.setAlignment(Qt.AlignCenter)
        self.tableWidget_7 = QTableWidget(self.dashboard)
        if (self.tableWidget_7.columnCount() < 9):
            self.tableWidget_7.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget_7.setObjectName(u"tableWidget_7")
        self.tableWidget_7.setGeometry(QRect(0, 380, 611, 231))
        self.student_name_11 = QLineEdit(self.dashboard)
        self.student_name_11.setObjectName(u"student_name_11")
        self.student_name_11.setGeometry(QRect(10, 330, 171, 31))
        self.student_name_11.setStyleSheet(u"background-color: rgb(136, 138, 133);\n"
"color: rgb(255, 255, 255);")
        self.student_name_11.setClearButtonEnabled(False)
        self.btn_search_5 = QPushButton(self.dashboard)
        self.btn_search_5.setObjectName(u"btn_search_5")
        self.btn_search_5.setGeometry(QRect(190, 330, 91, 31))
        self.btn_search_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_search_5.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(237, 212, 0);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-right-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(138, 226, 52);\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"assets/buttons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search_5.setIcon(icon12)
        self.btn_search_5.setIconSize(QSize(20, 20))
        self.tabWidget_2.addTab(self.dashboard, "")
        self.registration = QWidget()
        self.registration.setObjectName(u"registration")
        self.registration_number = QLineEdit(self.registration)
        self.registration_number.setObjectName(u"registration_number")
        self.registration_number.setGeometry(QRect(200, 60, 171, 31))
        self.registration_number.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);\n"
"border-radius: 12px;")
        self.label_21 = QLabel(self.registration)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(30, 260, 101, 31))
        self.label_21.setStyleSheet(u"background-color: transparent;")
        self.student_address = QTextEdit(self.registration)
        self.student_address.setObjectName(u"student_address")
        self.student_address.setGeometry(QRect(140, 310, 141, 71))
        self.student_address.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);\n"
"border-top-left-radius:12px;\n"
"")
        self.DOB = QLineEdit(self.registration)
        self.DOB.setObjectName(u"DOB")
        self.DOB.setGeometry(QRect(140, 160, 171, 31))
        self.DOB.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);")
        self.DOB.setClearButtonEnabled(True)
        self.student_gender = QComboBox(self.registration)
        self.student_gender.addItem("")
        self.student_gender.addItem("")
        self.student_gender.setObjectName(u"student_gender")
        self.student_gender.setGeometry(QRect(140, 260, 171, 31))
        self.student_gender.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);\n"
"border-top-left-radius:12px;")
        self.label_22 = QLabel(self.registration)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(30, 210, 101, 31))
        self.label_22.setStyleSheet(u"background-color: transparent;")
        self.label_23 = QLabel(self.registration)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(30, 330, 121, 31))
        self.label_23.setStyleSheet(u"background-color: transparent;")
        self.label_26 = QLabel(self.registration)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(30, 110, 91, 31))
        self.label_26.setStyleSheet(u"background-color: transparent;")
        self.label_24 = QLabel(self.registration)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(30, 60, 161, 31))
        self.label_24.setStyleSheet(u"background-color: transparent;")
        self.student_name = QLineEdit(self.registration)
        self.student_name.setObjectName(u"student_name")
        self.student_name.setGeometry(QRect(140, 110, 171, 31))
        self.student_name.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);")
        self.student_name.setClearButtonEnabled(True)
        self.student_class = QComboBox(self.registration)
        self.student_class.addItem("")
        self.student_class.addItem("")
        self.student_class.addItem("")
        self.student_class.addItem("")
        self.student_class.addItem("")
        self.student_class.addItem("")
        self.student_class.addItem("")
        self.student_class.addItem("")
        self.student_class.addItem("")
        self.student_class.addItem("")
        self.student_class.addItem("")
        self.student_class.addItem("")
        self.student_class.addItem("")
        self.student_class.addItem("")
        self.student_class.setObjectName(u"student_class")
        self.student_class.setGeometry(QRect(140, 210, 171, 31))
        self.student_class.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);\n"
"border-top-left-radius:12px;")
        self.label_25 = QLabel(self.registration)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(30, 160, 111, 31))
        self.label_25.setStyleSheet(u"background-color: transparent;")
        self.label_27 = QLabel(self.registration)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(-4, 0, 631, 31))
        self.label_27.setStyleSheet(u"font: 700 17pt \"Roboto\";\n"
"background-color: transparent;")
        self.label_27.setAlignment(Qt.AlignCenter)
        self.tableWidget = QTableWidget(self.registration)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem17)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 410, 611, 201))
        self.parentName = QLineEdit(self.registration)
        self.parentName.setObjectName(u"parentName")
        self.parentName.setGeometry(QRect(440, 190, 171, 31))
        self.parentName.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);")
        self.parentName.setClearButtonEnabled(True)
        self.label_28 = QLabel(self.registration)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(340, 190, 101, 31))
        self.label_28.setStyleSheet(u"background-color: transparent;")
        self.parent_number = QLineEdit(self.registration)
        self.parent_number.setObjectName(u"parent_number")
        self.parent_number.setGeometry(QRect(440, 240, 171, 31))
        self.parent_number.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);")
        self.parent_number.setClearButtonEnabled(True)
        self.label_29 = QLabel(self.registration)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(340, 240, 101, 31))
        self.label_29.setStyleSheet(u"background-color: transparent;")
        self.label_30 = QLabel(self.registration)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(330, 290, 111, 31))
        self.label_30.setStyleSheet(u"background-color: transparent;")
        self.parentEmail = QLineEdit(self.registration)
        self.parentEmail.setObjectName(u"parentEmail")
        self.parentEmail.setGeometry(QRect(440, 290, 171, 31))
        self.parentEmail.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);")
        self.parentEmail.setClearButtonEnabled(True)
        self.btn_register = QPushButton(self.registration)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setGeometry(QRect(360, 344, 141, 41))
        self.btn_register.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_register.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(214, 205, 205, 221);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-right-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(138, 226, 52);\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u"assets/buttons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_register.setIcon(icon13)
        self.btn_register.setIconSize(QSize(20, 20))
        self.tabWidget_2.addTab(self.registration, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_31 = QLabel(self.tab_3)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(-4, 0, 631, 31))
        self.label_31.setStyleSheet(u"font: 700 17pt \"Roboto\";\n"
"background-color: transparent;")
        self.label_31.setAlignment(Qt.AlignCenter)
        self.label_32 = QLabel(self.tab_3)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 100, 161, 31))
        self.label_32.setStyleSheet(u"background-color: transparent;")
        self.student_class_2 = QComboBox(self.tab_3)
        self.student_class_2.addItem("")
        self.student_class_2.addItem("")
        self.student_class_2.addItem("")
        self.student_class_2.addItem("")
        self.student_class_2.addItem("")
        self.student_class_2.addItem("")
        self.student_class_2.addItem("")
        self.student_class_2.addItem("")
        self.student_class_2.addItem("")
        self.student_class_2.addItem("")
        self.student_class_2.addItem("")
        self.student_class_2.addItem("")
        self.student_class_2.addItem("")
        self.student_class_2.addItem("")
        self.student_class_2.setObjectName(u"student_class_2")
        self.student_class_2.setGeometry(QRect(130, 250, 171, 31))
        self.student_class_2.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);\n"
"border-top-left-radius:12px;")
        self.label_33 = QLabel(self.tab_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(30, 300, 101, 31))
        self.label_33.setStyleSheet(u"background-color: transparent;")
        self.student_address_2 = QTextEdit(self.tab_3)
        self.student_address_2.setObjectName(u"student_address_2")
        self.student_address_2.setGeometry(QRect(140, 350, 141, 71))
        self.student_address_2.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);\n"
"border-top-left-radius:12px;\n"
"")
        self.label_34 = QLabel(self.tab_3)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(30, 150, 91, 31))
        self.label_34.setStyleSheet(u"background-color: transparent;")
        self.student_name_2 = QLineEdit(self.tab_3)
        self.student_name_2.setObjectName(u"student_name_2")
        self.student_name_2.setGeometry(QRect(130, 150, 171, 31))
        self.student_name_2.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);")
        self.student_name_2.setClearButtonEnabled(True)
        self.label_35 = QLabel(self.tab_3)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(30, 250, 101, 31))
        self.label_35.setStyleSheet(u"background-color: transparent;")
        self.label_36 = QLabel(self.tab_3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(30, 200, 111, 31))
        self.label_36.setStyleSheet(u"background-color: transparent;")
        self.student_gender_2 = QComboBox(self.tab_3)
        self.student_gender_2.addItem("")
        self.student_gender_2.addItem("")
        self.student_gender_2.setObjectName(u"student_gender_2")
        self.student_gender_2.setGeometry(QRect(130, 300, 171, 31))
        self.student_gender_2.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);\n"
"border-top-left-radius:12px;")
        self.label_37 = QLabel(self.tab_3)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(30, 370, 121, 31))
        self.label_37.setStyleSheet(u"background-color: transparent;")
        self.tableWidget_2 = QTableWidget(self.tab_3)
        if (self.tableWidget_2.columnCount() < 9):
            self.tableWidget_2.setColumnCount(9)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem26)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(0, 430, 611, 201))
        self.DOB_2 = QLineEdit(self.tab_3)
        self.DOB_2.setObjectName(u"DOB_2")
        self.DOB_2.setGeometry(QRect(130, 200, 171, 31))
        self.DOB_2.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);")
        self.DOB_2.setClearButtonEnabled(True)
        self.registration_number_2 = QLineEdit(self.tab_3)
        self.registration_number_2.setObjectName(u"registration_number_2")
        self.registration_number_2.setGeometry(QRect(170, 100, 171, 31))
        self.registration_number_2.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);\n"
"border-radius: 12px;")
        self.student_name_3 = QLineEdit(self.tab_3)
        self.student_name_3.setObjectName(u"student_name_3")
        self.student_name_3.setGeometry(QRect(310, 60, 171, 31))
        self.student_name_3.setStyleSheet(u"background-color: rgb(136, 138, 133);\n"
"color: rgb(255, 255, 255);")
        self.student_name_3.setClearButtonEnabled(False)
        self.btn_search = QPushButton(self.tab_3)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setGeometry(QRect(490, 60, 91, 31))
        self.btn_search.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_search.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(237, 212, 0);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-right-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(138, 226, 52);\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}")
        self.btn_search.setIcon(icon12)
        self.btn_search.setIconSize(QSize(20, 20))
        self.btn_delete = QPushButton(self.tab_3)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(360, 320, 141, 41))
        self.btn_delete.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(204, 0, 0);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-right-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(138, 226, 52);\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u"assets/buttons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete.setIcon(icon14)
        self.btn_delete.setIconSize(QSize(20, 20))
        self.btn_update_2 = QPushButton(self.tab_3)
        self.btn_update_2.setObjectName(u"btn_update_2")
        self.btn_update_2.setGeometry(QRect(360, 270, 141, 41))
        self.btn_update_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_update_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(214, 205, 205, 221);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-right-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(138, 226, 52);\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u"assets/buttons/edit-3.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_update_2.setIcon(icon15)
        self.btn_update_2.setIconSize(QSize(20, 20))
        self.tabWidget_2.addTab(self.tab_3, "")
        self.studentMarks = QWidget()
        self.studentMarks.setObjectName(u"studentMarks")
        self.student_class_5 = QComboBox(self.studentMarks)
        self.student_class_5.addItem("")
        self.student_class_5.addItem("")
        self.student_class_5.addItem("")
        self.student_class_5.addItem("")
        self.student_class_5.addItem("")
        self.student_class_5.addItem("")
        self.student_class_5.addItem("")
        self.student_class_5.addItem("")
        self.student_class_5.addItem("")
        self.student_class_5.addItem("")
        self.student_class_5.addItem("")
        self.student_class_5.addItem("")
        self.student_class_5.addItem("")
        self.student_class_5.addItem("")
        self.student_class_5.setObjectName(u"student_class_5")
        self.student_class_5.setGeometry(QRect(130, 210, 171, 31))
        self.student_class_5.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);\n"
"border-top-left-radius:12px;")
        self.student_subject = QComboBox(self.studentMarks)
        self.student_subject.addItem("")
        self.student_subject.addItem("")
        self.student_subject.addItem("")
        self.student_subject.addItem("")
        self.student_subject.addItem("")
        self.student_subject.addItem("")
        self.student_subject.addItem("")
        self.student_subject.addItem("")
        self.student_subject.addItem("")
        self.student_subject.addItem("")
        self.student_subject.addItem("")
        self.student_subject.addItem("")
        self.student_subject.addItem("")
        self.student_subject.addItem("")
        self.student_subject.addItem("")
        self.student_subject.addItem("")
        self.student_subject.addItem("")
        self.student_subject.addItem("")
        self.student_subject.addItem("")
        self.student_subject.setObjectName(u"student_subject")
        self.student_subject.setGeometry(QRect(130, 310, 171, 31))
        self.student_subject.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);\n"
"border-top-left-radius:12px;")
        self.student_name_4 = QLineEdit(self.studentMarks)
        self.student_name_4.setObjectName(u"student_name_4")
        self.student_name_4.setGeometry(QRect(330, 110, 171, 31))
        self.student_name_4.setStyleSheet(u"background-color: rgb(136, 138, 133);\n"
"color: rgb(255, 255, 255);")
        self.student_name_4.setClearButtonEnabled(False)
        self.student_name_5 = QLineEdit(self.studentMarks)
        self.student_name_5.setObjectName(u"student_name_5")
        self.student_name_5.setGeometry(QRect(130, 110, 171, 31))
        self.student_name_5.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);")
        self.student_name_5.setClearButtonEnabled(True)
        self.label_38 = QLabel(self.studentMarks)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(30, 160, 111, 31))
        self.label_38.setStyleSheet(u"background-color: transparent;")
        self.tableWidget_3 = QTableWidget(self.studentMarks)
        if (self.tableWidget_3.columnCount() < 7):
            self.tableWidget_3.setColumnCount(7)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem33)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(10, 400, 611, 201))
        self.registration_number_3 = QLineEdit(self.studentMarks)
        self.registration_number_3.setObjectName(u"registration_number_3")
        self.registration_number_3.setGeometry(QRect(170, 60, 171, 31))
        self.registration_number_3.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);\n"
"border-radius: 12px;")
        self.marks = QLineEdit(self.studentMarks)
        self.marks.setObjectName(u"marks")
        self.marks.setGeometry(QRect(130, 160, 171, 31))
        self.marks.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);")
        self.marks.setClearButtonEnabled(True)
        self.label_39 = QLabel(self.studentMarks)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(10, 60, 161, 31))
        self.label_39.setStyleSheet(u"background-color: transparent;")
        self.label_40 = QLabel(self.studentMarks)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(30, 210, 101, 31))
        self.label_40.setStyleSheet(u"background-color: transparent;")
        self.btn_search_2 = QPushButton(self.studentMarks)
        self.btn_search_2.setObjectName(u"btn_search_2")
        self.btn_search_2.setGeometry(QRect(510, 110, 91, 31))
        self.btn_search_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_search_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(237, 212, 0);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-right-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(138, 226, 52);\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}")
        self.btn_search_2.setIcon(icon12)
        self.btn_search_2.setIconSize(QSize(20, 20))
        self.btn_delete_2 = QPushButton(self.studentMarks)
        self.btn_delete_2.setObjectName(u"btn_delete_2")
        self.btn_delete_2.setGeometry(QRect(390, 330, 141, 41))
        self.btn_delete_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(204, 0, 0);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-right-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(138, 226, 52);\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}")
        self.btn_delete_2.setIcon(icon14)
        self.btn_delete_2.setIconSize(QSize(20, 20))
        self.label_41 = QLabel(self.studentMarks)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(30, 110, 91, 31))
        self.label_41.setStyleSheet(u"background-color: transparent;")
        self.label_42 = QLabel(self.studentMarks)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(30, 260, 111, 31))
        self.label_42.setStyleSheet(u"background-color: transparent;")
        self.label_65 = QLabel(self.studentMarks)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(30, 310, 91, 31))
        self.label_65.setStyleSheet(u"background-color: transparent;")
        self.schoo_term = QComboBox(self.studentMarks)
        self.schoo_term.addItem("")
        self.schoo_term.addItem("")
        self.schoo_term.addItem("")
        self.schoo_term.setObjectName(u"schoo_term")
        self.schoo_term.setGeometry(QRect(130, 360, 171, 31))
        self.schoo_term.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);\n"
"border-top-left-radius:12px;")
        self.marks_type = QComboBox(self.studentMarks)
        self.marks_type.addItem("")
        self.marks_type.addItem("")
        self.marks_type.addItem("")
        self.marks_type.setObjectName(u"marks_type")
        self.marks_type.setGeometry(QRect(130, 260, 171, 31))
        self.marks_type.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);\n"
"border-top-left-radius:12px;")
        self.label_66 = QLabel(self.studentMarks)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(30, 360, 91, 31))
        self.label_66.setStyleSheet(u"background-color: transparent;")
        self.btn_register_9 = QPushButton(self.studentMarks)
        self.btn_register_9.setObjectName(u"btn_register_9")
        self.btn_register_9.setGeometry(QRect(390, 250, 141, 41))
        self.btn_register_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_register_9.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(214, 205, 205, 221);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-right-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(138, 226, 52);\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}")
        self.btn_register_9.setIcon(icon13)
        self.btn_register_9.setIconSize(QSize(20, 20))
        self.label_71 = QLabel(self.studentMarks)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(-10, 0, 631, 31))
        self.label_71.setStyleSheet(u"font: 700 17pt \"Roboto\";\n"
"background-color: transparent;")
        self.label_71.setAlignment(Qt.AlignCenter)
        self.tabWidget_2.addTab(self.studentMarks, "")
        self.studentFees = QWidget()
        self.studentFees.setObjectName(u"studentFees")
        self.label_67 = QLabel(self.studentFees)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(30, 170, 111, 31))
        self.label_67.setStyleSheet(u"background-color: transparent;")
        self.student_name_12 = QLineEdit(self.studentFees)
        self.student_name_12.setObjectName(u"student_name_12")
        self.student_name_12.setGeometry(QRect(130, 70, 171, 31))
        self.student_name_12.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);")
        self.student_name_12.setClearButtonEnabled(True)
        self.student_class_6 = QComboBox(self.studentFees)
        self.student_class_6.addItem("")
        self.student_class_6.addItem("")
        self.student_class_6.addItem("")
        self.student_class_6.addItem("")
        self.student_class_6.addItem("")
        self.student_class_6.addItem("")
        self.student_class_6.addItem("")
        self.student_class_6.addItem("")
        self.student_class_6.addItem("")
        self.student_class_6.addItem("")
        self.student_class_6.addItem("")
        self.student_class_6.addItem("")
        self.student_class_6.addItem("")
        self.student_class_6.addItem("")
        self.student_class_6.setObjectName(u"student_class_6")
        self.student_class_6.setGeometry(QRect(130, 120, 171, 31))
        self.student_class_6.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);\n"
"border-top-left-radius:12px;")
        self.label_68 = QLabel(self.studentFees)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(30, 70, 91, 31))
        self.label_68.setStyleSheet(u"background-color: transparent;")
        self.label_69 = QLabel(self.studentFees)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(30, 220, 91, 31))
        self.label_69.setStyleSheet(u"background-color: transparent;")
        self.tableWidget_8 = QTableWidget(self.studentFees)
        if (self.tableWidget_8.columnCount() < 6):
            self.tableWidget_8.setColumnCount(6)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(3, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(4, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(5, __qtablewidgetitem39)
        self.tableWidget_8.setObjectName(u"tableWidget_8")
        self.tableWidget_8.setGeometry(QRect(0, 390, 611, 201))
        self.fees_type = QComboBox(self.studentFees)
        self.fees_type.addItem("")
        self.fees_type.addItem("")
        self.fees_type.addItem("")
        self.fees_type.setObjectName(u"fees_type")
        self.fees_type.setGeometry(QRect(130, 170, 171, 31))
        self.fees_type.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);\n"
"border-top-left-radius:12px;")
        self.schoo_term_2 = QComboBox(self.studentFees)
        self.schoo_term_2.addItem("")
        self.schoo_term_2.addItem("")
        self.schoo_term_2.addItem("")
        self.schoo_term_2.setObjectName(u"schoo_term_2")
        self.schoo_term_2.setGeometry(QRect(130, 220, 171, 31))
        self.schoo_term_2.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);\n"
"border-top-left-radius:12px;")
        self.label_70 = QLabel(self.studentFees)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(-10, 0, 631, 31))
        self.label_70.setStyleSheet(u"font: 700 17pt \"Roboto\";\n"
"background-color: transparent;")
        self.label_70.setAlignment(Qt.AlignCenter)
        self.label_72 = QLabel(self.studentFees)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(30, 120, 91, 31))
        self.label_72.setStyleSheet(u"background-color: transparent;")
        self.label_73 = QLabel(self.studentFees)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(30, 270, 91, 31))
        self.label_73.setStyleSheet(u"background-color: transparent;")
        self.amount_Paid = QLineEdit(self.studentFees)
        self.amount_Paid.setObjectName(u"amount_Paid")
        self.amount_Paid.setGeometry(QRect(130, 270, 171, 31))
        self.amount_Paid.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);")
        self.amount_Paid.setClearButtonEnabled(True)
        self.label_74 = QLabel(self.studentFees)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(30, 320, 91, 31))
        self.label_74.setStyleSheet(u"background-color: transparent;")
        self.paymentDate = QLineEdit(self.studentFees)
        self.paymentDate.setObjectName(u"paymentDate")
        self.paymentDate.setGeometry(QRect(130, 320, 171, 31))
        self.paymentDate.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);")
        self.paymentDate.setClearButtonEnabled(True)
        self.btn_search_6 = QPushButton(self.studentFees)
        self.btn_search_6.setObjectName(u"btn_search_6")
        self.btn_search_6.setGeometry(QRect(520, 100, 91, 31))
        self.btn_search_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_search_6.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(237, 212, 0);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-right-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(138, 226, 52);\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}")
        self.btn_search_6.setIcon(icon12)
        self.btn_search_6.setIconSize(QSize(20, 20))
        self.payment_search = QLineEdit(self.studentFees)
        self.payment_search.setObjectName(u"payment_search")
        self.payment_search.setGeometry(QRect(340, 100, 171, 31))
        self.payment_search.setStyleSheet(u"background-color: rgb(136, 138, 133);\n"
"color: rgb(255, 255, 255);")
        self.payment_search.setClearButtonEnabled(False)
        self.btn_register_10 = QPushButton(self.studentFees)
        self.btn_register_10.setObjectName(u"btn_register_10")
        self.btn_register_10.setGeometry(QRect(400, 250, 141, 41))
        self.btn_register_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_register_10.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(214, 205, 205, 221);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-right-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(138, 226, 52);\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}")
        self.btn_register_10.setIcon(icon13)
        self.btn_register_10.setIconSize(QSize(20, 20))
        self.btn_delete_5 = QPushButton(self.studentFees)
        self.btn_delete_5.setObjectName(u"btn_delete_5")
        self.btn_delete_5.setGeometry(QRect(400, 320, 141, 41))
        self.btn_delete_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_5.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(204, 0, 0);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-right-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(138, 226, 52);\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}")
        self.btn_delete_5.setIcon(icon14)
        self.btn_delete_5.setIconSize(QSize(20, 20))
        self.tabWidget_2.addTab(self.studentFees, "")
        self.attendance1 = QWidget()
        self.attendance1.setObjectName(u"attendance1")
        self.btn_register_11 = QPushButton(self.attendance1)
        self.btn_register_11.setObjectName(u"btn_register_11")
        self.btn_register_11.setGeometry(QRect(430, 190, 141, 41))
        self.btn_register_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_register_11.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(214, 205, 205, 221);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-right-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(138, 226, 52);\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}")
        self.btn_register_11.setIcon(icon13)
        self.btn_register_11.setIconSize(QSize(20, 20))
        self.btn_update_4 = QPushButton(self.attendance1)
        self.btn_update_4.setObjectName(u"btn_update_4")
        self.btn_update_4.setGeometry(QRect(430, 250, 141, 41))
        self.btn_update_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_update_4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(214, 205, 205, 221);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-right-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(138, 226, 52);\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}")
        self.btn_update_4.setIcon(icon15)
        self.btn_update_4.setIconSize(QSize(20, 20))
        self.btn_delete_6 = QPushButton(self.attendance1)
        self.btn_delete_6.setObjectName(u"btn_delete_6")
        self.btn_delete_6.setGeometry(QRect(430, 310, 141, 41))
        self.btn_delete_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_6.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(204, 0, 0);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-right-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(138, 226, 52);\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}")
        self.btn_delete_6.setIcon(icon14)
        self.btn_delete_6.setIconSize(QSize(20, 20))
        self.label_75 = QLabel(self.attendance1)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(60, 160, 161, 31))
        self.label_75.setStyleSheet(u"background-color: transparent;")
        self.label_76 = QLabel(self.attendance1)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(80, 260, 101, 31))
        self.label_76.setStyleSheet(u"background-color: transparent;")
        self.student_name_14 = QLineEdit(self.attendance1)
        self.student_name_14.setObjectName(u"student_name_14")
        self.student_name_14.setGeometry(QRect(180, 210, 171, 31))
        self.student_name_14.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);")
        self.student_name_14.setClearButtonEnabled(True)
        self.tableWidget_9 = QTableWidget(self.attendance1)
        if (self.tableWidget_9.columnCount() < 4):
            self.tableWidget_9.setColumnCount(4)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(2, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(3, __qtablewidgetitem43)
        self.tableWidget_9.setObjectName(u"tableWidget_9")
        self.tableWidget_9.setGeometry(QRect(110, 400, 401, 201))
        self.btn_search_7 = QPushButton(self.attendance1)
        self.btn_search_7.setObjectName(u"btn_search_7")
        self.btn_search_7.setGeometry(QRect(510, 60, 91, 31))
        self.btn_search_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_search_7.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(237, 212, 0);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-right-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(138, 226, 52);\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}")
        self.btn_search_7.setIcon(icon12)
        self.btn_search_7.setIconSize(QSize(20, 20))
        self.attendance_search = QLineEdit(self.attendance1)
        self.attendance_search.setObjectName(u"attendance_search")
        self.attendance_search.setGeometry(QRect(330, 60, 171, 31))
        self.attendance_search.setStyleSheet(u"background-color: rgb(136, 138, 133);\n"
"color: rgb(255, 255, 255);")
        self.attendance_search.setClearButtonEnabled(False)
        self.label_77 = QLabel(self.attendance1)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(80, 210, 91, 31))
        self.label_77.setStyleSheet(u"background-color: transparent;")
        self.student_class_7 = QComboBox(self.attendance1)
        self.student_class_7.addItem("")
        self.student_class_7.addItem("")
        self.student_class_7.addItem("")
        self.student_class_7.addItem("")
        self.student_class_7.addItem("")
        self.student_class_7.addItem("")
        self.student_class_7.addItem("")
        self.student_class_7.addItem("")
        self.student_class_7.addItem("")
        self.student_class_7.addItem("")
        self.student_class_7.addItem("")
        self.student_class_7.addItem("")
        self.student_class_7.addItem("")
        self.student_class_7.addItem("")
        self.student_class_7.setObjectName(u"student_class_7")
        self.student_class_7.setGeometry(QRect(180, 260, 171, 31))
        self.student_class_7.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);\n"
"border-top-left-radius:12px;")
        self.registration_number_7 = QLineEdit(self.attendance1)
        self.registration_number_7.setObjectName(u"registration_number_7")
        self.registration_number_7.setGeometry(QRect(220, 160, 171, 31))
        self.registration_number_7.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);\n"
"border-radius: 12px;")
        self.paymentDate_2 = QLineEdit(self.attendance1)
        self.paymentDate_2.setObjectName(u"paymentDate_2")
        self.paymentDate_2.setGeometry(QRect(180, 310, 171, 31))
        self.paymentDate_2.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);")
        self.paymentDate_2.setClearButtonEnabled(True)
        self.label_78 = QLabel(self.attendance1)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(80, 310, 91, 31))
        self.label_78.setStyleSheet(u"background-color: transparent;")
        self.label_79 = QLabel(self.attendance1)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(0, 10, 631, 31))
        self.label_79.setStyleSheet(u"font: 700 17pt \"Roboto\";\n"
"background-color: transparent;")
        self.label_79.setAlignment(Qt.AlignCenter)
        self.tabWidget_2.addTab(self.attendance1, "")
        self.expenses1 = QWidget()
        self.expenses1.setObjectName(u"expenses1")
        self.get_expensesType = QLineEdit(self.expenses1)
        self.get_expensesType.setObjectName(u"get_expensesType")
        self.get_expensesType.setGeometry(QRect(130, 270, 171, 31))
        self.get_expensesType.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);")
        self.label_80 = QLabel(self.expenses1)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(10, 280, 111, 20))
        self.label_80.setStyleSheet(u"background-color: transparent;")
        self.label_81 = QLabel(self.expenses1)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(10, 330, 71, 20))
        self.label_81.setStyleSheet(u"background-color: transparent;\n"
"")
        self.get_amount = QLineEdit(self.expenses1)
        self.get_amount.setObjectName(u"get_amount")
        self.get_amount.setGeometry(QRect(130, 320, 171, 31))
        self.get_amount.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);")
        self.label_82 = QLabel(self.expenses1)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(10, 230, 121, 20))
        self.label_82.setStyleSheet(u"background-color: transparent;")
        self.get_expenses = QComboBox(self.expenses1)
        self.get_expenses.addItem("")
        self.get_expenses.addItem("")
        self.get_expenses.addItem("")
        self.get_expenses.setObjectName(u"get_expenses")
        self.get_expenses.setGeometry(QRect(130, 220, 171, 31))
        self.get_expenses.setCursor(QCursor(Qt.OpenHandCursor))
        self.get_expenses.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);\n"
"border-top-left-radius:12px;")
        self.label_1585 = QLabel(self.expenses1)
        self.label_1585.setObjectName(u"label_1585")
        self.label_1585.setGeometry(QRect(10, 90, 121, 31))
        self.label_1585.setStyleSheet(u"background-color: transparent;")
        self.main_feedingFees = QLabel(self.expenses1)
        self.main_feedingFees.setObjectName(u"main_feedingFees")
        self.main_feedingFees.setGeometry(QRect(110, 130, 211, 31))
        self.main_feedingFees.setStyleSheet(u"color: rgb(135, 68, 0);\n"
"background-color: rgb(185, 185, 185);\n"
"font: 900 12pt \"Roboto\";")
        self.main_feedingFees.setAlignment(Qt.AlignCenter)
        self.main_schoolFees = QLabel(self.expenses1)
        self.main_schoolFees.setObjectName(u"main_schoolFees")
        self.main_schoolFees.setGeometry(QRect(110, 90, 211, 31))
        self.main_schoolFees.setStyleSheet(u"color: rgb(135, 68, 0);\n"
"background-color: rgb(185, 185, 185);\n"
"font: 900 12pt \"Roboto\";")
        self.main_schoolFees.setAlignment(Qt.AlignCenter)
        self.label_84 = QLabel(self.expenses1)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(10, 130, 121, 31))
        self.label_84.setStyleSheet(u"background-color: transparent;")
        self.main_studiesFees = QLabel(self.expenses1)
        self.main_studiesFees.setObjectName(u"main_studiesFees")
        self.main_studiesFees.setGeometry(QRect(110, 50, 211, 31))
        self.main_studiesFees.setStyleSheet(u"color: rgb(135, 68, 0);\n"
"background-color: rgb(185, 185, 185);\n"
"font: 900 12pt \"Roboto\";")
        self.main_studiesFees.setAlignment(Qt.AlignCenter)
        self.label_86 = QLabel(self.expenses1)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(10, 50, 121, 31))
        self.label_86.setStyleSheet(u"background-color: transparent;")
        self.schoolFees = QLabel(self.expenses1)
        self.schoolFees.setObjectName(u"schoolFees")
        self.schoolFees.setGeometry(QRect(440, 340, 181, 31))
        self.schoolFees.setStyleSheet(u"\n"
"color: rgb(0, 170, 0);\n"
"font: 900 12pt \"Roboto\";")
        self.schoolFees.setAlignment(Qt.AlignCenter)
        self.feedingFees = QLabel(self.expenses1)
        self.feedingFees.setObjectName(u"feedingFees")
        self.feedingFees.setGeometry(QRect(440, 380, 181, 31))
        self.feedingFees.setStyleSheet(u"\n"
"color: rgb(0, 170, 0);\n"
"font: 900 12pt \"Roboto\";")
        self.feedingFees.setAlignment(Qt.AlignCenter)
        self.studiesFees = QLabel(self.expenses1)
        self.studiesFees.setObjectName(u"studiesFees")
        self.studiesFees.setGeometry(QRect(440, 420, 181, 31))
        self.studiesFees.setStyleSheet(u"\n"
"color: rgb(0, 170, 0);\n"
"font: 900 12pt \"Roboto\";")
        self.studiesFees.setAlignment(Qt.AlignCenter)
        self.label_87 = QLabel(self.expenses1)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setGeometry(QRect(480, 470, 91, 31))
        self.label_87.setStyleSheet(u"background-color: transparent;")
        self.label_88 = QLabel(self.expenses1)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setGeometry(QRect(0, 480, 161, 31))
        self.label_88.setStyleSheet(u"background-color: transparent;")
        self.from_studiesFees = QLabel(self.expenses1)
        self.from_studiesFees.setObjectName(u"from_studiesFees")
        self.from_studiesFees.setGeometry(QRect(150, 520, 161, 31))
        self.from_studiesFees.setStyleSheet(u"\n"
"color: rgb(229, 153, 0);")
        self.from_studiesFees.setAlignment(Qt.AlignCenter)
        self.label_89 = QLabel(self.expenses1)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setGeometry(QRect(0, 520, 161, 31))
        self.label_89.setStyleSheet(u"background-color: transparent;")
        self.label_90 = QLabel(self.expenses1)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setGeometry(QRect(10, 560, 81, 31))
        self.label_90.setStyleSheet(u"background-color: transparent;")
        self.from_feedingFees = QLabel(self.expenses1)
        self.from_feedingFees.setObjectName(u"from_feedingFees")
        self.from_feedingFees.setGeometry(QRect(150, 480, 161, 31))
        self.from_feedingFees.setStyleSheet(u"\n"
"color: rgb(229, 153, 0);")
        self.from_feedingFees.setAlignment(Qt.AlignCenter)
        self.label_96 = QLabel(self.expenses1)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setGeometry(QRect(490, 300, 51, 31))
        self.label_96.setStyleSheet(u"background-color: transparent;")
        self.label_97 = QLabel(self.expenses1)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(10, 440, 161, 31))
        self.label_97.setStyleSheet(u"background-color: transparent;")
        self.from_schoolFees = QLabel(self.expenses1)
        self.from_schoolFees.setObjectName(u"from_schoolFees")
        self.from_schoolFees.setGeometry(QRect(150, 440, 161, 31))
        self.from_schoolFees.setStyleSheet(u"\n"
"color: rgb(229, 153, 0);")
        self.from_schoolFees.setAlignment(Qt.AlignCenter)
        self.label_99 = QLabel(self.expenses1)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(340, 380, 111, 31))
        self.label_99.setStyleSheet(u"background-color: transparent;")
        self.balanceFees = QLabel(self.expenses1)
        self.balanceFees.setObjectName(u"balanceFees")
        self.balanceFees.setGeometry(QRect(400, 510, 211, 31))
        self.balanceFees.setStyleSheet(u"background-color: rgb(156, 78, 0);\n"
"color: rgb(188, 188, 188);\n"
"font: 900 12pt \"Roboto\";")
        self.balanceFees.setAlignment(Qt.AlignCenter)
        self.label_101 = QLabel(self.expenses1)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setGeometry(QRect(340, 340, 101, 31))
        self.label_101.setStyleSheet(u"background-color: transparent;")
        self.label_102 = QLabel(self.expenses1)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setGeometry(QRect(340, 420, 101, 31))
        self.label_102.setStyleSheet(u"background-color: transparent;")
        self.total_expenses = QLabel(self.expenses1)
        self.total_expenses.setObjectName(u"total_expenses")
        self.total_expenses.setGeometry(QRect(110, 560, 201, 31))
        self.total_expenses.setStyleSheet(u"color: rgb(166, 166, 166);\n"
"background-color: rgb(170, 0, 0);\n"
"font: 900 12pt \"Roboto\";")
        self.total_expenses.setAlignment(Qt.AlignCenter)
        self.add_schholFees = QPushButton(self.expenses1)
        self.add_schholFees.setObjectName(u"add_schholFees")
        self.add_schholFees.setGeometry(QRect(400, 130, 161, 41))
        self.add_schholFees.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_schholFees.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(214, 205, 205, 221);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-right-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(138, 226, 52);\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}")
        self.add_schholFees.setIcon(icon13)
        self.add_schholFees.setIconSize(QSize(20, 20))
        self.add_studiesFees = QPushButton(self.expenses1)
        self.add_studiesFees.setObjectName(u"add_studiesFees")
        self.add_studiesFees.setGeometry(QRect(400, 180, 161, 41))
        self.add_studiesFees.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_studiesFees.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(214, 205, 205, 221);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-right-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(138, 226, 52);\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}")
        self.add_studiesFees.setIcon(icon13)
        self.add_studiesFees.setIconSize(QSize(20, 20))
        self.add_feedingFees = QPushButton(self.expenses1)
        self.add_feedingFees.setObjectName(u"add_feedingFees")
        self.add_feedingFees.setGeometry(QRect(400, 230, 161, 41))
        self.add_feedingFees.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_feedingFees.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(214, 205, 205, 221);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-right-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(138, 226, 52);\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}")
        self.add_feedingFees.setIcon(icon13)
        self.add_feedingFees.setIconSize(QSize(20, 20))
        self.label_104 = QLabel(self.expenses1)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setGeometry(QRect(60, 170, 201, 61))
        self.label_104.setStyleSheet(u"background-color: transparent;")
        self.label_104.setAlignment(Qt.AlignCenter)
        self.tabWidget_2.addTab(self.expenses1, "")
        self.email = QWidget()
        self.email.setObjectName(u"email")
        self.get_expensesType_2 = QLineEdit(self.email)
        self.get_expensesType_2.setObjectName(u"get_expensesType_2")
        self.get_expensesType_2.setGeometry(QRect(150, 50, 171, 31))
        self.get_expensesType_2.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);")
        self.label_83 = QLabel(self.email)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(20, 50, 121, 31))
        self.label_83.setStyleSheet(u"background-color: transparent;")
        self.label_85 = QLabel(self.email)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(380, 49, 61, 31))
        self.label_85.setStyleSheet(u"background-color: transparent;")
        self.get_expensesType_3 = QLineEdit(self.email)
        self.get_expensesType_3.setObjectName(u"get_expensesType_3")
        self.get_expensesType_3.setGeometry(QRect(420, 50, 171, 31))
        self.get_expensesType_3.setStyleSheet(u"background-color: rgba(241, 185, 119, 181);")
        self.textEdit = QTextEdit(self.email)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(90, 110, 451, 381))
        self.textEdit.setStyleSheet(u"background-color: rgba(241, 185, 119, 97);\n"
"color: rgb(255, 255, 255);")
        self.textEdit.setFrameShape(QFrame.Box)
        self.textEdit.setFrameShadow(QFrame.Raised)
        self.textEdit.setLineWidth(1)
        self.textEdit.setMidLineWidth(0)
        self.add_schholFees_2 = QPushButton(self.email)
        self.add_schholFees_2.setObjectName(u"add_schholFees_2")
        self.add_schholFees_2.setGeometry(QRect(250, 540, 161, 41))
        self.add_schholFees_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_schholFees_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(214, 205, 205, 221);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-right-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(138, 226, 52);\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u"assets/buttons/send.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_schholFees_2.setIcon(icon16)
        self.add_schholFees_2.setIconSize(QSize(20, 20))
        self.tabWidget_2.addTab(self.email, "")

        self.horizontalLayout_2.addWidget(self.tabWidget_2)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(211, 215, 207);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(206, 70, 91, 81))
        self.label_16.setPixmap(QPixmap(u"assets/imgs/student.png"))
        self.label_16.setScaledContents(True)
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 60, 251, 41))
        self.label_15.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(78, 154, 6);\n"
"font: 700 15pt \"Ubuntu\";")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 40, 251, 41))
        self.label_14.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(78, 154, 6);\n"
"font: 700 15pt \"Ubuntu\";")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(40, 150, 221, 111))
        self.frame_5.setStyleSheet(u"background-color: rgba(241, 185, 119, 97);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(6, 10, 211, 20))
        self.label_17.setStyleSheet(u"background-color: transparent;")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 29, 201, 81))
        self.label_18.setStyleSheet(u"background-color: transparent;")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(40, 280, 221, 111))
        self.frame_6.setStyleSheet(u"background-color: rgba(100, 98, 157, 183);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_19 = QLabel(self.frame_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(6, 10, 211, 20))
        self.label_19.setStyleSheet(u"background-color: transparent;")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_20 = QLabel(self.frame_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 29, 201, 81))
        self.label_20.setStyleSheet(u"background-color: transparent;")
        self.label_20.setAlignment(Qt.AlignCenter)
        self.calendarWidget = QCalendarWidget(self.frame)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(20, 390, 281, 221))
        self.calendarWidget.setLayoutDirection(Qt.LeftToRight)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setSelectionMode(QCalendarWidget.NoSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 10, 41, 41))
        self.pushButton.setStyleSheet(u"QFrame{\n"
"background-color:transparent ;\n"
"}\n"
"QPushButton{\n"
"background-color:transparent ;\n"
"color: rgb(255, 255, 255);\n"
"font: 900 12pt \"Roboto\";\n"
"}\n"
"QPushButton:hover{\n"
"	border-top-left-radius: 12px;\n"
"	background-color: rgb(239, 41, 41);\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u"assets/buttons/x-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon17)
        self.pushButton.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.frame)

        self.horizontalLayout_2.setStretch(0, 8)
        self.horizontalLayout_2.setStretch(1, 4)

        self.horizontalLayout.addWidget(self.frame_2)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 11)

        self.verticalLayout_3.addWidget(self.main_framWork)

        self.tabWidget.addTab(self.mainDashboard, "")

        self.verticalLayout.addWidget(self.tabWidget)

        SMS.setCentralWidget(self.centralwidget)

        self.retranslateUi(SMS)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SMS)
    # setupUi

    def retranslateUi(self, SMS):
        SMS.setWindowTitle(QCoreApplication.translate("SMS", u"School Management System", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("SMS", u"PLEASE LOGIN", None))
        self.label_3.setText(QCoreApplication.translate("SMS", u"User name :", None))
        self.label_4.setText(QCoreApplication.translate("SMS", u"Password :", None))
        self.login_2.setText(QCoreApplication.translate("SMS", u"Login", None))
        self.label_5.setText(QCoreApplication.translate("SMS", u"Do not have an account", None))
        self.login_3.setText(QCoreApplication.translate("SMS", u"Create new account", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.login), QCoreApplication.translate("SMS", u"login", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("SMS", u"Create an account to login", None))
        self.singup.setText(QCoreApplication.translate("SMS", u"SignUp", None))
        self.label_8.setText(QCoreApplication.translate("SMS", u"Full name :", None))
        self.label_9.setText(QCoreApplication.translate("SMS", u"Password :", None))
        self.label_10.setText(QCoreApplication.translate("SMS", u"User name :", None))
        self.label_11.setText(QCoreApplication.translate("SMS", u"Re-enter password :", None))
        self.label_12.setText(QCoreApplication.translate("SMS", u"Already have account", None))
        self.label_43.setText(QCoreApplication.translate("SMS", u"Email Address :", None))
        self.login_4.setText(QCoreApplication.translate("SMS", u"Go to login page", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.signUp), QCoreApplication.translate("SMS", u"signUp", None))
        self.label_13.setText("")
        self.dashboard_2.setText(QCoreApplication.translate("SMS", u"Dashboard", None))
        self.student_fees_2.setText(QCoreApplication.translate("SMS", u"Student Report", None))
        self.logout.setText(QCoreApplication.translate("SMS", u"LogOut", None))
        self.student_fees.setText(QCoreApplication.translate("SMS", u"Student Fees", None))
        self.student_marks.setText(QCoreApplication.translate("SMS", u"Student Marks", None))
        self.expenses.setText(QCoreApplication.translate("SMS", u"Expenses", None))
        self.add_student.setText(QCoreApplication.translate("SMS", u"Add Student", None))
        self.edit_student.setText(QCoreApplication.translate("SMS", u"Edit Student", None))
        self.attendance.setText(QCoreApplication.translate("SMS", u"Attendance", None))
        self.send_email.setText(QCoreApplication.translate("SMS", u"Send Email", None))
        self.label_91.setText(QCoreApplication.translate("SMS", u"School Management System", None))
        self.label_92.setText(QCoreApplication.translate("SMS", u"For more details please", None))
        self.label_93.setText(QCoreApplication.translate("SMS", u"Contact the Developers", None))
        self.label_94.setText("")
        ___qtablewidgetitem = self.tableWidget_7.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SMS", u"Reg_N0:", None));
        ___qtablewidgetitem1 = self.tableWidget_7.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SMS", u"Full Name", None));
        ___qtablewidgetitem2 = self.tableWidget_7.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SMS", u"Date of Birth", None));
        ___qtablewidgetitem3 = self.tableWidget_7.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SMS", u"Class", None));
        ___qtablewidgetitem4 = self.tableWidget_7.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("SMS", u"Gender", None));
        ___qtablewidgetitem5 = self.tableWidget_7.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("SMS", u"Home Address", None));
        ___qtablewidgetitem6 = self.tableWidget_7.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("SMS", u"Parent Name", None));
        ___qtablewidgetitem7 = self.tableWidget_7.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("SMS", u"Telephone", None));
        ___qtablewidgetitem8 = self.tableWidget_7.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("SMS", u"Email Address", None));
        self.student_name_11.setPlaceholderText(QCoreApplication.translate("SMS", u"searching...", None))
        self.btn_search_5.setText(QCoreApplication.translate("SMS", u"Search", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.dashboard), QCoreApplication.translate("SMS", u"dashboard", None))
        self.label_21.setText(QCoreApplication.translate("SMS", u"Gender :", None))
        self.student_address.setPlaceholderText("")
        self.DOB.setPlaceholderText("")
        self.student_gender.setItemText(0, QCoreApplication.translate("SMS", u"Male", None))
        self.student_gender.setItemText(1, QCoreApplication.translate("SMS", u"Female", None))

        self.student_gender.setPlaceholderText(QCoreApplication.translate("SMS", u"gender.....", None))
        self.label_22.setText(QCoreApplication.translate("SMS", u"Class :", None))
        self.label_23.setText(QCoreApplication.translate("SMS", u"Home Address :", None))
        self.label_26.setText(QCoreApplication.translate("SMS", u"Full Name :", None))
        self.label_24.setText(QCoreApplication.translate("SMS", u"Registration Number :", None))
        self.student_class.setItemText(0, QCoreApplication.translate("SMS", u"Crache", None))
        self.student_class.setItemText(1, QCoreApplication.translate("SMS", u"Nursery 1", None))
        self.student_class.setItemText(2, QCoreApplication.translate("SMS", u"Nursery 2", None))
        self.student_class.setItemText(3, QCoreApplication.translate("SMS", u"Kindergaten 1", None))
        self.student_class.setItemText(4, QCoreApplication.translate("SMS", u"Kindergaten 2", None))
        self.student_class.setItemText(5, QCoreApplication.translate("SMS", u"Class 1", None))
        self.student_class.setItemText(6, QCoreApplication.translate("SMS", u"Class 2", None))
        self.student_class.setItemText(7, QCoreApplication.translate("SMS", u"Class 3", None))
        self.student_class.setItemText(8, QCoreApplication.translate("SMS", u"Class 4", None))
        self.student_class.setItemText(9, QCoreApplication.translate("SMS", u"Class 5", None))
        self.student_class.setItemText(10, QCoreApplication.translate("SMS", u"Class 6", None))
        self.student_class.setItemText(11, QCoreApplication.translate("SMS", u"JHS 1", None))
        self.student_class.setItemText(12, QCoreApplication.translate("SMS", u"JHS 2", None))
        self.student_class.setItemText(13, QCoreApplication.translate("SMS", u"JHS 3", None))

        self.student_class.setPlaceholderText(QCoreApplication.translate("SMS", u"class .....", None))
        self.label_25.setText(QCoreApplication.translate("SMS", u"Date Of Birth :", None))
        self.label_27.setText(QCoreApplication.translate("SMS", u"Student Registration", None))
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("SMS", u"Reg_N0:", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("SMS", u"Full Name", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("SMS", u"Date of Birth", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("SMS", u"Class", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("SMS", u"Gender", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("SMS", u"Home Address", None));
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("SMS", u"Parent Name", None));
        ___qtablewidgetitem16 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("SMS", u"Telephone", None));
        ___qtablewidgetitem17 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("SMS", u"Email Address", None));
        self.label_28.setText(QCoreApplication.translate("SMS", u"Parent Name :", None))
        self.label_29.setText(QCoreApplication.translate("SMS", u"Telephone :", None))
        self.label_30.setText(QCoreApplication.translate("SMS", u"Email Address :", None))
        self.btn_register.setText(QCoreApplication.translate("SMS", u"Save Details", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.registration), QCoreApplication.translate("SMS", u"registration", None))
        self.label_31.setText(QCoreApplication.translate("SMS", u"Update / Delete Student Details", None))
        self.label_32.setText(QCoreApplication.translate("SMS", u"Registration Number :", None))
        self.student_class_2.setItemText(0, QCoreApplication.translate("SMS", u"Crache", None))
        self.student_class_2.setItemText(1, QCoreApplication.translate("SMS", u"Nursery 1", None))
        self.student_class_2.setItemText(2, QCoreApplication.translate("SMS", u"Nursery 2", None))
        self.student_class_2.setItemText(3, QCoreApplication.translate("SMS", u"Kindergaten 1", None))
        self.student_class_2.setItemText(4, QCoreApplication.translate("SMS", u"Kindergaten 2", None))
        self.student_class_2.setItemText(5, QCoreApplication.translate("SMS", u"Class 1", None))
        self.student_class_2.setItemText(6, QCoreApplication.translate("SMS", u"Class 2", None))
        self.student_class_2.setItemText(7, QCoreApplication.translate("SMS", u"Class 3", None))
        self.student_class_2.setItemText(8, QCoreApplication.translate("SMS", u"Class 4", None))
        self.student_class_2.setItemText(9, QCoreApplication.translate("SMS", u"Class 5", None))
        self.student_class_2.setItemText(10, QCoreApplication.translate("SMS", u"Class 6", None))
        self.student_class_2.setItemText(11, QCoreApplication.translate("SMS", u"JHS 1", None))
        self.student_class_2.setItemText(12, QCoreApplication.translate("SMS", u"JHS 2", None))
        self.student_class_2.setItemText(13, QCoreApplication.translate("SMS", u"JHS 3", None))

        self.student_class_2.setPlaceholderText(QCoreApplication.translate("SMS", u"class .....", None))
        self.label_33.setText(QCoreApplication.translate("SMS", u"Gender :", None))
        self.student_address_2.setPlaceholderText("")
        self.label_34.setText(QCoreApplication.translate("SMS", u"Full Name :", None))
        self.label_35.setText(QCoreApplication.translate("SMS", u"Class :", None))
        self.label_36.setText(QCoreApplication.translate("SMS", u"Date Of Birth :", None))
        self.student_gender_2.setItemText(0, QCoreApplication.translate("SMS", u"Male", None))
        self.student_gender_2.setItemText(1, QCoreApplication.translate("SMS", u"Female", None))

        self.student_gender_2.setPlaceholderText(QCoreApplication.translate("SMS", u"gender.....", None))
        self.label_37.setText(QCoreApplication.translate("SMS", u"Home Address :", None))
        ___qtablewidgetitem18 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("SMS", u"Reg_N0:", None));
        ___qtablewidgetitem19 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("SMS", u"Full Name", None));
        ___qtablewidgetitem20 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("SMS", u"Date of Birth", None));
        ___qtablewidgetitem21 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("SMS", u"Class", None));
        ___qtablewidgetitem22 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("SMS", u"Gender", None));
        ___qtablewidgetitem23 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("SMS", u"Home Address", None));
        ___qtablewidgetitem24 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("SMS", u"Parent Name", None));
        ___qtablewidgetitem25 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("SMS", u"Telephone", None));
        ___qtablewidgetitem26 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("SMS", u"Email Address", None));
        self.DOB_2.setPlaceholderText("")
        self.student_name_3.setPlaceholderText(QCoreApplication.translate("SMS", u"searching...", None))
        self.btn_search.setText(QCoreApplication.translate("SMS", u"Search", None))
        self.btn_delete.setText(QCoreApplication.translate("SMS", u"Delete Details", None))
        self.btn_update_2.setText(QCoreApplication.translate("SMS", u"Update Details", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("SMS", u"edit/delete", None))
        self.student_class_5.setItemText(0, QCoreApplication.translate("SMS", u"Crache", None))
        self.student_class_5.setItemText(1, QCoreApplication.translate("SMS", u"Nursery 1", None))
        self.student_class_5.setItemText(2, QCoreApplication.translate("SMS", u"Nursery 2", None))
        self.student_class_5.setItemText(3, QCoreApplication.translate("SMS", u"Kindergaten 1", None))
        self.student_class_5.setItemText(4, QCoreApplication.translate("SMS", u"Kindergaten 2", None))
        self.student_class_5.setItemText(5, QCoreApplication.translate("SMS", u"Class 1", None))
        self.student_class_5.setItemText(6, QCoreApplication.translate("SMS", u"Class 2", None))
        self.student_class_5.setItemText(7, QCoreApplication.translate("SMS", u"Class 3", None))
        self.student_class_5.setItemText(8, QCoreApplication.translate("SMS", u"Class 4", None))
        self.student_class_5.setItemText(9, QCoreApplication.translate("SMS", u"Class 5", None))
        self.student_class_5.setItemText(10, QCoreApplication.translate("SMS", u"Class 6", None))
        self.student_class_5.setItemText(11, QCoreApplication.translate("SMS", u"JHS 1", None))
        self.student_class_5.setItemText(12, QCoreApplication.translate("SMS", u"JHS 2", None))
        self.student_class_5.setItemText(13, QCoreApplication.translate("SMS", u"JHS 3", None))

        self.student_class_5.setPlaceholderText(QCoreApplication.translate("SMS", u"class .....", None))
        self.student_subject.setItemText(0, QCoreApplication.translate("SMS", u"English Language", None))
        self.student_subject.setItemText(1, QCoreApplication.translate("SMS", u"Mathematics", None))
        self.student_subject.setItemText(2, QCoreApplication.translate("SMS", u"Intergrated Science", None))
        self.student_subject.setItemText(3, QCoreApplication.translate("SMS", u"Computing", None))
        self.student_subject.setItemText(4, QCoreApplication.translate("SMS", u"Social Studies", None))
        self.student_subject.setItemText(5, QCoreApplication.translate("SMS", u"History", None))
        self.student_subject.setItemText(6, QCoreApplication.translate("SMS", u"Creative Arts", None))
        self.student_subject.setItemText(7, QCoreApplication.translate("SMS", u"French", None))
        self.student_subject.setItemText(8, QCoreApplication.translate("SMS", u"Ghanaian Language", None))
        self.student_subject.setItemText(9, QCoreApplication.translate("SMS", u"Basic Design and Tech.", None))
        self.student_subject.setItemText(10, QCoreApplication.translate("SMS", u"Our World Our People", None))
        self.student_subject.setItemText(11, QCoreApplication.translate("SMS", u"Religious and Moral Education", None))
        self.student_subject.setItemText(12, QCoreApplication.translate("SMS", u"Language and Oral Literacy Skills", None))
        self.student_subject.setItemText(13, QCoreApplication.translate("SMS", u"Pre-Reading Skills", None))
        self.student_subject.setItemText(14, QCoreApplication.translate("SMS", u"Pre-Writing", None))
        self.student_subject.setItemText(15, QCoreApplication.translate("SMS", u"Numeracy", None))
        self.student_subject.setItemText(16, QCoreApplication.translate("SMS", u"Health and Environment Studies", None))
        self.student_subject.setItemText(17, QCoreApplication.translate("SMS", u"Psychosocial Skills", None))
        self.student_subject.setItemText(18, QCoreApplication.translate("SMS", u"Creative Skills", None))

        self.student_subject.setPlaceholderText(QCoreApplication.translate("SMS", u"subject...", None))
        self.student_name_4.setPlaceholderText(QCoreApplication.translate("SMS", u"searching...", None))
        self.label_38.setText(QCoreApplication.translate("SMS", u"Marks :", None))
        ___qtablewidgetitem27 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("SMS", u"Reg_N0:", None));
        ___qtablewidgetitem28 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("SMS", u"Full Name", None));
        ___qtablewidgetitem29 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("SMS", u"Marks", None));
        ___qtablewidgetitem30 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("SMS", u"Class", None));
        ___qtablewidgetitem31 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("SMS", u"Marks Type", None));
        ___qtablewidgetitem32 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("SMS", u"Subject", None));
        ___qtablewidgetitem33 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("SMS", u"Term", None));
        self.marks.setPlaceholderText("")
        self.label_39.setText(QCoreApplication.translate("SMS", u"Registration Number :", None))
        self.label_40.setText(QCoreApplication.translate("SMS", u"Class :", None))
        self.btn_search_2.setText(QCoreApplication.translate("SMS", u"Search", None))
        self.btn_delete_2.setText(QCoreApplication.translate("SMS", u"Delete Details", None))
        self.label_41.setText(QCoreApplication.translate("SMS", u"Full Name :", None))
        self.label_42.setText(QCoreApplication.translate("SMS", u"Marks Type :", None))
        self.label_65.setText(QCoreApplication.translate("SMS", u"Subject :", None))
        self.schoo_term.setItemText(0, QCoreApplication.translate("SMS", u"Term 1", None))
        self.schoo_term.setItemText(1, QCoreApplication.translate("SMS", u"Term 2", None))
        self.schoo_term.setItemText(2, QCoreApplication.translate("SMS", u"Term 3", None))

        self.schoo_term.setPlaceholderText(QCoreApplication.translate("SMS", u"term ...", None))
        self.marks_type.setItemText(0, QCoreApplication.translate("SMS", u"Exams", None))
        self.marks_type.setItemText(1, QCoreApplication.translate("SMS", u"Class Work", None))
        self.marks_type.setItemText(2, QCoreApplication.translate("SMS", u"Projects", None))

        self.marks_type.setPlaceholderText(QCoreApplication.translate("SMS", u"type...", None))
        self.label_66.setText(QCoreApplication.translate("SMS", u"Term :", None))
        self.btn_register_9.setText(QCoreApplication.translate("SMS", u"Save Details", None))
        self.label_71.setText(QCoreApplication.translate("SMS", u"Student Marks", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.studentMarks), QCoreApplication.translate("SMS", u"student marks", None))
        self.label_67.setText(QCoreApplication.translate("SMS", u"Payment Type :", None))
        self.student_class_6.setItemText(0, QCoreApplication.translate("SMS", u"Crache", None))
        self.student_class_6.setItemText(1, QCoreApplication.translate("SMS", u"Nursery 1", None))
        self.student_class_6.setItemText(2, QCoreApplication.translate("SMS", u"Nursery 2", None))
        self.student_class_6.setItemText(3, QCoreApplication.translate("SMS", u"Kindergaten 1", None))
        self.student_class_6.setItemText(4, QCoreApplication.translate("SMS", u"Kindergaten 2", None))
        self.student_class_6.setItemText(5, QCoreApplication.translate("SMS", u"Class 1", None))
        self.student_class_6.setItemText(6, QCoreApplication.translate("SMS", u"Class 2", None))
        self.student_class_6.setItemText(7, QCoreApplication.translate("SMS", u"Class 3", None))
        self.student_class_6.setItemText(8, QCoreApplication.translate("SMS", u"Class 4", None))
        self.student_class_6.setItemText(9, QCoreApplication.translate("SMS", u"Class 5", None))
        self.student_class_6.setItemText(10, QCoreApplication.translate("SMS", u"Class 6", None))
        self.student_class_6.setItemText(11, QCoreApplication.translate("SMS", u"JHS 1", None))
        self.student_class_6.setItemText(12, QCoreApplication.translate("SMS", u"JHS 2", None))
        self.student_class_6.setItemText(13, QCoreApplication.translate("SMS", u"JHS 3", None))

        self.student_class_6.setPlaceholderText(QCoreApplication.translate("SMS", u"class .....", None))
        self.label_68.setText(QCoreApplication.translate("SMS", u"Full Name :", None))
        self.label_69.setText(QCoreApplication.translate("SMS", u"Term :", None))
        ___qtablewidgetitem34 = self.tableWidget_8.horizontalHeaderItem(0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("SMS", u"Full Name", None));
        ___qtablewidgetitem35 = self.tableWidget_8.horizontalHeaderItem(1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("SMS", u"Class", None));
        ___qtablewidgetitem36 = self.tableWidget_8.horizontalHeaderItem(2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("SMS", u"Payment Type", None));
        ___qtablewidgetitem37 = self.tableWidget_8.horizontalHeaderItem(3)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("SMS", u"Term", None));
        ___qtablewidgetitem38 = self.tableWidget_8.horizontalHeaderItem(4)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("SMS", u"Amount", None));
        ___qtablewidgetitem39 = self.tableWidget_8.horizontalHeaderItem(5)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("SMS", u"Date", None));
        self.fees_type.setItemText(0, QCoreApplication.translate("SMS", u"Exams Fees", None))
        self.fees_type.setItemText(1, QCoreApplication.translate("SMS", u"Fedding Fees", None))
        self.fees_type.setItemText(2, QCoreApplication.translate("SMS", u"School Fees", None))

        self.fees_type.setPlaceholderText(QCoreApplication.translate("SMS", u"type...", None))
        self.schoo_term_2.setItemText(0, QCoreApplication.translate("SMS", u"Term 1", None))
        self.schoo_term_2.setItemText(1, QCoreApplication.translate("SMS", u"Term 2", None))
        self.schoo_term_2.setItemText(2, QCoreApplication.translate("SMS", u"Term 3", None))

        self.schoo_term_2.setPlaceholderText(QCoreApplication.translate("SMS", u"term ...", None))
        self.label_70.setText(QCoreApplication.translate("SMS", u"Students Fees Payment", None))
        self.label_72.setText(QCoreApplication.translate("SMS", u"Class :", None))
        self.label_73.setText(QCoreApplication.translate("SMS", u"Amount :", None))
        self.label_74.setText(QCoreApplication.translate("SMS", u"Date :", None))
        self.btn_search_6.setText(QCoreApplication.translate("SMS", u"Search", None))
        self.payment_search.setPlaceholderText(QCoreApplication.translate("SMS", u"searching...", None))
        self.btn_register_10.setText(QCoreApplication.translate("SMS", u"Save Details", None))
        self.btn_delete_5.setText(QCoreApplication.translate("SMS", u"Delete Details", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.studentFees), QCoreApplication.translate("SMS", u"studentFees", None))
        self.btn_register_11.setText(QCoreApplication.translate("SMS", u"Save Details", None))
        self.btn_update_4.setText(QCoreApplication.translate("SMS", u"Update Details", None))
        self.btn_delete_6.setText(QCoreApplication.translate("SMS", u"Delete Details", None))
        self.label_75.setText(QCoreApplication.translate("SMS", u"Registration Number :", None))
        self.label_76.setText(QCoreApplication.translate("SMS", u"Class :", None))
        ___qtablewidgetitem40 = self.tableWidget_9.horizontalHeaderItem(0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("SMS", u"Reg_N0:", None));
        ___qtablewidgetitem41 = self.tableWidget_9.horizontalHeaderItem(1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("SMS", u"Full Name", None));
        ___qtablewidgetitem42 = self.tableWidget_9.horizontalHeaderItem(2)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("SMS", u"Class", None));
        ___qtablewidgetitem43 = self.tableWidget_9.horizontalHeaderItem(3)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("SMS", u"Date", None));
        self.btn_search_7.setText(QCoreApplication.translate("SMS", u"Search", None))
        self.attendance_search.setPlaceholderText(QCoreApplication.translate("SMS", u"searching...", None))
        self.label_77.setText(QCoreApplication.translate("SMS", u"Full Name :", None))
        self.student_class_7.setItemText(0, QCoreApplication.translate("SMS", u"Crache", None))
        self.student_class_7.setItemText(1, QCoreApplication.translate("SMS", u"Nursery 1", None))
        self.student_class_7.setItemText(2, QCoreApplication.translate("SMS", u"Nursery 2", None))
        self.student_class_7.setItemText(3, QCoreApplication.translate("SMS", u"Kindergaten 1", None))
        self.student_class_7.setItemText(4, QCoreApplication.translate("SMS", u"Kindergaten 2", None))
        self.student_class_7.setItemText(5, QCoreApplication.translate("SMS", u"Class 1", None))
        self.student_class_7.setItemText(6, QCoreApplication.translate("SMS", u"Class 2", None))
        self.student_class_7.setItemText(7, QCoreApplication.translate("SMS", u"Class 3", None))
        self.student_class_7.setItemText(8, QCoreApplication.translate("SMS", u"Class 4", None))
        self.student_class_7.setItemText(9, QCoreApplication.translate("SMS", u"Class 5", None))
        self.student_class_7.setItemText(10, QCoreApplication.translate("SMS", u"Class 6", None))
        self.student_class_7.setItemText(11, QCoreApplication.translate("SMS", u"JHS 1", None))
        self.student_class_7.setItemText(12, QCoreApplication.translate("SMS", u"JHS 2", None))
        self.student_class_7.setItemText(13, QCoreApplication.translate("SMS", u"JHS 3", None))

        self.student_class_7.setPlaceholderText(QCoreApplication.translate("SMS", u"class .....", None))
        self.label_78.setText(QCoreApplication.translate("SMS", u"Date :", None))
        self.label_79.setText(QCoreApplication.translate("SMS", u"Students Attendance", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.attendance1), QCoreApplication.translate("SMS", u"attendance", None))
        self.label_80.setText(QCoreApplication.translate("SMS", u"Expenses For :", None))
        self.label_81.setText(QCoreApplication.translate("SMS", u"Amout :", None))
        self.label_82.setText(QCoreApplication.translate("SMS", u"Expenses From :", None))
        self.get_expenses.setItemText(0, QCoreApplication.translate("SMS", u"School Fees", None))
        self.get_expenses.setItemText(1, QCoreApplication.translate("SMS", u"Feeding Fees", None))
        self.get_expenses.setItemText(2, QCoreApplication.translate("SMS", u"Studies Fees", None))

        self.get_expenses.setPlaceholderText("")
        self.label_1585.setText(QCoreApplication.translate("SMS", u"School Fees :", None))
        self.main_feedingFees.setText(QCoreApplication.translate("SMS", u"...", None))
        self.main_schoolFees.setText(QCoreApplication.translate("SMS", u"...", None))
        self.label_84.setText(QCoreApplication.translate("SMS", u"Feeding Fees :", None))
        self.main_studiesFees.setText(QCoreApplication.translate("SMS", u"...", None))
        self.label_86.setText(QCoreApplication.translate("SMS", u"Studies Fees :", None))
        self.schoolFees.setText(QCoreApplication.translate("SMS", u"...", None))
        self.feedingFees.setText(QCoreApplication.translate("SMS", u"...", None))
        self.studiesFees.setText(QCoreApplication.translate("SMS", u"...", None))
        self.label_87.setText(QCoreApplication.translate("SMS", u"Balances :", None))
        self.label_88.setText(QCoreApplication.translate("SMS", u"From Feeding Fees :", None))
        self.from_studiesFees.setText(QCoreApplication.translate("SMS", u"...", None))
        self.label_89.setText(QCoreApplication.translate("SMS", u"From Studies Fees :", None))
        self.label_90.setText(QCoreApplication.translate("SMS", u"Expenses :", None))
        self.from_feedingFees.setText(QCoreApplication.translate("SMS", u"...", None))
        self.label_96.setText(QCoreApplication.translate("SMS", u"Total", None))
        self.label_97.setText(QCoreApplication.translate("SMS", u"From School Fees :", None))
        self.from_schoolFees.setText(QCoreApplication.translate("SMS", u"..", None))
        self.label_99.setText(QCoreApplication.translate("SMS", u"Feeding Fees :", None))
        self.balanceFees.setText(QCoreApplication.translate("SMS", u"...", None))
        self.label_101.setText(QCoreApplication.translate("SMS", u"School Fees :", None))
        self.label_102.setText(QCoreApplication.translate("SMS", u"Studies Fees :", None))
        self.total_expenses.setText(QCoreApplication.translate("SMS", u"...", None))
        self.add_schholFees.setText(QCoreApplication.translate("SMS", u"Save School Fees", None))
        self.add_studiesFees.setText(QCoreApplication.translate("SMS", u"Save Studies Fees", None))
        self.add_feedingFees.setText(QCoreApplication.translate("SMS", u"Save Feeding Fees", None))
        self.label_104.setText(QCoreApplication.translate("SMS", u"<html><head/><body><p><span style=\" font-weight:400; text-decoration: underline;\">Adding Expenses Used</span></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.expenses1), QCoreApplication.translate("SMS", u"expenses", None))
        self.label_83.setText(QCoreApplication.translate("SMS", u"Message Subject :", None))
        self.label_85.setText(QCoreApplication.translate("SMS", u"To :", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("SMS", u"Input message here...", None))
        self.add_schholFees_2.setText(QCoreApplication.translate("SMS", u"Send mail", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.email), QCoreApplication.translate("SMS", u"email", None))
        self.label_16.setText("")
        self.label_15.setText(QCoreApplication.translate("SMS", u"System", None))
        self.label_14.setText(QCoreApplication.translate("SMS", u"School Management", None))
        self.label_17.setText(QCoreApplication.translate("SMS", u"Total Student", None))
        self.label_18.setText(QCoreApplication.translate("SMS", u"....", None))
        self.label_19.setText(QCoreApplication.translate("SMS", u"Total Expenses", None))
        self.label_20.setText(QCoreApplication.translate("SMS", u"....", None))
        self.pushButton.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainDashboard), QCoreApplication.translate("SMS", u"main", None))
    # retranslateUi

