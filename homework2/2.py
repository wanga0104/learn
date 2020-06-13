people = int(input('请输入人数：'))
weight = int(input('请输入总重量：'))
if people >= 10 and weight <= 1000:
    print('电梯超载')
else:
    print('电梯正常运行')