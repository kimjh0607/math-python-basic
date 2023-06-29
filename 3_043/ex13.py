n = int(input('enter n : '))
r = int(input('enter r : '))
result = 1

for i in range(n, n-r, -1):
    result *= i

print(f'{n}P{r} : {result}')
