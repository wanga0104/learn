age = int(input('请输入年龄：'))
if age <= 0:
    print(f'请输入正确的年龄')
elif age <= 6:
    print(f'{age}属于童年')
elif 7 <= age <= 17:
    print(f'{age}属于少年')
elif 18 <= age <= 40:
    print(f'{age}属于青年')
elif 41 <= age <= 65:
    print(f'{age}属于中年')
elif age >65 :
    print(f'{age}属于老年')