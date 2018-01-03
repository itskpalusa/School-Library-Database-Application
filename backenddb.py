# import sqlite3 framework - this enables database creation with python integration

import sqlite3

# create the variable class

class Database:

# master TABLE
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS master(id INTEGER PRIMARY KEY, booktitle text, bookauthor text, FOREIGN KEY(booktitle, bookauthor) REFRENCES book(title, author))")

# creation of the base table and database
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title text ,author text )")
        self.conn.commit()

# creation of user table

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY, schoolID INTEGER, userType NOT NULL CHECK (Usertype IN ('Student', 'Staff'))")
        self.conn.commit()

# creation of loan table

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS loan(id INTEGER PRIMARY KEY )")
        self.conn.commit()

# create the proper layout for the insert function
    def insert(self,title,author):
        self.cur.execute("INSERT into book VALUES (NULL,?,?)",(title,author))
        self.conn.commit()

# create the proper layout for the view function

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

# create the proper layout for the search command

    def search(self,title="",author=""):
        self.cur.execute("SELECT * FROM book where title=? OR author=?",(title,author))
        rows=self.cur.fetchall()
        return rows

# delete function execution from the database itself

    def delete(self,id):
        self.cur.execute("DELETE FROM book where id =?",(id,))
        self.conn.commit()

# self-recurring update argument

    def update(self,id,author,title):
        self.cur.execute("UPDATE book SET title=?,author=? WHERE id=?",(title,author))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
