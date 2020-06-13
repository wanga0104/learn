import  random
num = int(input('请输入：剪刀（0）石头（1）布（2）：'))
pc = random.randint(0,2)
if num == 0 and pc == 0 or num == 1 and pc == 1 or num == 2 and pc == 2:
    print(f'你们都是{num}，打平手了！')
elif num == 0 and pc == 1 or num == 1 and pc == 2 or num == 2 and pc == 0:
    print(f'您输入的是{num}电脑输入的是{pc}\n您输了！')
elif num == 0 and pc == 2 or num == 1 and pc == 0 or num == 2 and pc == 1:
    print(f'您输入的是{num}电脑0输入的是{pc}\n获胜，你太厉害了！')