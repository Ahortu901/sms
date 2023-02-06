import sys
import os
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
from PySide6.QtGui import QScreen
import sqlite3
import random
import backEnd

from ui_splash_screen import Ui_SplashScreen

from ui_sms import Ui_SMS

backEnd.connection()

counter = 0

class MainWindow(QMainWindow, Ui_SMS):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.tabWidget.tabBar().setVisible(False)
        self.tabWidget_2.tabBar().setVisible(False)

        # --- Buttons Functions ------#
        self.login_3.clicked.connect(self.createUser)
        self.singup.clicked.connect(self.new_user)
        self.login_2.clicked.connect(self.login_user)
        self.add_student.clicked.connect(self.student_dashboard)
        self.add_student.clicked.connect(self.toggle)
        self.btn_register.clicked.connect(self.student_registration)
        self.dashboard_2.clicked.connect(self.dashboard_show)
        self.dashboard_2.clicked.connect(self.toggle)
        self.edit_student.clicked.connect(self.editStudents_nav)
        self.btn_update_2.clicked.connect(self.updateStudents)
        self.btn_delete.clicked.connect(self.deleteStudent)
        self.btn_search.clicked.connect(self.displaySearch)
        self.student_marks.clicked.connect(self.Marks_Tab_nav)
        self.btn_search_2.clicked.connect(self.getting_regNum_from_all_student)
        self.btn_register_9.clicked.connect(self.adding_studentMark)
        self.btn_delete_2.clicked.connect(self.deleteStudent)
    
    
    
        
    def createUser(self):
        self.tabWidget.setCurrentIndex(1)
    
    def new_user(self):
        try:
            fullname = self.login_username_2.text()
            user_info = self.login_username_3.text()
            mail = self.login_username_4.text()
            password1 = self.login_password_2.text()
            re_password = self.login_password_3.text()
            
            if re_password == password1:
                backEnd.user(full_name=fullname,username=user_info,email=mail,password=password1)
                self.tabWidget.setCurrentIndex(0)
                self.login_username_2.clear()
                self.login_username_3.clear()
                self.login_username_4.clear()
                self.login_password_2.clear()
                self.login_password_3.clear()
            else:
                QMessageBox.warning(self, "SignUp Error", "Passwords do not much")
        except Exception as Error:
            QMessageBox.warning(self, "SignUp error", "User already exists please login")
    
    def login_user(self):
        try:
            user = self.login_username.text()
            password = self.login_password.text()
            if len(user)== 0 or len(password)==0:
                QMessageBox.warning(self, "Login From", "Please fill all fileds")
                self.login_username.clear()
                self.login_password.clear()
            
            else:
                conn = sqlite3.connect("./School.db")
                cursor = conn.cursor()
                cursor.execute('SELECT password FROM users WHERE username =\'' + user + "\'")
                result_pass = cursor.fetchone()[0]
                conn.close()
                if result_pass == password:
                    self.tabWidget.setCurrentIndex(2)
                    self.tabWidget_2.setCurrentIndex(0)

                    self.tableWidget_7.setRowCount(0)
                    self.tableWidget_7.insertRow(0)
                    self.dashboard_show()

                    conn =sqlite3.connect("School.db")
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM all_students")
                    data = cursor.fetchall()
                    conn.close()
                    for row , form in enumerate(data):
                        for col , item in enumerate(form):
                            self.tableWidget_7.setItem(row, col, QTableWidgetItem(str(item)))
                            col +=1

                            row_position = self.tableWidget_7.rowCount()
                            self.tableWidget_7.insertRow(row_position)
                
                else:
                    QMessageBox.warning(self, "Login info", "Invalid username or password")
        except Exception:
            QMessageBox.warning(self, "Login error", "Details not found try again")
# ------------- Shadow Effects -------------
    def frame3(self):
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(6)
        self.shadow.setYOffset(4)
        self.shadow.setColor(QColor (85, 87, 83))
        self.frame_3.setGraphicsEffect(self.shadow)
    
    def frame5(self):
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(6)
        self.shadow.setYOffset(4)
        self.shadow.setColor(QColor (85, 87, 83))
        self.frame_5.setGraphicsEffect(self.shadow)
    
    def frame6(self):
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(6)
        self.shadow.setYOffset(4)
        self.shadow.setColor(QColor (85, 87, 83))
        self.frame_6.setGraphicsEffect(self.shadow)
