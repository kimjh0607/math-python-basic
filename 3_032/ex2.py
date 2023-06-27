import random

ranNum = random.randint(100, 1000)
print(f'random number is {ranNum}')
list = []

n = 2
while n <= ranNum:
    if ranNum % n == 0:
        print(f'{n} is soinsu separate')
        list.append(n)
        ranNum /= n
    else:
        n += 1

print(list)

tempNum = 0
for s in list:
    if tempNum != s:
        print(f'{s}\'s count : {list.count(s)}')
        tempNum = s

