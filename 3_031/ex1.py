'''
100부터 1000 시이의 난수를 생성하고
그 난수의 <약수, 소수, 소인수>를 출력하는 프로그램 만들기
'''

import random
num = random.randint(100, 1000)
print(f'random number is {num}')

for i in range(1, num+1):
    bothFlag = 0
    #약수
    if num % i == 0:
        print(f'약수 : {i}')
        bothFlag += 1

    #소수
    if i != 1:
        flag = True
        for n in range(2, i):
            if i % n == 0:
                flag = False
                break

        if flag:
            print(f'소수 : {i}')
            bothFlag += 1

    #소인수
    if bothFlag >= 2:
        print(f'소인수 : {i}')

