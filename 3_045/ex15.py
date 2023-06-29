
def function():
    n = int(input('enter n : '))
    r = int(input('enter r : '))
    resP = 1
    resR = 1
    resC = 1

    for i in range(n, n-r, -1):
        resP *= i

    print(f'{n}P{r} : {resP}')

    for i in range(r, 0, -1):
        resR *= i

    print(f'{r}! : {resR}')

    resC = int(resP / resR)
    print(f'{n}C{r} : {resC}')

    return resC

sample = function()
print(f'sample : {sample}')
event1 = function()
print(f'event1 : {event1}')
event2 = function()
print(f'event2 : {event2}')

probab = (event1 * event2) / sample
print(f'확률 : {round(probab*100, 2)}%')
