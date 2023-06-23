num1 = int(input('enter number1 : '))
num2 = int(input('enter number2 : '))
maxNum = 0
for i in range(1, (num1+1)):
    if num1 % i == 0 and num2 % i == 0:
        maxNum = i

print(f'{maxNum}는 {num1}, {num2}의 최대공약수')
print(f'{(num1 * num2) /maxNum}는 {num1}, {num2}의 최소공배수')

#2
# minNum = num1 * num2 / maxNum
# print(f'{minNum}는 {num1}, {num2}의 최소공배수')

#세자리의 최소공배수 구하기
#두개의 수로 먼저 최소공배수를 구하고 그 값과 세번쨰 숫자의 최소공배수를 구하면 됨.
n1 = int(input('enter number1 : '))
n2 = int(input('enter number2 : '))
n3 = int(input('enter number3 : '))

maxN = 0
for i in range(1, (n1+1)):
    if n1 % i == 0 and n2 % i == 0:
        maxN = i

minN = int(n1 * n2 // maxN)

#두번째 최대공약수
maxN2 = 0
for i in range(1, (maxN+1)):
    if n3 % i == 0 and maxN % i == 0:
        maxN2 = i

print(f'{maxN2} is {n1}, {n2}, {n3}\'s Max Common Divisor')
minN2 = (minN * n3) // maxN2
#minN2 = (n1 * n2 * n3) // maxN2
print(f'{minN2} is {n1}, {n2}, {n3}\'s Least Common Multiple')