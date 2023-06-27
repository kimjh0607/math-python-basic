import random

rNum1 = random.randint(100, 1000)
rNum2 = random.randint(100, 1000)
print(f'num1 is {rNum1}')
print(f'num2 is {rNum2}')

max = 0
for i in range(1, min(rNum1, rNum2)+1):
    if rNum1 % i == 0 and rNum2 % i == 0:
        print(f'공약수 : {i}')
        max = i

print(f'최대공약수 : {max}')

if max == 1:
    print(f'{rNum1}과 {rNum2}은 서로소이다.')