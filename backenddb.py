# import sqlite3 framework - this enables database creation with python integration

import sqlite3

# create the variable class

class Database:

# creation of the base database
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title text ,author text,schoolID INTEGER ,type text,due INTEGER )")
        self.conn.commit()

# create the proper layout for the insert function
    def insert(self,title,author,schoolID,type,due):
        self.cur.execute("INSERT into book VALUES (NULL,?,?,?,?,?)",(title,author,schoolID,type,due))
        self.conn.commit()

# create the proper layout for the view function

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

# create the proper layout for the search command

    def search(self,title="",author="",schooID="",due=""):
        self.cur.execute("SELECT * FROM book where title=? OR author=? OR schooID=? OR due=?",(title,author,schoolID,due))
        rows=self.cur.fetchall()
        return rows

# delete function execution from the database itself

    def delete(self,id):
        self.cur.execute("DELETE FROM book where id =?",(id,))
        self.conn.commit()

# self-recurring update argument

    def update(self,id,author,title,schoolID,type,due):
        self.cur.execute("UPDATE book SET title=?,author=?,schoolID=?,due=? WHERE id=?",(title,author,schoolID,type,due,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
