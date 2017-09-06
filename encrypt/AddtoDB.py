from prettytable import PrettyTable
from dbconn import Sqlite
from encryptdata import SafeData
from logger import logbase
import sys


class AddtoDb:
    obj_db = None
    safedata = None
    obj_AddtoDb = None
    log = None

    def __init__(self):
        self.obj_db = Sqlite()
        self.safedata = SafeData()
        self.log = logbase()

    def addtoDb(self,acc_info, user_info, user_pass, account_no, pin):
        try:
            self.obj_db.dbinsert(acc_info, user_info, self.safedata.encrypt(user_pass),
                             account_no, self.safedata.encrypt(pin))
            self.log.loginfo("inserted data in to the Db "+ acc_info +" "+user_info+" "+" "+
                        self.safedata.encrypt(user_pass)+" "+account_no+" "+self.safedata.encrypt(pin))
        except :
            self.log.logerror("Error in inserting data to the DB "+sys.exc_info()[0])

    def getdata(self, pass_key):
        datas = self.obj_db.getdata()
        t = PrettyTable(['Account_info', 'User_name', 'User_pass', 'Account_no', 'Pin'])
        for data in datas:
            lst = list(data)
            lst[2] = self.safedata.decrypt(data[2], pass_key)
            lst[4] = self.safedata.decrypt(data[4], pass_key)
            t.add_row(lst)
        print t




obj_AddtoDb = AddtoDb()
obj_AddtoDb.addtoDb('HDFC', '123123', 'ad@12345', '32141E13', '123456')
print "Enter the Pass_key :"
pass_key = raw_input()
obj_AddtoDb.getdata(pass_key)



