#循环中else子句
#1.for
for i in range(1,5):
    print(i)
    if i % 3==0:
        break
else:
    print('循环结束了。。。')

print('--------')

#2.while
count=0
while count<5:
    print(count,'is less than 5')
    count =count+1
    if count % 3==0:
        break
else:
    print(count,'is not less than 5')