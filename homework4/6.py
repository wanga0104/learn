'''a = ['andy','18','男','大熊','167','233','18','18']
#b = set(a)
print(list(set(a)))
'''
a = ['andy','18','男','大熊','167','233','18','18']
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)