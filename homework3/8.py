all_money = 10000
while all_money > 0:
    money = int(input('少侠请下注：'))
    if money > all_money:
        print('投注超出了总资产，请重新投注')
    elif money == 0:
        print('下点真金白银')
    else:
        import random
        you = random.randint(1,6)
        pc = random.randint(1,6)
        if you > pc:
            print(f'你摇出了{you}\n庄家摇出了{pc}\n恭喜了，你赢了，如果继续赌博早晚会输光，您身上还有{all_money+money}')
            all_money += money
        elif you <= pc:
            print(f'你摇出了{you}\n庄家摇出了{pc}\n，您输了输了，如果继续赌博早晚会输光，您身上还有{all_money-money}')
            all_money -= money
else:
    print('少侠您身上上已经没有钱了！游戏结束')

