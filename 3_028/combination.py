n = int(input('enter number : '))
r = int(input('enter choice : '))
resP = 1
resC = 1
resR = 1

for i in range(n, n-r, -1):
    print(f'{i}')
    resP *= i

print(f'순열 {n}P{r} : {resP}')

for i in range(r, 0 , -1):
    print(f'{i}')
    resR *= i

print(f'팩토리얼 r : {resR}')

resC = int(resP / resR)
print(f'조합 {n}C{r} : {resC}')

#실습
res = (1 / resC) * 100
print('{}%'.format(round(res, 2)))