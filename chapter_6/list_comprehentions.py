# list = [i ** 2 for i in range(21) if not i % 2 == 0 ]
# print(list)
# new_list = [i if i > 100 else i ** 2 for i in list]
# print(new_list)
list_val = []
for i in '高富帅':
    for j in '白富美':
        list_val.append(i+j)
print(list_val)
print([i+j for i in '高富帅' for j in '白富美'])