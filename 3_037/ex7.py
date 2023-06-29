
a1 = int(input('enter first number : '))
r = int(input('enter gap : '))
n = int(input('enter how many : '))

an = a1 * (r**(n-1))
if r == 1:
    sn = a1 * n
else:
    sn = a1 * (1-r**(n)) / (1-r)

print(f'일반항 : {an}')
print(f'{n}번까지의 합 : {int(sn)}')

# an = 0
# sn = 0
# i = 1
# while i <= n:
#
#     if i == 1:
#         an = a1
#         sn += an
#         i += 1
#         continue
#
#     an *= r
#     sn += an
#     i += 1
#
# print(f'일반항 : {an}')
# print(f'{n}번까지의 합 : {sn}')