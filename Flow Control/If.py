#园博园购票
print("请出示身份证")
city=input()
if 'beihai'==city:
    print('门票10元/人')
    print('请输入年龄：')
    age=int(input())   #int()将字符串转换为整数
    if age >=60:
        print('老年人免费游玩')
    else:
        print('请扫码支付...')
elif 'nanning'== city or 'qinzhou'==city:
    print('门票20元/人')
else:
    print('门票60元/人')
