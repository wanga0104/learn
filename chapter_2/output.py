#最简单的输出
print('hello world')
#输出变量
price = 20
number = 5
print('总花费',price*number)
#sep分隔符
print('hello','world')
print('hello','world',sep=',')
print('2019','12','12',sep='-')
print('wanga0104','gmail',sep='@')
#end 结束符
print('hello')
print('world')

print('hello''\n')
print('world')
#file
file_source = open('zen.txt','w')
print('人生苦短，我用Python！',file=file_source)
file_source.close()