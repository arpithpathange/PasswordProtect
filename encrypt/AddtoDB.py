#!/usr/bin/python
'''
Version:    0.0.1
Author:     Arpith Vittal Pathange

This class inserts data to tbe db and retrives data form the db by calling dbconn object
Infos and any errors are logged by calling the logger class

Using PrettyTable to display the information on the console. Its beautifully puts the data on the console.


'''
from prettytable import PrettyTable
from dbconn import Sqlite
from encryptdata import SafeData
from logger import logbase
import sys
import getpass


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

            pass1 = self.safedata.encrypt(user_pass)
            pin1 = self.safedata.encrypt(pin)
            self.obj_db.dbinsert( acc_info, user_info, pass1,
                             account_no, pin1)
            self.log.loginfo("inserted data in to the Db "+ acc_info +" "+user_info+" "+" "+
                        self.safedata.encrypt(user_pass)+" "+account_no+" "+self.safedata.encrypt(pin))
        except :
            self.log.logerror("Error in inserting data to the DB ")

    def getdata(self, pass_key):
        try:
            self.log.loginfo("Getting data form the tables")
            datas = self.obj_db.getdata()
            self.log.loginfo("Data being fetched from the table")
            t = PrettyTable(['Account_info', 'User_name', 'User_pass', 'Account_no', 'Pin'])
            for data in datas:
                lst = list(data)
                lst[2] = self.safedata.decrypt(data[2], pass_key)
                lst[4] = self.safedata.decrypt(data[4], pass_key)
                t.add_row(lst)
            print t
        except:
            self.log.logerror("Error in fetching the data ")




obj_AddtoDb = AddtoDb()
#obj_AddtoDb.addtoDb('icici', '123123', 'ad@12345', '32141E13', '123456')
print "Enter the Pass_key :"
pass_key = getpass.getpass('Password:')
obj_AddtoDb.getdata(pass_key)



