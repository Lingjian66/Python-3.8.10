#字符串

#String 字符串
#1.字符串是不可变的
text="人生苦短，我用python"
print(text[0])
#text[0]="狗"  #报错，因为字符串不能修改值
#printf(text)


#2.字符串索引，使用[索引值]表示
print(text[0])
print(text[2])

#3.字符串切片，获取子字符串，包含起始索引，不包含结束索引
text="人生苦短，我用python"
print(text[:6])
print(text[0:4])
print(text[1:5])
print(text[6:])

#4.更新字符串，需要创建一个新的字符串
s1="hello world"
print(s1[0:6]+"python")

#5.转义字符串 \n换行，\t Tab
text="人生苦短\n我用python"
print(text)

#6.三重引号，字符串跨越多行，包括换行符、tab和任何其它特殊字符
text='''人生苦短，

              我用python
              
'''
print(text)

#7.字符串连接使用+，但是不能连接字符串和数字
s1="hello"
s2="python"
print(s1 + s2)
s3=10
#printf(s1+s3)  报错信息：can only concatenate str (not "int") to str


#8.字符串重复，*
text="python"
print(text*3)

#9.字符串内置函数
#9.1 upper(),lower(),大写、小写，返回一个新的字符串
text="Python"
print(text.upper())
print(text.lower())

#9.2 str(),将指定的值转换为字符串
x=10
print(str(x)+"abc")

#9.3 min(),返回字符串中最小字母字符
#9.4 max（），返回字符串中最大字母字符
text="Python"
print(min(text))
print(max(text))

#10.格式化字符串
#10.1 位置格式
text='{}{}'.format('aaa','bbb')
print(text)


text='{1}{0}{1}{2}{1}{0}'.format('aaa','bbb','ccc')
print(text)


#10.2 左对齐 <,默认对齐方式，可省略
text='{:10}'.format('hello')
print(text)

#10.3 右对齐 >,
text='{:>10}'.format('hello')
print(text)

text2='{:>10}'.format('python')
print(text2)

#10.4  f-string
name1='Jack1'
name2='Jack2'
name3='Jack3'
text=f'hello{name1}{name2}{name3}'
print(text)










