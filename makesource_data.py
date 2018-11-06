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
    dict = {}
    with open('../User_A.csv') as userfile:
        with open('../Product_A.csv') as productfile:
            next(userfile)
            next(productfile)
            for userdata in userfile:
                for productdata in productfile:
                    key = userdata.split(',')[0]+'|'+productdata.split(',')[0]
                    value = userdata.split(',')[1:]+productdata.split(',')[1:]
                    dict[key] = value
     print(len(dict))
    return dict

i = 0           
with open('../Action_20160409_A.csv') as file:
    next(file)
    for line in file:
        if(i == 0):
            startTime = line.split(',')[2][0:10]
            i+=1
        endTime = line.split(',')[2][0:10]
        if(Caltime(startTime,endTime)<7):
            
            
        i+=1
        dict = makeDict();
