'''
sequence
an = a1+(n-1)*d
Sn = n*(a1+an)/2
'''

#1
a1 = int(input('enter first number : '))
d = int(input('enter gap : '))
n = int(input('enter how many : '))

# an = a1 + (n-1)*d
# print(f'일반항 a{n} : {an}')
#
# sn = int(n*(a1+an) / 2)
# print(f'{n}항 까지의 합 : {sn}')

#2
an = 0
sn = 0
i = 1
while i <= n:

    if i == 1:
        an = a1
        sn += a1
        i += 1
        continue

    else:
        an += d
        sn += an
        i += 1

print(f'일반항 : {an}')
print(f'{n}번째 까지의 합 : {sn}')



