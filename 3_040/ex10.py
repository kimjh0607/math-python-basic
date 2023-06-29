
n = int(input('enter n : '))

nVal = 0
sum = 0

nPreVal1 = 0
nPreVal2 = 0

i = 1
while i <= n:
    if i == 1 or i == 2:
        nVal = 1
        nPreVal1 = nVal
        nPreVal2 = nVal
        sum += nVal
        i += 1
        continue #이거안해주면 답 이상하게 나옴.. 아니면 else를 확실하게 해주어야 함..

    nVal = nPreVal1 + nPreVal2
    sum += nVal
    nPreVal2 = nPreVal1
    nPreVal1 = nVal
    i += 1

print(f'{i}번쨰 값 - {nVal}, 합 - {sum}')
