inputN = int(input('enter number : '))

nValue = 0
sumValue = 0

n=1
while n <= inputN:

    if n==1 or n==2:
        nValue = 1
        nPreVal1 = nValue
        nPreVal2 = nValue
        sumValue += nValue
        n += 1
    else:
        nValue = nPreVal2 + nPreVal1
        nPreVal2 = nPreVal1
        nPreVal1 = nValue
        sumValue += nValue
        n += 1

print(f'{inputN} 번째 항 : {nValue}')
print(f'{inputN} 번째 까지 합 : {sumValue}')
