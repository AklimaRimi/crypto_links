import os
import pandas as pd


df1 = pd.read_csv('info2.csv')['Project Info'].values.tolist()
df2 = pd.read_csv('info3.csv')['Links'].values.tolist()


print(len(df1), len(df2))

df1.sort()

print([x for x in df2 if x not in df1])
    
        
# df2 = pd.read_csv('coinrank_links.csv')
# df2 = df2.drop_duplicates(['Links'])

# # print( df2['Project Info'].value_counts()[:10])
# df2.to_csv('info3.csv',index=False)