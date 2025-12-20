s="Code25"
result=""

for i in range (len(s)):
    if i%2==0:
        if i+1<len(s):
            result+=s[i+1]+s[i]
        else:
            result+=s[i]
    else:
        result+=str(i%3)

print(result)