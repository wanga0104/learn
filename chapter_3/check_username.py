username = input('请输入一个用户名：')
if len(username) < 3:
    print('用户名不能小于三个字符')
elif len(username) > 50:
    print('用户名不能大于50个字符')
else:
    print('用户名可用！')