#!/usr/bin/python
import sys
def productDict():
    dict={}
    with open('../../data/problem1/A/Product_A.csv') as productfile:
        next(productfile)
        productdatas=productfile.readlines()
        for productdata in productdatas:
            key = productdata.split(',')[0]
            value = 0
            dict[key]=value
    return dict
def filterProduct():
    dict = productDict()
    #fw1 = open('../file/Action_201602_F.csv','w')
    #fw2 = open('../file/Action_201603_F.csv','w')
    #fw3 = open('../file/Action_20160409_F.csv','w')
    fw = open('../file/Action_F.csv','w')
    with open('../../data/problem1/A/Action_201602_A.csv') as actionfile:
        next(actionfile)
        actiondatas=actionfile.readlines()
        for actiondata in actiondatas:
            if actiondata.split(',')[1] in dict:
                fw.write(actiondata)
    with open('../../data/problem1/A/Action_201603_A.csv') as actionfile:
        next(actionfile)
        actiondatas=actionfile.readlines()
        for actiondata in actiondatas:
            if actiondata.split(',')[1] in dict:
                fw.write(actiondata)   
    with open('../../data/problem1/A/Action_20160409_A.csv') as actionfile:
        next(actionfile)
        actiondatas=actionfile.readlines()
        for actiondata in actiondatas:
            if actiondata.split(',')[1] in dict:
                fw.write(actiondata) 
    #fw1.close()
    #fw2.close()
    #fw3.close()
    fw.close()
def main():
    filterProduct()
if __name__ == '__main__':
    main()

