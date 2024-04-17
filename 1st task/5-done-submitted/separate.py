import os
import pandas as pd


df1 = pd.read_csv('coinbot_links.csv')['Links'].values.tolist()
df2 = pd.read_csv('coinbot_info.csv')


df = []
for i in df1:
    i= i.replace('\t','')
    df = df2[df2['Project Info'] == i]
    df.to_csv('info.csv',index=False,mode='a',header=False)
    
df = pd.read_csv('info.csv')
df = df.drop_duplicates()
df.to_csv('info.csv',index=False)  
