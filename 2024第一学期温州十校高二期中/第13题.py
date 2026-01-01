#奇校验

ch=input('请输入一个ascll码字符：')
ans=0
s=''
x=ord(ch)

while x>0:#原题目为‘x>=0,错误的’
    ans=ans+x%2
    s=str(x%2)+s
    x=x//2
if ans%2==1:
    s='0'+s
else:
    s='1'+s

print('生成的奇校验码为',s)