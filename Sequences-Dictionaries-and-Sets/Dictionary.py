#Dictionary 字典

#1.访问字典
login_info={'username':'admin','password':'12345','login_type':'QQ'}
print(login_info['username'])
print(login_info['password'])

#2.使用函数访问元素
#2.1keys(),values(),items()'
login_info={'username':'admin','password':'12345','login_type':'QQ'}
print(login_info.keys())
print(login_info.values())
print(login_info.items())
print("--------------------------------")

#2.2 使用for循环遍历字典的键和值
login_info={'username':'admin','password':'12345','login_type':'QQ'}

#3.1 dict[key]=value
login_info['login_type']='Wechat'
login_info['remember_pwd']=True
print(login_info)
#3.2 update()
login_info.update({'login_type':'zhifubao'})
login_info.update({'remember_pwd':True})
print(login_info)

#4.删除，使用del语句
login_info={'username':'admin','password':'12345','login_type':'QQ'}
del login_info['login_type']
print(login_info)

#5.清除所有字典元素，使用dict.clear()
login_info={'username':'admin','password':'12345','longin_type':'QQ'}
login_info.clear()
print(login_info)