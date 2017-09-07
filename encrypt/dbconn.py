'''
Version:    0.0.1
Author:     Arpith Vittal Pathange

This class connects to the sqlite db for all your DB operations. I have used sqlite for now as it is easy to use.

Sqlite has following disadventages:
1. No user support
2.

Adventages of postgress:
1. Large support
2. Huge support for 3rd party , I have no idea but down the line we might integrate with some 3rd party apps.

'''
import sqlite3


class Sqlite:
    conn = None
    c = None

    def __init__(self):
        self.conn = sqlite3.connect('my_first_db.sqlite')
        self.conn.text_factory = str
        self.c = self.conn.cursor()

    def dbinsert(self, acc_info, user_info, user_pass, account_no, pin):
        rows = [acc_info, user_info, user_pass, account_no, pin]
        self.c.execute('insert into Account values (?,?,?,?,?)', rows)
        self.conn.commit()

    def getdata(self):
        self.c.execute("SELECT * FROM Account")
        rows = self.c.fetchall()

        return rows

    def deldata(self):
        self.c.execute('delete  from Account')

    def closedb(self):
        self.conn.close()





