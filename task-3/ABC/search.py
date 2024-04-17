import pandas as pd


A = pd.read_csv('updatedA1 .csv')['Email'].values.tolist()
B = pd.read_csv('updatedB2 .csv')['Email'].values.tolist()
c = pd.read_csv('updatedC3 .csv')['Email'].values.tolist()

final = A+B+ c

email = pd.read_csv('Email.csv')['Email'].values.tolist()


li = []

for e in email:
    if e not in final:
        li.append(e)
        
        
print(len(li))     
print((li))
li = pd.DataFrame(li,columns = ['Email'])
li.to_csv('ABC_unmatched.csv',index = False)