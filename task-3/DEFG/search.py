import pandas as pd


A = pd.read_csv('updatedD4 .csv')['Email'].values.tolist()
B = pd.read_csv('updatedE5 .csv')['Email'].values.tolist()
c = pd.read_csv('updatedF6 .csv')['Email'].values.tolist()
d = pd.read_csv('updatedG7 .csv')['Email'].values.tolist()

final = A+B+ c + d

email = pd.read_csv('email.csv')['Email'].values.tolist()


li = []

for e in email:
    if e not in final:
        li.append(e)
        
print((li))        
print(len(li))     

li = pd.DataFrame(li,columns = ['Email'])
li.to_csv('DEFG_unmatched.csv',index = False)