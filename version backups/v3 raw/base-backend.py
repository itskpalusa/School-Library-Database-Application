import sqlite3
import datetime
import os


def create_db():
    if os.path.isfile('./schoollibrary.db'):
        os.remove('./schoollibrary.db')

    conn = sqlite3.connect('schoollibrary.db')

    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER NOT NULL PRIMARY KEY,
            title TEXT,
            author text,
            schoolID INTEGER
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER NOT NULL PRIMARY KEY,
            name text,
            type TEXT check(type = "student" or type = "staff")
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS loans(
            book_id INTEGER UNIQUE,
            user_id INTEGER,
            expiration_date DATETIME,
            FOREIGN KEY(book_id) REFERENCES books(id),
            FOREIGN KEY(user_id) REFERENCES users(id),
            PRIMARY KEY (book_id, user_id)
        )
    """)

#    c.execute("INSERT INTO books VALUES(1, 'Catcher in the Rye', 'J. D. Salinger', 1);")
#    c.execute("INSERT INTO books VALUES(2, 'Don Quixote', 'Miguel de Cervantes', 1);")
#    c.execute("INSERT INTO users VALUES(1, 'Karthik', 'staff');")
#    c.execute("INSERT INTO users VALUES(2, 'BorrajaX', 'student');")
#    conn.commit()
#    print(c.execute("SELECT COUNT(*) FROM books").fetchone())
#    print(c.execute("SELECT COUNT(*) FROM users").fetchone())


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


if __name__ == "__main__":
    create_db()
