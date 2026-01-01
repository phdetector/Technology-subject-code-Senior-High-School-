import random

flag=[0]*6
lst=[]
while sum(flag)!=5:
    a=random.randint(1,5)
    lst.append(a)
    flag[a]=1
print(lst)