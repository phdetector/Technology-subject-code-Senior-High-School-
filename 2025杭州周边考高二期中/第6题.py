import random

a=[0]*6
i=0

while i<6:
    a[i]=random.randint(1,10)
    if a[i]%2!=i%2:
        a[i]=a[i]-1
    i=i+1

print(a)