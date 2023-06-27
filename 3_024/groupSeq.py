'''
1,1,2,1,2,3,1,2,3,4,1,2,3,4,5 ...
nCnt : 항의 수
searchN : 그 항의 담긴 숫자
'''
inputN = int(input('enter number : '))
flag = True
n = 1
nCnt = 1
searchNC = 0
searchNP = 0

while flag:

    for i in range(1, (n+1)):
        print(f'{i}/{n-i+1},', end='')

        nCnt += 1

        if (nCnt > inputN):
            searchNC = i
            searchNP = n-i+1

            flag = False
            break

    print()
    n += 1

print(f'{inputN}항 : {searchNC}.{searchNP}')
