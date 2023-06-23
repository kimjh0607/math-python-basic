num1 = int(input('enter number1 : '))
num2 = int(input('enter number2 : '))

temp1 = num1
temp2 = num2

while temp2 > 0:
    temp = temp2
    temp2 = temp1 % temp2
    temp1 = temp

print(f'{num1}, {num2}의 최대공약수 : {temp1}')

for i in range(1,(temp1+1)):
    if temp1 % i == 0:
        print(f'{num1}, {num2}의 공약수는 : {i}')
