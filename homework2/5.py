a = int(input('请输入第一个数：'))
b = int(input('请输入第二个数：'))
c = int(input('请输入第三个数：'))
if a == b or b == c  or a == c:
    print('0')
else:
    print(f'{a+b+c}')