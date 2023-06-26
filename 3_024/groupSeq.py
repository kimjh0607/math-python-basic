'''
1,1,2,1,2,3,1,2,3,4,1,2,3,4,5 ...
nCnt : 항의 수
searchN : 그 항의 담긴 숫자
'''
inputN = int(input('enter number : '))
flag = True
n = 1
nCnt = 1
searchN = 0

while flag:

    for i in range(1, (n+1)):
        print(f'{i} ', end='')

        nCnt += 1

        if (nCnt > inputN):
            searchN = i
            flag = False
            break

    print()
    n += 1
print(f'{inputN}항 : {searchN}')
