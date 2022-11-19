data=[]
for i in range(101):
    data.append(i)
print(data)


#1.使用列表推导式创建一个0-10的列表
data_comprehension=[i for i in range(11)]
print(data_comprehension)

#2.使用列表推导式创建一个0-10的奇数列表
data_even=[i for i in range(11) if i %2 !=0]
print(data_even)


3.
my_string='python'
data_str=[(i,i.upper())for i in my_string if i not in 'opq']
print(data_str)
#['y','t','h','n']