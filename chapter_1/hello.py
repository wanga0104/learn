start = int(input('请为《叶问》的电影评分(请输入1-10):'))
if start > 10 or start <= 0:
    print ('数字不能大于10或者小于0')
else:
    print('您为《叶问》的电影打分为',start*'⭐')