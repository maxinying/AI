#!/usr/bin/python
import sys
def userDict():
    dict={}
    with open('../../data/problem1/A/User_A.csv') as userfile:
        next(userfile)
        userdatas=userfile.readlines()
        for userdata in userdatas:
            key = userdata.split(',')[1]
            if key in dict:
                dict[key] += 1
            else:
                dict[key] = 1
    return dict
def main():
    dict = userDict()
    for key,value in dict.items():
        print(key,value)
if __name__ == '__main__':
    main()
