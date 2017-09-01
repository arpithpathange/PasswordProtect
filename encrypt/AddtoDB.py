from prettytable import PrettyTable
from dbconn import Sqlite
from encryptdata import SafeData


class AddtoDb:
    obj_db = None
    safedata = None
    obj_AddtoDb = None

    def __init__(self):
        self.obj_db = Sqlite()
        self.safedata = SafeData()

    def addtoDb(self,acc_info, user_info, user_pass, account_no, pin):
        self.obj_db.dbinsert(acc_info, user_info, self.safedata.encrypt(user_pass),
                             account_no, self.safedata.encrypt(pin))

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



