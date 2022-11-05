# 代码格式化的快捷键：Ctrl+Alt+l

#1.整数 integer
a=100
print("a=",a)   #a=100

#2.浮点数 float
b=3.14
print("b=",b)

3.#Boolean 布尔类型
c=1>2
d=1<2
e=1==1
print(c,d,e)

#4.string 字符串，使用双引号或者单引号表示
name="Jack"
email='664514687@qq.com'
print("name=",name)
print("email=",email)

#使用''' '''或者""" """表示多行字符串
address='''
广西壮族自治区
桂林电子科技大学
东校区'''
print(address)

#5.list 列表，是一个可变的有序序列，使用[]表示。
oddNumbers=[1,3,5,7,9]
print(oddNumbers)

courses=['html','linux','mysql','java','python']
print(courses)

my=['haoop','hbase']
print(my)

#可以存放不同的数据类型元素
arrays=[1,'html',3.14,True]
print(arrays)

#或者列表的元素，使用索引的方式
print(courses[0])
print(arrays[2])

#往列表立添加元素，使用append（）方法
courses.append("javascript")
print(courses)

#6.Tuple:元组，是一个不可变的有序序列，使用（）表示。
color=("blue","red","green")
print(color)

#7.Dictionary:字典，是一个键值对  key-value,使用{}表示。
account_dict={"username":"admin","password":"12345"}
print(account_dict)
#或者键对应的值
print(account_dict["username"])



















