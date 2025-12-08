import pandas as pd

df=pd.read_csv("Sports_data.csv")
print(df.info())
unique_dict = {col: df[col].unique().tolist() for col in df.columns}
print(unique_dict)

df2=df[df['enjoy sport']=='yes']
df2=df2.drop(columns=['enjoy sport'])
#print(len(df2.columns))
h1=['Ø']*(len(df2.columns))
k=0
for i in df2.columns:
    for j in df2[i]:
        if(h1[k]=='Ø'):
            h1[k]=j
        
        elif(j!=h1[k]):
            h1[k]='?'
    k+=1
print("Final Hypothesis")
print(h1)
