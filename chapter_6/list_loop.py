'''
foodlist = ['康师傅方便面', '冰红茶', '绿茶', ['哇哈哈哈', '矿泉水']]
#for循环
for name in foodlist:
    print(name)
#while循环
number = len(foodlist)
i = 0
while i < number:
    print(foodlist[i])
    i += 1
'''
foodlist1 = ['康师傅方便面', '冰红茶', '绿茶', ['哇哈哈哈', '矿泉水']]
foodlist2 = ['瓜子', '自行车', '茅台', ]
foodlist3 = ['剑南春', '五粮液', '拉菲',]
foodlist = [foodlist1, foodlist2, foodlist3]
#print(foodlist)

for name in foodlist1:
    for i in name:
        if not isinstance(i,list):
         print(i)
        else:
            for j in i:
                print(j)

# for i, value in enumerate(foodlist):
#         print(f'第{i+1}元素的值是{value}')
#         for j, name in enumerate(value):
#            print(f'第{j+1}元素的值是{name}')