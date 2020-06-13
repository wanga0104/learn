sum = 0
number = 1
sum += number
for i in range(2,65):
    number *= 2
    sum = sum + number
print(sum)