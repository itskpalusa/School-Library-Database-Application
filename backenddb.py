import sqlite3

class Database:

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title text ,author text,schoolID INTEGER ,due INTEGER )")
        self.conn.commit()

    def insert(self,title,author,schoolID,due):
        self.cur.execute("INSERT into book VALUES (NULL,?,?,?,?)",(title,author,schoolID,due))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="",author="",schooID="",due=""):
        self.cur.execute("SELECT * FROM book where title=? OR author=? OR schooID=? OR due=?",(title,author,schoolID,due))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book where id =?",(id,))
        self.conn.commit()

    def update(self,id,author,title,schoolID,due):
        self.cur.execute("UPDATE book SET title=?,author=?,schoolID=?,due=? WHERE id=?",(title,author,schoolID,due,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
