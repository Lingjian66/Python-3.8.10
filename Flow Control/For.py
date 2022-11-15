#for循环
#1.字符串
my_string='python'
for str in my_string:
    print(str)

#2.list
data_list=['Mysql','Hadoop','Java']
for item in data_list:
    print(item)


#3.整数不是可迭代对象，使用for循环遍历会报错

#4.range（）：可以用来创建整数列表，range（x,y,z）,x表示起始位置，y表示结束位置，z表示步幅
for i in range(10):
    print(i)