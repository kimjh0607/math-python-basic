inputNum = int(input('enter number : '))

n = 2
while n <= inputNum:
    if inputNum % n == 0:
        print(f'{n}은 {inputNum}의 소인수')
        inputNum /= n
    else:
        n += 1