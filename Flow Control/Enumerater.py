#枚举函数enumerate（）：接受一个客迭代对象并返回一个枚举对象（一个迭代器），
#该对象生成一个（index，value）形式的元组，其中index是指项目的偏移量
#item是指来自客迭代对象的相应项目
my_string='Python'
print(list(enumerate(my_string)))

data_list=['a','b','c']
print(list(enumerate(data_list)))