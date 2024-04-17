import pandas as pd

df =  pd.read_csv('info.csv')

df['Website'] = df['Website'].apply(lambda x: str(x).split('?ref')[0])

df.to_csv('info2.csv',index = False)