# ------ Nav -----------------
    def toggle(self):
        self.dashboard_2.setCheckable(True)
        self.edit_student.setCheckable(True)
        self.add_student.setCheckable(True)
        self.student_marks.setCheckable(True)

        if self.dashboard_2.isChecked():
            self.dashboard_2.setStyleSheet("Background-color: red;")
            self.add_student.isChecked(False)

        elif self.add_student.isChecked():
            self.add_student.setStyleSheet("Background-color: red;")
            self.dashboard_2.isChecked(False)

    def dashboard_show(self):
        self.tabWidget_2.setCurrentIndex(0)

        self.frame3()
        self.frame5()
        self.frame6()
        

    def student_dashboard(self):
        self.tabWidget_2.setCurrentIndex(1)
        self.fill_next_reg_num()
    
    def editStudents_nav(self):
        self.tabWidget_2.setCurrentIndex(2)
        self.display2()
    def Marks_Tab_nav(self):
        self.tabWidget_2.setCurrentIndex(3)

    def fill_next_reg_num(self):
        self.registration_number.setDisabled(True)
        rand_ref = random.randint(500, 6000)
        conv_ref = ('Reg_N0:'+ str(rand_ref))
        self.registration_number.setText(conv_ref)

# ------- Adding Deleteing Updateing Students    
    def student_registration(self):
        try:
            self.tableWidget.setRowCount(0)
            self.tableWidget.insertRow(0)
            reg_num = self.registration_number.text()
            fullname = self.student_name.text()
            dob = self.DOB.text()
            student_class = self.student_class.currentText()
            student_gender = self.student_gender.currentText()
            homeAddress = self.student_address.toPlainText()
            parentname = self.parentName.text()
            telephone = self.parent_number.text()
            email_parent = self.parentEmail.text()

            backEnd.add_student(registratin_number=reg_num, full_name=fullname, date_of_birth=dob,Class=student_class,
            gender=student_gender, home_address=homeAddress, parent_name=parentname, mobile_number=telephone, email_address=email_parent)
            QMessageBox.information(self, "Registration", "Saved Successfully")

            conn =sqlite3.connect("School.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM all_students")
            data = cursor.fetchall()
            conn.close()
            for row , form in enumerate(data):
                for col , item in enumerate(form):
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
                    col +=1

                    row_position = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_position)
        
        except Exception:
            QMessageBox.warning(self, "Registration error", "Details already exists")
    
    def getReg_number(self):
        conn =sqlite3.connect("School.db")
        cursor = conn.cursor()

        search_by_name = self.student_name_3.text()
        if search_by_name != '':  
            qry = ("SELECT (registratin_number) FROM all_students WHERE full_name = '{}'").format(search_by_name)
            cursor.execute(qry)
            data = cursor.fetchall()[0][0]

            self.registration_number_2.setDisabled(True)
            self.registration_number_2.setText(str(data))
         
    def displaySearch(self):
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)

        conn =sqlite3.connect("School.db")
        cursor = conn.cursor()

        search_by_name = self.student_name_3.text()
        if search_by_name != '':
            qry = ("SELECT * FROM all_students WHERE full_name = '{}'").format(search_by_name)
            cursor.execute(qry)
            data = cursor.fetchall()

            for row , form in enumerate(data):
                for col , item in enumerate(form):
                    self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                    col +=1

                    row_position = self.tableWidget_2.rowCount()
                    self.tableWidget_2.insertRow(row_position)
                    self.getReg_number()
        
        else:
            QMessageBox.information(self, "Search error ", "Please enter the full name\n of the student to search")
    
    def display2(self):
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)

        conn =sqlite3.connect("School.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM all_students")

        data = cursor.fetchall()
        cursor.close()

        for row , form in enumerate(data):
            for col , item in enumerate(form):
                self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                col +=1

                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)

    def updateStudents(self):
        conn =sqlite3.connect("School.db")
        cursor = conn.cursor()
        
        reg_number = self.registration_number_2.text()
        full_name = self.student_name_2.text()
        date_of_birth = self.DOB_2.text()
        Class = self.student_class_2.currentText()
        gender = self.student_gender_2.currentText()
        address = self.student_address_2.toPlainText()
        
        if reg_number != '' and full_name != '':
            qry =("UPDATE students SET full_name = '{}' WHERE registratin_number = '{}'" ).format(full_name, reg_number)
            cursor.execute(qry)
            conn.commit()
            cursor.close()
            QMessageBox.information(self, "success", "Full name updated Successfully")
            self.display2()
            
        elif reg_number != '' and date_of_birth != '':
            qry =("UPDATE students SET date_of_birth = '{}' WHERE registratin_number = '{}'" ).format(date_of_birth, reg_number)
            cursor.execute(qry)
            conn.commit()
            cursor.close()
            QMessageBox.information(self, "success", "Date of Birth updated Successfully")
            self.display2()

        elif reg_number != '' and Class != '':
            qry =("UPDATE students SET Class = '{}' WHERE registratin_number = '{}'" ).format(Class, reg_number)
            cursor.execute(qry)
            conn.commit()
            cursor.close()
            QMessageBox.information(self, "success", "Class updated Successfully")
            self.display2()
        
        else:
            if reg_number != '' and full_name!= '' and date_of_birth!= '' and Class!= '' and gender!='' and address != '':
                qry = ('''
                    UPDATE students SET full_name = '{}', date_of_birth = '{}', Class = '{}',
                    gender = '{}', home_address = '{}', parent_full_name = '{}', phone_number ='{}', email_address = '{}'
                    WHERE registratin_number = '{}'
                ''').format(full_name, date_of_birth, Class, gender, address, reg_number)
                cursor.execute(qry)
                conn.commit()
                cursor.close()

                QMessageBox.information(self, "success", "Updated all Successfully")

                self.display2()
                self.student_name_2.clear()
                self.DOB_2.clear()
    
    def deleteStudent(self):
        full_name1 = self.student_name_2.text()
        if full_name1 != "":
            backEnd.delete_student(full_name=full_name1)
            self.display2()
            QMessageBox.information(self, "Delete info", "Deleted successfully")
        else:
            QMessageBox.warning(self, "Delete error", "Please the name of student to delete")

