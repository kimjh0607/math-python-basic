n = int(input('enter number : '))
r = int(input('enter choice : '))
result = 1

for i in range(n , n-r, -1):
    print(f'{i}')
    result *= i

print(f'{n}P{r}은 : {result}')