num = int(input('enter number : '))

for i in range(2, (num + 1)):
    flag = True
    for n in range(2,i):
        if i % n == 0:
            flag = False #소수가 아님.
            break

    if (flag):
        print(f'{i}는 소수')
    else:
        print(f'{i}는 Not소수')


