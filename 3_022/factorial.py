'''
1부터 양의 정수 n까지의 정수를 모두 곱한 것
0! 은 1로 약속
'''
inputN = int(input('enter number : '))

#for사용
result = 1
for n in range(1, inputN+1):
    result *= n

print(f'{n}의 팩토리얼 {result}')

#재귀함수 사용
def facFunc(n):
    if n == 1:
        return 1
    return n * facFunc(n - 1)

print(f'{inputN}의 팩토리얼 {facFunc(inputN)}')

#while 사용
result = 1
n = 1
while n <= inputN:
    result *= n
    n += 1

print(f'{inputN}의 팩토리얼 {result}')

#math module사용
import math

print(f'{math.factorial(inputN)}')
