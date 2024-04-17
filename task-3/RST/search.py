import pandas as pd


A = pd.read_csv('updatedR18 .csv')['Email'].values.tolist()
B = pd.read_csv('updatedS19 .csv')['Email'].values.tolist()
c = pd.read_csv('updatedT20 .csv')['Email'].values.tolist()

final = A+B+ c

email = pd.read_csv('email.csv')['Email'].values.tolist()


li = []

for e in email:
    if e not in final:
        li.append(e)
        
        
print(len(li))     
print((li))
li = pd.DataFrame(li,columns = ['Email'])
li.to_csv('unmatched.csv',index = False)