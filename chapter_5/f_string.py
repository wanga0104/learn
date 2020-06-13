name = 'andy'
login_time = 10
cost = 198.654
print('您好',name,'这是您第',login_time,'登陆！本次登陆您消费：',cost,'元',sep='')
print('您好%s这是您第%d登陆！本次登陆您消费：%.2f元'%(name,login_time,cost))
print('您好{}这是您第{}登陆！本次登陆您消费：{:.2f}元'.format(name,login_time,cost))
print(f'您好{name}这是您第{login_time}登陆！本次登陆您消费：{cost:.2f}元')