# ------- Adding, Deleting, Updating of Students Marks --------------------
    def getting_regNum_from_all_student(self):
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.insertRow(0)
        conn =sqlite3.connect("School.db")
        cursor = conn.cursor()
        searchBox = self.student_name_4.text()

        if searchBox != '':
            response = QMessageBox.question(self, "Searching...", "What do you want to search for? \n 1. Selecte Yes if for only registration number \n 2. Selecte No to make a full search")
            if response == QMessageBox.StandardButton.Yes:
                qry = ("SELECT (registratin_number) FROM all_students WHERE full_name = '{}'").format(searchBox)
                cursor.execute(qry)
                data = cursor.fetchall()[0][0]

                self.registration_number_3.setDisabled(True)
                self.registration_number_3.setText(str(data))
            elif response == QMessageBox.StandardButton.No:
                qry = ("SELECT * FROM student_marks WHERE full_name ='{}'").format(searchBox)
                cursor.execute(qry)
                data = cursor.fetchall()
                cursor.close()

                for row , form in enumerate(data):
                    for col , item in enumerate(form):
                        self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(item)))
                        col +=1

                        row_position = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(row_position)
        else:
            return QMessageBox.warning(self, "Searching error", "Please ener a name to search")

    def displayingMarks(self):
        conn =sqlite3.connect("School.db")
        cursor = conn.cursor()
        qry = ("SELECT * FROM student_marks")
        cursor.execute(qry)
        data = cursor.fetchall()
        cursor.close()

        for row , form in enumerate(data):
            for col , item in enumerate(form):
                self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(item)))
                col +=1

                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)

    def adding_studentMark(self):
        regNum = self.registration_number_3.text()
        fullName1 = self.student_name_5.text()
        Marks = self.marks.text()
        class_set = self.student_class_5.currentText()
        mark_Type = self.marks_type.currentText()
        subjects = self.student_subject.currentText()
        term = self.schoo_term.currentText()

        if regNum != '':
            backEnd.add_student_marks(reg_num=regNum, fullName=fullName1, Marks_set=Marks, Class=class_set, marks_types=mark_Type, subjects_set=subjects, term_school= term)
            QMessageBox.information(self, "Adding Marks...", "Marks added successfully")
            self.displayingMarks()
        else:
            QMessageBox.warning(self, "Adding markds error", "Please fill all fileds")
    
    def deleteMarks_sutdents(self):
        regNum = self.registration_number_3.text()
        fullName1 = self.student_name_5.text()

        if regNum != '' and fullName1 != '':
            backEnd.delete_marks(fullName=fullName1)
            QMessageBox.information(self, "Deleting Marks...", "Marks deleted successfully")
            self.displayingMarks()
        else:
            return QMessageBox.warning(self, "Deleting error", "Please fill in the student name and registration number to delete.")



# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        
        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(214, 205, 205, 221))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>searching</strong> for updates from database")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>loading</strong> database..."))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>loading</strong> user interface..."))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    geo = window.frameGeometry()
    geo.moveCenter(center)
    window.move(geo.topLeft())
    sys.exit(app.exec())