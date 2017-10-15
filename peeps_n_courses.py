import csv
import sqlite3

pc="peeps_n_courses.db"

db = sqlite3.connect(pc)
d = db.cursor()

init_table = "CREATE TABLE peeps (name TEXT, age NUMERIC, id NUMERIC)"
d.execute(init_table)

peeps = csv.DictReader(open("peeps.csv"))
for row in peeps:
	add_row = 'INSERT INTO peeps VALUES ("' + row["name"] + '",' + row["age"] + "," + row["id"] + ")"
	#print add_row
	d.execute(add_row)

init_table = "CREATE TABLE courses (code TEXT, mark NUMERIC, id NUMERIC)"
d.execute(init_table)

courses = csv.DictReader(open("courses.csv"))
for row in courses:
	add_row = "INSERT INTO courses VALUES ('" + row["code"] + "'," + row["mark"] + "," + row["id"] + ")"
	d.execute(add_row)

db.commit()
db.close()
