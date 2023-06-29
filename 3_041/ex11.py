#factorial

n = int(input('enter number : '))
def facto(n):
    num = 1
    for i in range(n, 0, -1):
        num *= i

    return num

print(f'{n}! : {facto(n)}')

def selfFac(n):

    if n == 1:
        return 1

    return n * selfFac(n-1)

print(f'{n}! : {selfFac(n)}')
#재귀함수를 잘쓰면 코드가 간단해지고 쉽게 해결할 때에도 있다.