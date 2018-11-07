#!/usr/bin/python
import sys
dict_infor={}
age_dict={'-1': -1,'15岁以下': 0,'16-25岁': 1,'26-35岁': 2,'36-45岁': 3,'46-55岁': 4,'56岁以上': 5}
def userDict():
    dict={}
    with open('../../data/problem1/A/User_A.csv') as userfile:
        next(userfile)
        userdatas=userfile.readlines()
        for userdata in userdatas:
            key = userdata.split(',')[0]
            value = 0
            dict[key]=value
            age = userdata.split(',')[1]
            age_transe = age_dict[age]
            dict_infor[key]= str(age_transe)+','+','.join(userdata.strip().split(',')[2:])
    return dict
def filterUser():
    dict = userDict()
    fw = open('../file/UserFilter.csv','w')
    #fo = open('UserFilterOut.csv','w')
    with open('../../data/problem1/A/Action_201602_A.csv') as actionfile:
        next(actionfile)
        actiondatas=actionfile.readlines()
        for actiondata in actiondatas:
            key = actiondata.split(',')[0]
            dict[key]+=1
    with open('../../data/problem1/A/Action_201603_A.csv') as actionfile:
        next(actionfile)
        actiondatas=actionfile.readlines()
        for actiondata in actiondatas:
            key = actiondata.split(',')[0]
            dict[key]+=1     
    with open('../../data/problem1/A/Action_20160409_A.csv') as actionfile:
        next(actionfile)
        actiondatas=actionfile.readlines()
        for actiondata in actiondatas:
            key = actiondata.split(',')[0]
            dict[key]+=1
    for key,value in dict.items():
        if value > 0:
            fw.write(key+','+dict_infor[key]+'\n')
    fw.close()
    #fo.close()
def main():
    filterUser()
if __name__ == '__main__':
    main()

