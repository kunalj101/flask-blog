#sql.py databse connections

#import sqlite
import sqlite3

#create new database, if it does not exist
with sqlite3.connect("blog.db") as connection:
	#Get cursor object to execute the SQL commands
	c = connection.cursor()
	#create the table
	c.execute("""CREATE TABLE posts
		(title TEXT, post TEXT)""")
	#insert dummy values in the table
	c.execute("""INSERT INTO posts VALUES ("Good","I'm good")""")
	c.execute("""INSERT INTO posts VALUES ("Okay","I'm okay")""")
	c.execute("""INSERT INTO posts VALUES ("Excellent","I'm excellent")""")
	c.execute("""INSERT INTO posts VALUES ("Well","I'm well")""")
