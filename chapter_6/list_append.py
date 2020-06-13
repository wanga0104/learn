'''
list = ['西游记', '三国演义']
list.append('水浒传')
list.insert(0,'红楼梦')
print(list)
kongfu = ['天龙八部', '笑傲江湖']
list.extend(kongfu)
print(list)
list[5] = '射雕英雄传'
print(list)
shu = '天龙八部'
if shu not in list:
    print(f'{shu}不在列表中')
else:
    print(f'{shu}在列表中')
print(list.count('天龙八部'))
print(list.index('射雕英雄传'))
del list[-1]
print(list)
list.pop()
print(list)
list.remove('西游记')
print(list)
'''
list_val = [14,16,17,89,90,45]
# list_val.sort(reverse=True)
# print(list_val)
# list_val.reverse()
# print(list_val)
new_list = list_val.copy()
print(new_list)
print(id(list_val))
print(id(new_list))