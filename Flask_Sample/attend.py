# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:59:47 2019

@author: yokotaka
"""

from flask import Flask
from flask import request
from flask import render_template
import mysql.connector
import datetime

app = Flask(__name__)

@app.route("/")  # どのページで実行する関数か設定
def main():

	conn = mysql.connector.connect(user='root',password='alice&9160&yokkuSQL',database='attend_check')
	cur = conn.cursor()

	cur.execute("select * from student")

	#print(cur.fetchall())

	student = cur.fetchall()

	student_length = len(student)

	return render_template('attend_check.html',student = student, student_length = student_length)

@app.route("/send",methods=["POST"])
def send():
	if request.method == "POST":
		date=datetime.date.today()
		writer = request.form["writer"]
		freetext = request.form["freetext"]
		student_name = request.form.getlist("student_name")
		print(student_name)
		print(freetext)
		return render_template('attend_send.html',student = student_name,text=freetext,writer_name=writer,day=date)

@app.route("/send2",methods=["POST"])
def final_check():
	if request.method == "POST":
		mail = request.form.get("mail")
		print(mail)
		return render_template('thanks.html',final_check=mail)

if __name__ == "__main__":
    app.run(debug=True)