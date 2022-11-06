#数字函数

import random

#1.Power:乘方，幂，**
x=2
y=10
print(x**y)

#2.Quotient form floor division:整除的商，//
x=10
y=3
print(x//y)

#3.在python3中，商始终是一个浮点数
x=4
y=2
print(x/y)

#4.在python中，商始终是一个浮点数
x=10
y=4
print(x/y)

#5.内置数学函数
#5.1 绝对值abs()
print(abs(-3))

#5.2以元组的形式展示 商和余数 divmod()
x=10
y=3
print(divmod(x,y))

#5.3幂运算 pow()
x=2
y=10
print(pow(x,y))

#5.4 四舍五入 round（）
print(round(3.141592657,2))


#5.5计算求和sum（），可用于列表、元组、字典（字典的key相加）
#复制当前行的快捷键：Ctrl+d
data1=[1,2,3,4,5]
data2=(2,4,6,8)
data3={1:'a',5:'b',8:'c'}
print(sum(data1))
print(sum(data2))
print(sum(data3))

#5.6随机数  random(),返回一个0.0~1.0之间的随机浮点数，包括0.0但不包括1.0，需要导入random模块，命令：import random
x=random.random()
print(x)

#5.7  randint(low,high),返回介于low和high两者之间的整数，包括low、high
y=random.randint(1,10)
print(y)

#5.8 在序列中随机选取一个choice()
courses=["c","java","python","html","mysql"]
print(random.choice(courses))
