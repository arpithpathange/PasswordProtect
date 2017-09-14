__author__ = 'arpith.pathange'

import sqlite3

conn = sqlite3.connect(r"account.sqlite")
c = conn.cursor()
c.execute('''CREATE TABLE `Account` ( `account_name` TEXT,
                        `User_name` TEXT, `Password` TEXT, `account_no`
                            TEXT, `pin` TEXT );''')

