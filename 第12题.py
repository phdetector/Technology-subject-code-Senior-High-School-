#以下Python程序用于处理字符串数组，
# 将每个字符串中的数字字符提取出来并反转，然后过滤掉空字符串，
# 如数组 arr=["alb2c3","hello","x4y5z6","no_digits"]，输出结果为['321’,"654"]


import random

def p_str(arr):
    result=[]
    for s in arr:
        dgs=""
        for char in s:
            if char>="0" and char<="9":
                dgs+=char
        rever=""
        for i in range(len(dgs)-1,-1,-1):
            rever+=dgs[i]
        if len(rever)>0:#rever!=""也可以
            result.append(rever)
    return result

arr=["a1b2c3","hello","x4y5z6","no_dgs"]
print(p_str(arr))