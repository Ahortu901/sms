#!/usr/bin/python3
import sqlite3
import mysql.connector
import psycopg2
import datetime

def connection():
	conn = sqlite3.connect("School.db")
	cursor = conn.cursor()

	sql = """CREATE TABLE IF NOT EXISTS users(
		full_name CHAR(50) NOT NULL,
		username CHAR(50) NOT NULL,
		email CHAR(50) NOT NULL,
		password CHAR(50),
		UNIQUE (username)
	)"""

	sql1 = """CREATE TABLE IF NOT EXISTS all_students(
		registratin_number VARCHAR(60) NOT NULL, 
		full_name VARCHAR(100) NOT NULL, 
		date_of_birth VARCHAR(50), 
		Class VARCHAR(20), 
		gender VARCHAR(20), 
		home_address VARCHAR(100), 
		parent_name VARCHAR(100), 
		mobile_number VARCHAR(15), 
		email_address VARCHAR(100), 
		PRIMARY KEY (registratin_number), 
		UNIQUE (registratin_number)
	)"""

	sql2 = """CREATE TABLE IF NOT EXISTS mail(
		message_subject VARCHAR(100) NOT NULL, 
		"to" VARCHAR(50) NOT NULL, 
		mail_input VARCHAR(50000000) NOT NULL, 
		date_created DATETIME
	)"""

	sql3 = """CREATE TABLE IF NOT EXISTS expenses (
		expenses_from VARCHAR(20) NOT NULL, 
		expenses_for VARCHAR(20) NOT NULL, 
		amount VARCHAR(50) NOT NULL
	)"""

	sql4 = """CREATE TABLE IF NOT EXISTS attendance (
		registration_number VARCHAR(50) NOT NULL, 
		full_name VARCHAR(100) NOT NULL, 
		Class VARCHAR(20) NOT NULL, 
		date VARCHAR(30) NOT NULL
	)"""

	sql5 = """CREATE TABLE IF NOT EXISTS students_fees (
		full_name VARCHAR(100) NOT NULL, 
		Class VARCHAR(50) NOT NULL, 
		fees_type VARCHAR(50) NOT NULL, 
		term VARCHAR(20) NOT NULL, 
		amount VARCHAR(50) NOT NULL, 
		date VARCHAR(20) NOT NULL, 
		date_created DATETIME
	)"""

	sql6 = """CREATE TABLE IF NOT EXISTS student_marks (
		registration_number VARCHAR(60) NOT NULL, 
		full_name VARCHAR(100), 
		marks VARCHAR(50) NOT NULL, 
		Class VARCHAR(50) NOT NULL, 
		marks_type VARCHAR(50) NOT NULL, 
		subject VARCHAR(50) NOT NULL, 
		term VARCHAR(50) NOT NULL
	)"""

	print("Table created successfuly.")
	cursor.execute(sql)
	cursor.execute(sql1)
	cursor.execute(sql2)
	cursor.execute(sql3)
	cursor.execute(sql4)
	cursor.execute(sql5)
	cursor.execute(sql6)
	conn.commit()
	conn.close()

def user(full_name = '', username = '', email = '', password = ''):
	conn = sqlite3.connect("School.db")
	cursor = conn.cursor()
	
	qry =('INSERT INTO users(full_name, username, email, password) VALUES ("{}","{}","{}","{}")').format(full_name, username, email, password)
	value = (full_name, username, email, password)
	cursor.execute(qry)
	conn.commit()
	conn.close()

def add_student(registratin_number='', full_name='', date_of_birth='', Class='', gender='', home_address='', parent_name='', mobile_number='', email_address=''):
	conn = sqlite3.connect("School.db")
	cursor = conn.cursor()
	qry = """INSERT INTO all_students(registratin_number, full_name, date_of_birth, Class, gender, home_address,
		parent_name, mobile_number, email_address) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')
	""".format(registratin_number, full_name, date_of_birth, Class, gender, home_address, parent_name, mobile_number, email_address)
	cursor.execute(qry)
	conn.commit()
	conn.close()

def update_student(full_name='', date_of_birth='', Class='', gender='', home_address='', parent_name='', mobile_number='', email_address='', registratin_number=''):
	conn = sqlite3.connect("School.db")
	cursor = conn.cursor()
	qry = """UPDATE all_students SET full_name = '{}', date_of_birth = '{}', Class ='{}', gender ='{}', home_address ='{}'
		parent_name ='{}', mobile_number ='{}', email_address = '{}' WHERE registratin_number = '{}'
		""".format(full_name, date_of_birth, Class, gender, home_address, parent_name, mobile_number, email_address, registratin_number)
	cursor.execute(qry)
	conn.commit()
	conn.close()

def delete_student(full_name):
	conn = sqlite3.connect("School.db")
	cursor = conn.cursor()
	qry = "DELETE  FROM all_students WHERE full_name = '{}'".format(full_name)
	cursor.execute(qry)
	conn.commit()
	conn.close()

def add_student_marks(reg_num ='', fullName='', Marks_set='', Class='', marks_types='', subjects_set='', term_school=''):
	conn = sqlite3.connect("School.db")
	cursor = conn.cursor()
	qry = """INSERT INTO student_marks(registration_number, full_name, marks, Class, marks_type, subject, term)
		VALUES ('{}','{}','{}','{}','{}','{}','{}')""".format(reg_num, fullName, Marks_set, Class, marks_types, subjects_set, term_school)
	cursor.execute(qry)
	conn.commit()
	conn.close()

def delete_marks(fullName = ''):
	conn = sqlite3.connect("School.db")
	cursor = conn.cursor()
	qry = """DELETE FROM student_marks WHERE full_name = '{}'""".format(fullName)
	cursor.execute(qry)
	conn.commit()
	conn.close()