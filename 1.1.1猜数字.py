from random import randint
x=randint(0,300)
for n in range(10):
    print '输入一个数：'
    y=input()
    if y==x:
        print'正确'
    elif y>x:
        print'大了'
    else:
        print'小了'
print'超过次数'