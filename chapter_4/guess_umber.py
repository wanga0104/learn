secret_number = 8
guess_count = 0
guess_limit = 3
flag = False
while guess_count < guess_limit:
    guess = int(input('请输入数字：'))
    guess_count = guess_count + 1
    if guess == secret_number:
        flag = True
        break
    elif guess < secret_number:
        print('数字小了')
    else:
        print('数字大了')
if flag:
    print('恭喜你答对了！')
else:
    print('三次机会用完了！！')
print('游戏结束')