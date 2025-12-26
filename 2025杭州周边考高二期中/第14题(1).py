import pandas as pd

#(1)
df=pd.read_excel("2025杭州周边考高二期中.xlsx")
s=[]
score=[9,7,6,5,4,3,2,1]

for i in range(len(df)):
    if df["名次"][i]<=8:
        s.append(df["名次"]-1)
    else:
        s.append(0)
df["得分"]=s




