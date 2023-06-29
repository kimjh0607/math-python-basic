def solution(n):
    cnt1 = bin(n).count('1')

    next = n + 1

    while bin(next).count('1') != cnt1:
        next += 1

    return next


number = int(input('enter number : '))
print(f'{solution(number)}')