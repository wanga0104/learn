list1 = ['积善成德神明自得','hello','world']
list2 = ['hello','world',40,50,'大熊课堂']
#print(list(set(list2).difference(set(list1))))
list3 = []
for i in  list1:
    if i  in list2:
        list3.append(i)
print(f'{list1}和{list2}中有相同元素 相同元素为{list3}')