s = int(input('enter Start Number : '))
r = int(input('enter ratio : '))
n = int(input('enter how many : '))

nValue = s * (r ** (n - 1))

print(f'공비가 {r}인 {n}번째항 : {nValue} ')

#등비중항
s = int(input('enter Start Number : '))
r = int(input('enter ratio : '))
n = int(input('enter how many : '))

nmValue = s * (r ** ((n-1) - 1))
npValue = s * (r ** ((n+1) - 1))

between = (nmValue * npValue) ** (1/2)
print(f'등비중항 구하기 {nmValue}, {npValue} = {between}')

