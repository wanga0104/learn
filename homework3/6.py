import time
min = 2
flag = True
while flag:
    for m in range(min,-1,-1):
        if min == 0:
            flag = False
            break
        for sencond in range(59, -1,-1):
            time.sleep(1)
            print(f'{min-1:02}:{sencond:02}')