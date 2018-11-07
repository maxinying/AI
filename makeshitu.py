#!/usr/bin/python
def userDict():
    dict={}
    with open('../file/UserFilter.csv') as userfile:
        userdatas=userfile.readlines()
        for userdata in userdatas:
            key = userdata.split(',')[0]
            dict[key]=','.join(userdata.strip().split(',')[1:]
    return dict
def makeshitu():
    user_dict=userDict()
    dict={}
    typedict={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}
    fw = open('../file/shitu.csv')
    with open('../file/Action_F.csv') as actionfile:
        actiondatas=actionfile.readlines()
        for action in actiondatas:
            key_user = action.split(',')[0]
            key_product=action.split(',')[1]
            key = key_user + '|'+ key_product
            if key in dict:
                s = dict[key].split(',')[6]
                
            else:
                cate = action.split(',')[5]
                brand = action.split(',')[6]
                user_age = user_dict[key_user].split(',')[0] 
                user_sex = user_dict[key_user].split(',')[1]
                user_degree = user_dict[key_user].split(',')[2]
                user_signDay = user_dict[key_user].split(',')[3]
                typedict[action.split(',')[4]] +=1
                for key,value in typedict:
                    s = s + str(value) +','
                print(s)
                value = cate+','+brand+','+user_age+','+user_sex+','+user_degree+','+user_signDay+','+ s
                dict[key] = value;
                
    return dict