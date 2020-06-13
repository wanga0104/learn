import  random
basket = ['香蕉','苹果','鸡蛋','面包','葡萄','南果梨','牛奶']
print('这个篮子里面有:')
for i in basket:
         print(i)
print('这个篮子里面还剩（去掉非水果）:')
list2 = ['鸡蛋','面包','牛奶']
for i in list2:
    basket.remove(i)
for i in basket:
    print(i)
print('给这个篮子里面还剩（添加草莓菠萝）:')
list3 = ['草莓','菠萝']
list4 = basket+list3
for i in list4:
    print(i)
print('从这个篮子里面随机取2种水果:')
list5 = random.sample(list4,k=2)
for i in list5:
    print(i)