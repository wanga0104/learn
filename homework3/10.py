
for i in range(1,20):
    for j in range(1,33):
        k = 100 - i -j
        if (k%3==0 and 5*i + 3*j + k//3 == 100):
            print(i, j, k)

i = 1
while i <= 20:
    j = 1
    while j <= 33:
        k = 100 - i -j
        if  5*i + 3*j + k/3 == 100 and k%3==0 :
            print(i, j, k)
        j += 1
    i += 1
