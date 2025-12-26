import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

#新增得分列，即仿照第二题
df=pd.read_excel("2025杭州周边考高二期中.xlsx")
s=[]
score=[9,7,6,5,4,3,2,1]

for i in range(len(df)):
    if df["名次"][i]<=8:
        s.append(df["名次"][i]-1)
    else:
        s.append(0)
df["得分"]=s


df1=df.groupby("班级",as_index=False)["得分"].sum()
df2=df1.sort_values("得分",ascending=False)
df3=df2.head(6)
print(df3)
plt.bar(df3.班级,df3.得分)
plt.show()