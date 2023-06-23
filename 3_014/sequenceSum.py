# input1 = int(input('enter 1st number : '))
# inputD = int(input('enter gap(d) number : '))
# inputN = int(input('enter numTh : '))
#
# nValue = 0
# n = 1
# sumValue = 0
# while n <= inputN:
#     if n == 1:
#         nValue = input1
#         sumValue += nValue
#         print(f'{n}th value : {nValue}')
#         print(f'{n}th sum  : {sumValue}')
#         n += 1
#         continue
#
#     nValue += inputD
#     sumValue += nValue
#     print(f'{n}th value : {nValue}')
#     print(f'{n}th sum  : {sumValue}')
#     n += 1
#
# print(f'{inputN}th value : {nValue}')
# print(f'{inputN}th sum  : {sumValue}')

#2
input1 = int(input('enter 1st number : '))
inputD = int(input('enter gap(d) number : '))
inputN = int(input('enter numTh : '))

#an = a1 + (n-1) * d
nValue = input1 + ((inputN - 1) * inputD)

#Sn = n(a1 + an) / 2
sumValue = (inputN * (input1 + nValue)) / 2

print(f'일반항 구하기 : {nValue}')
print(f'n번째 까지 합 구하기 : {sumValue}')

