
flag = True
n = 1
nCnt = 1; c = 0 ; p = 0
sum = 0

while flag:

    for i in range(1, (n+1)):
        print(f'{i}/{n-i+1} ', end='')

        sum += i / (n-i+1)
        nCnt += 1

        if sum > 100:
            c = i
            p = n-i+1
            flag = False
            break

    print()
    n += 1

print(f'{nCnt} {c}/{p} {round(sum, 2)}')