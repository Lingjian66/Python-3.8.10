#function 函数
#1.预定义函数（内置函数）
#打印
print("人生苦短，我用python")
#max（），main()
maxNumber=max(1,3,5,7,9)
minNumber=min(1,3,5,7,9)
print(maxNumber,minNumber)

#len()
name="Luly"
print(len(name))
courses=['html','linux','mysql','java','python']
print(len(courses))

print("---------")

#2.用户自定义函数
#2.1定义没有参数，没有返回值的加法函数
def addition():
    a=3
    b=2
    sum=a+b
    print("sum=",sum)
    return
#调用函数
addition()


#2.2定义有参数，有返回值的减法函数
def subtraction(x,y):
    result=x-y
    return result
#调用函数
res=subtraction(10,2)
print("subtraction=",res)

#3.函数的形参（parameter）和实参（argument）
#3.1 Positional or Required arguments 位置或必须参数：参数应该与函数定义完全匹配
subtraction(10,3)


#3.2keyword arguments 关键字参数：在函数调用参数时，通过参数名称标识参数
def login(username,password):
    print(username)
    print(password)
    return

login("admin","12345")
login(password="12345",username="admin")


#3.3  Default arguments 默认参数：参数的函数调用中没有提供值，则假定默认值
def getInfo(name,age=1):
    print("name",name)
    print("age",age)
    return

getInfo("Lily",20)
