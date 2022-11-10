#Tuple 元组，元组的元素不能修改
#1。索引，索引从0开始，或者以负索引访问，表示从列表末尾开始访问，从-1开始
data_tuple=('Mysql','Html','Java','Python')
print(data_tuple[0])
print(data_tuple[-1])


#2.切片
data_tuple=('Mysql','Html','Java','Python')
print(data_tuple[1:3])

#3.元组连接（+）与乘法（*）
data_tuple_1=('Mysql','Hbase')
data_tuple_2=('Html','Java')
data_tuple_3=('Hadoop','Python')
print(data_tuple_1+data_tuple_2+data_tuple_3)
print(data_tuple_1*3)


#4.元组函数：len(),min(),max()

#5.list(),将元组转换为列表；tuple（），将列表转换为元组
data_tuple=('Mysql','Htaml','java')
data_list=list(data_tuple)
print(data_list)

data_lst_2=['a','b','c']
data_tuple_2=tuple(data_lst_2)
print(data_tuple_2)