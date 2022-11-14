#整数和字符串是不可变对象，意味可以用来共享

a=3
b=3
c=a
print(a is b)
print(a is c)

s1='python'
s2='python'
print(s1 is s2)

#列表是可变对象
list1=[1,2,3]
list2=[1,2,3]
print(list1 is list2)
print(list1 is not list2)