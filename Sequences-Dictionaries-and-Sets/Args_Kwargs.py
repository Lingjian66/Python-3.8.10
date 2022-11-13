#1. *args:在python 中，*args的单星形式可用作参数
#将非关键字客变长度的参数列表发送到函数

def multiply(x,y):
    print(x*y)
    return

multiply(2,3)
multiply(3,3)


print("---------")

#定义一个可变参数的乘法函数

def multiply_2(*args):
    res=1
    for i in args:
        res *=i
    print(res)
    return

multiply_2(2,3)
multiply_2(3,4,5)

#2. **kwargs:**kwargs的双星号形式用于将带关键字的可变长度参数字典传递给函数