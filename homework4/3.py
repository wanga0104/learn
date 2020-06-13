list = ['Andy','男',18,'篮球','唱歌','跳舞','看书','Python老司机']
list_str = [str(i) for i in list]
value_key = input('输入你要查找下标的元素：')
print(f'您需要查找的元素{value_key}，对应的下标为:',list_str.index(value_key))
