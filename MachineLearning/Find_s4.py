import pandas as pd

df=pd.read_csv("dataset.csv")

df2=df[df['Yes']=='Yes']

df2=df2.drop(columns=['Yes'])
print(df2.columns)
h1=['Ø']*(len(df2.columns))
print(h1)
k=0
for i in df2.columns:
    for j in df2[i]:
        if h1[k]=='Ø':
            h1[k]=j
        elif h1[k]!=j:
            h1[k]='?'
    k=k+1
print("Final Hypothesis")
print(h1)
