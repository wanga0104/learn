# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)
for i in range(1,10):
    for j in range(1,i+1):
        #print(i, '*', j, '=', i * j,end='  ')
        #print(f'{i}*{j}={i*j}',end='  ')
        print('{}*{}={}'.format(i,j,i*j),end='  ')
    print('\n')


list = [123, 456]
print(type(list))