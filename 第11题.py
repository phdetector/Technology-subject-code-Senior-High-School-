import random

a=[0]*5
for i in range(5):
    x=random.randint(0,4)
    if x!=i:
        a[x]+=1
    else:
        a[i]=x

print(a)