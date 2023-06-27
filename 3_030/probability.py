'''
ex) 빨간구슬3 파란구슬4
빨간구슬 1 파란구슬2 뽑을 확률 > 3C1 * 4C2 / 7C3 = 18/35
'''
def first():
    n = int(input('enter number : '))
    r = int(input('enter number : '))

    resP = 1
    resC = 1
    resR = 1

    for i in range(n, n-r, -1):
        resP *= i
    print(f'{resP}')

    for i in range(r, 0, -1):
        resR *= i
    print(f'{resR}')

    resC = int(resP / resR)
    print(f'{resC}')

    return resC

sample = first()
print(f'sample : {sample}')

event1 = first()
print(f'event1 : {event1}')

event2 = first()
print(f'event2 : {event2}')

probab = (event1 * event2) / sample
print(f'확률 : {round(probab*100, 2)}%')