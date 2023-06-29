a1 = int(input('enter first number : '))
r = int(input('enter gap : '))
n = int(input('enter how many : '))

an = 0
sn = 0
i = 1
while i <= n:

    if i == 1:
        an = a1
        sn += an
        i += 1
        continue

    an *= r
    sn += an
    i += 1

print(f'{n}번까지의 받은 쌀 {sn}톨')