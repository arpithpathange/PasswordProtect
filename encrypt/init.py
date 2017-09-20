__author__ = 'arpith.pathange'

import sqlite3
from encryptdata import SafeData

safedata = SafeData()

conn = sqlite3.connect("account2.sqlite")
c = conn.cursor()
c.execute('''CREATE TABLE `Account` ( 'account_name' TEXT,
                        `User_name` TEXT, `Password` TEXT, `account_no`
                           TEXT, `pin` TEXT );''')

c.execute('''CREATE TABLE passkey (key TEXT );''')
passkey = raw_input("Please enter your Secret Passkey: ")
c = conn.cursor()
c.execute('INSERT INTO passkey VALUES(?)', (safedata.encrypt(passkey),))
conn.commit()