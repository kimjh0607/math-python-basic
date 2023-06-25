#등차수열 합 - 1초항 2공차 3항갯수
a1 = int(input('enter 1st number : '))
d = int(input('enter gap : '))
n = int(input('enter how many : '))
an = a1 + (n-1)*d #일반항 an 구하기
sn = n*(a1+an) / 2 #n까지의 합 Sn구하기
print(f'{n}th number : {an}')
print(f'Sum up to {n}th number : {sn}')

#등비수열 합
a1 = int(input('enter 1st number : '))
r = int(input('enter gap : '))
n = int(input('enter how many : '))

an = a1 * (r ** (n-1))
sn = a1 * (1 - (r**n)) / (1-r)
print(f'{n}th number : {an}')
print(f'Sum up to {n}th number : {sn}')