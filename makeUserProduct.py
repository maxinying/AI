#!/usr/bin/python
import time
import datetime


def Caltime(date1,date2):
    date1=time.strptime(startTime,"%Y-%m-%d")
    date2=time.strptime(endTime,"%Y-%m-%d")
    date1=datetime.datetime(date1[0],date1[1],date1[2])  
    date2=datetime.datetime(date2[0],date2[1],date2[2])
    return (date2-date1).days
def makeDict():
    fw = open('UserProductDatas.csv','w')
    with open('../data/problem1/A/User_A.csv') as userfile:
        with open('../data/problem1/A/Product_A.csv') as productfile:
            next(userfile)
            next(productfile)
            userdatas=userfile.readlines()
            productdatas=productfile.readlines()
            for userdata in userdatas:
                for productdata in productdatas:
                    key = userdata.split(',')[0]+'|'+productdata.split(',')[0]
                    value = ','.join(userdata.strip().split(',')[1:]+productdata.strip().split(',')[1:])
                    fw.write(key+','+value+'\n')
    fw.close()
makeDict()