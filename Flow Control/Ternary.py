#三元运算符
#需求：求a，b的最大值
#1.if-else
a=2
b=4
if a>b:
    print(a)
elif a<b:
    print(b)
else:
    print('a==b')

#2.TrueValue if expression else FalseValue
result=a if a>b else b
print(result)

#3.(FalseValue,TrueValue)[expression]
result=(b,a)[a>b]
print(result)