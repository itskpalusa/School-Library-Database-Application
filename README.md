# School Library Database Application

A python and sqlite3 based database application for a school library.

Can also choose to use a pure SQL based application as of right now. Since the base applications on both ends have been created, I am in the process of trying to merge the two data to create a full Python GUI to communicate with a SQL database. So far they aren't exactly cooperation.

##### Topic: Develop a database program to manage the issuance of books at a school library. Give the school a name. The program must be able to complete a minimum of the following tasks:

~~1. Track student and teacher names with ability to enter/view/edit names.~~

~~2. Track the issuance of books for a student or teacher.~~

3. Manage different limits for the number of books that can be issued to a student or teacher.

4. Manage the number of days that students and teachers can check out any book. (Hint: Mostly like the number of days will differ for students and teachers).

~~5. Give each book a different ID. Also, each book of same name and same author (but number of copies) will have different ID.~~

~~6. Generate/print weekly report to show books issued to whom and number of days leading to the due date return.~~

7. Generate/print weekly report of detail of fines (when book not returned on time).


# Requirements

## System Requirements

* You need Python 3.4 or later to be able to run the program.

You can have multiple Python versions (2.x and 3.x) installed on the same system without problems.
By default most computer have installed some version of python 2.x, so to install python3:

In most linux flavors you can install Python 3 like this:

$ sudo apt-get install python3 python3-pip

For other Linux flavors, OS X and Windows, packages are available at

http://www.python.org/getit/

* This program also uses sqlite3, which you can learn about here:

https://docs.python.org/2/library/sqlite3.html

To install sqlite3 please follow this link

https://www.sqlite.org/download.html

* Lastly, this program also pulls information from one of Python's own built in library known as TK or formally known as Tkinter. To learn more about Tk:

https://docs.python.org/3/library/tk.html


---

This is all you will need to run and execute the program, however if you decide you'd want further customization, this program can also be controlled with any SQL manager, as the database itself is sqlite based.

Personally, I recommend using DB browser for SQL lite.

To install and to learn more about DB browser go to:
http://sqlitebrowser.org/
