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



'''conn = Sqlite()
conn.dbinsert('icici1', '08', 'sdhf')
infos = conn.getdata()


for info in infos:
    print str(info)

conn.closedb()'''

