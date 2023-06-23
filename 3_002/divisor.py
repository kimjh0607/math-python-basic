num = int(input('enter number : '))

for i in range(1,(num+1)):
    if num % i == 0:
        print(f'{i}는 {num}의 약수')