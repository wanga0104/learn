print('请输入如下菜单编号:\n0:退出系统\n1：加法运算\n2：减法运算\n3：乘法运算\n4：除法运算')
cpu = int(input('请输入菜单编号:'))
if cpu == 1:
    i = float(input('请输入第一个数字：'))
    j = float(input('请输入第一个数字：'))
    print('加法运算')
    print(f'{i}+{j}={i+j:.1f}')
elif cpu == 2:
    print('减法运算')
    i = float(input('请输入第一个数字：'))
    j = float(input('请输入第一个数字：'))
    print(f'{i}-{j}={i-j:.1f}')
elif cpu == 3:
    print('乘法运算')
    i = float(input('请输入第一个数字：'))
    j = float(input('请输入第一个数字：'))
    print(f'{i}*{j}={i*j:.1f}')
elif cpu == 4:
    print('除法运算')
    i = float(input('请输入第一个数字：'))
    j = float(input('请输入第一个数字：'))
    print(f'{i}/{j}={i / j:.1f}')
else:
    print('退出系统')