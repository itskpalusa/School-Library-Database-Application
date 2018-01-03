# import sqlite3 framework - this enables database creation with python integration

import sqlite3

# import python os

import os

# import datetime library

import datetime

# create the variable class

class Database:

# creation of the base table and database
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS books(
        id INTEGER NOT NULL PRIMARY KEY,
        title text,
        author text,
        schoolID INTEGER
            )
        """)
        self.conn.commit()

# creation of user table

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS user(
        id INTEGER NOT NULL PRIMARY KEY,
        name text,
        type TEXT check(type = "student" or type = "staff")
            )
        """)
        self.conn.commit()

# creation of loan table

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("""
         CREATE TABLE IF NOT EXISTS loans(
            book_id INTEGER UNIQUE,
            user_id INTEGER,
            expiration_date DATETIME,
            FOREIGN KEY(book_id) REFERENCES books(id),
            FOREIGN KEY(user_id) REFERENCES users(id),
            PRIMARY KEY (book_id, user_id)
                )
            """)
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

# borrow function
    def borrow(user_id, book_id):
        conn = sqlite3.connect('stack_100.db')
        c = conn.cursor()
        user_type = c.execute("SELECT type FROM users WHERE users.id=%s" % user_id).fetchone()[0]
        print("user_type='%s'" % user_type)
        if user_type == 'staff':
            # Staff can borrow for 2 weeks
            due_date = datetime.datetime.now() + datetime.timedelta(weeks=2)
        elif user_type == 'student':
            # Student can borrow for 1 weeks
            due_date = datetime.datetime.now() + datetime.timedelta(weeks=1)
        else:
            raise ValueError("Don't know what to do with a user of type '%s'" % user_type)

            user = c.execute("SELECT * FROM users WHERE users.id=%s" % user_id).fetchone()
            user_id = user[0]
            book = c.execute("SELECT * FROM books WHERE books.id=%s" % book_id).fetchone()
            book_id = book[0]
            print("User=%s (user_id=%s) is trying to borrow book=%s (book_id=%s)" % (
            user[1], user_id, book[1], book_id)
            )
            try:
                c.execute(
                "INSERT INTO loans(book_id, user_id, expiration_date) VALUES(?, ?, ?);", (
                book_id, user_id, due_date)
                )
                conn.commit()
                print("Borrowed!!.")
            except sqlite3.IntegrityError:
                print("Uh oh... It looks like that book was already borrowed?")
                previous = c.execute("SELECT * FROM loans WHERE book_id=%s" % book_id).fetchone()
                print("Previous borrow: %s" % (previous,))


    def __del__(self):
        self.conn.close()
