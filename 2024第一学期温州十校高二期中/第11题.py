def prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

a=int(input('请输入一个大于等于四的偶数'))
for i in range(2,a):
    j=a-i
    if prime(j) and prime(i):
        print('YES')
        print(str(a)+'='+str(i)+'+'+str(j))
        break