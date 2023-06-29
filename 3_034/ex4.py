import random
rNum1 = random.randint(100, 1000)
rNum2 = random.randint(100, 1000)

print(f'random number1 is {rNum1}')
print(f'random number2 is {rNum2}')

max = 0
for i in range(1, min(rNum1, rNum2)+1):
    if rNum1 % i == 0 and rNum2 % i == 0:
        print(f'공약수 {i}')
        max = i
print(f'최대공약수 : {max}')

min = (rNum1 * rNum2) / max
print(f'최소공배수 : {round(min, 2)}')