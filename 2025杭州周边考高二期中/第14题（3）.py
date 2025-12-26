import pandas as pd

df=pd.read_excel("2025杭州周边考高二期中.xlsx")
df_q=df.groupby("姓名",as_index=False).count()
sum=0
for i in range(len(df_q)):
    if df_q["比赛项目"][i]==3:
        sum+=1
print(sum)
