'''
def take_second(elem):
    return elem[1]
list = [(2,5),(1,2),(4,4),(2,3),(2,1)]
#list = [(2,2), (3,4), (4,1), (1,3)]
list.sort(key=take_second,reverse=True)
print(list)
'''
list = [(2,5),(1,2),(4,4),(2,3),(2,1)]
list.sort(key=lambda i:i[1],reverse=True)
print(list)