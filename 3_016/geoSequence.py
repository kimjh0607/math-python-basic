input1 = int(input('enter 1st number : '))
inputD = int(input('enter gap(d) number : '))
inputN = int(input('enter numTh : '))

nValue = 0
n = 1
while n <= inputN:
    if n == 1:
        nValue = input1
        #print(f'{n}th value : {nValue}')
        n += 1
        continue

    nValue *= inputD
    #print(f'{n}th value : {nValue}')
    n += 1

print(f'{inputN}th value : {nValue}')