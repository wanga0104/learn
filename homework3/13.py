cont = 0
while cont < 3:
    name = input('请输入你的用户名:')
    passwd = input('请输入你的密码：')
    if name == 'aaa' and passwd == 'bbb':
            print('登陆成功！')
            break
    else:
        cont += 1
        print(f'登陆失败！\n 您还有{3-cont}次机会')
else:
        print('登陆次数超过3次，账号已经锁定!')
