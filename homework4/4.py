words = ['da','xiong','121121','hello','andy','想一想','zz']
count = 0
for i in words:
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1
print(f'符合条件的个数是{count}')