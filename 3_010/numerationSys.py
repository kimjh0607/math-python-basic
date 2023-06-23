'''
bin(number)
oct(number)
hex(number)
반환타입은 string
'''
dNum = 30
print(f'2진 : {bin(dNum)}') #0binary
print(f'8진 : {oct(dNum)}') #0Oct
print(f'16진 : {hex(dNum)}') #0Hex

print('2진 : {}'.format(format(dNum , '#b')))
print('8진 : {}'.format(format(dNum , '#o')))
print('16진 : {}'.format(format(dNum , '#x')))

print('2진 : {}'.format(format(dNum , 'b')))
print('8진 : {}'.format(format(dNum , 'o')))
print('16진 : {}'.format(format(dNum , 'x')))

print('2 : {0:#b}, 8 : {0:#o}, 16 : {0:#x}'.format(dNum, dNum, dNum))
print('2 : {0:#b}, 8 : {0:#o}, 16 : {0:#x}'.format(dNum))

print(f'2진수 : {type(bin(dNum))}') #0binary
print(f'8진수 : {type(oct(dNum))}') #0Oct
print(f'16진수 : {type(hex(dNum))}') #0Hex

print('2진수 > 10진수 = {}'.format(int('0b11110', 2)))
print('8진수 > 10진수 = {}'.format(int('0o36', 8)))
print('16진수 > 10진수 = {}'.format(int('0x1e', 16)))