for i in range(1,11):
    if i % 3==0:
        continue
    else:
        print(i)

print("-----")
i=1
while True:
    if i % 3==0:
        break
    print(i)
    i=i+2