import csv #Gonna need that DictReader
import sqlite3 #To write to the database

pc="peeps_n_courses.db" #This is gonna be our file

db = sqlite3.connect(pc) #Create/establish a connection with our file
d = db.cursor() #Enable changes

#### CREATING PEEPS TABLE ####
init_table = "CREATE TABLE peeps (name TEXT, age NUMERIC, id NUMERIC)" #SQL command to create a table
d.execute(init_table) #Make that table yo

peeps = csv.DictReader(open("peeps.csv")) #Read up on our peeps

for row in peeps: #Loop through the rows in our CSV
	add_row = 'INSERT INTO peeps VALUES ("' + row["name"] + '",' + row["age"] + "," + row["id"] + ")" #Code to take the csv data and add it to a SQL table
	#print add_row
	d.execute(add_row) #Execute that code

#### CREATING COURSES TABLE ####

init_table = "CREATE TABLE courses (code TEXT, mark NUMERIC, id NUMERIC)" #Code to create our table
d.execute(init_table) #Create that table

courses = csv.DictReader(open("courses.csv")) #Read courses CSV
for row in courses: #Loop through our rows
	add_row = "INSERT INTO courses VALUES ('" + row["code"] + "'," + row["mark"] + "," + row["id"] + ")" #code to add this row to our table as SQL
	d.execute(add_row) #Add the row

db.commit() #Commit our changes! It's official!!!
db.close() #Close the file connection
