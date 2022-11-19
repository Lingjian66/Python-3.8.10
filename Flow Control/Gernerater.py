#生成器
def countdown(num):
    print('Starting...')
    while num>0:
        yield num
        num -=1

gen=countdown(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))