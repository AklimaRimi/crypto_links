import pandas as pd
import os


file1 = pd.read_csv('P16 - P16.csv')
file2 = pd.read_csv('email.csv')
# li = []
# with open('LMP/new.txt','r') as f:
#     x = f.read()
#     li =[i.replace("\'",'').replace(' ','') for i in x.split(',')]
    
# print(li)





noot_found = []
file1['web'] = file1['Website'].apply(lambda x: str(x).replace('https:','').replace('http:','').replace('/','').replace('www.','').replace(' ',''))
# file1.to_csv('updatedFilterEmail.csv',index = False)
for i in  file2['Email'].values.tolist():
    
    # file1['web'] = file1['Website'].apply(lambda x: sorted(str(x).split('/'))[-1].replace('www.',''))
    print(i)
    matching_indices = []
    indx = i.index('@')
    i1 = i[indx+1:].replace(' ','').lower()
    
    for w in range(len(file1['web'].values.tolist())):
        # print(file1['web'][w],i)
        comp = file1['web'][w]
        if len(comp) > 4 and ((i1 ==  comp) or (comp == i1) or (comp.find(i1) != -1)):
            print(file1['web'][w], i1)
            matching_indices.append([str(file1['Main Link'][w]).lower(),w])

    # print(ind)
    print(len(matching_indices))
    check = 0
    if len(matching_indices)> 0 :
        
        if check == 0:
            for x in matching_indices:
                if 'coingecko' in x[0]:
                    check = 1
                    file1.loc[x[1], 'Email'] = i
                    
        if check == 0:
            for x in matching_indices:
                if 'coinmarketcap' in x[0]:
                    check = 1
                    file1.loc[x[1], 'Email'] = i
                    
        if check == 0:
            for x in matching_indices:
                if 'coinranking' in x[0]:
                    check = 1
                    file1.loc[x[1], 'Email'] = i
        if check == 0:
            for x in matching_indices:
                if 'coincarp' in x[0]:
                    check = 1
                    file1.loc[x[1], 'Email'] = i
                    
        if check == 0:
            for x in matching_indices:
                if 'coincheckup' in x[0]:
                    check = 1
                    file1.loc[x[1], 'Email'] = i
                    
        if check == 0:
            for x in matching_indices:
                if 'livecoinwatch' in x[0]:
                    check = 1
                    file1.loc[x[1], 'Email'] = i
                    
        if check == 0:
            for x in matching_indices:
                if 'coinvote' in x[0]:
                    check = 1
                    file1.loc[x[1], 'Email'] = i
                    
        if check == 0:
            for x in matching_indices:
                if 'coindiscovery' in x[0]:
                    check = 1
                    file1.loc[x[1], 'Email'] = i
        
        if check == 0:
            for x in matching_indices:
                if 'coinmoon' in x[0]:
                    check = 1
                    file1.loc[x[1], 'Email'] = i
                    
        if check == 0:
            for x in matching_indices:
                if 'coinscop' in x[0]:
                    check = 1
                    file1.loc[x[1], 'Email'] = i
                    
        if check == 0:
            for x in matching_indices:
                if 'icoholder' in x[0]:
                    check = 1
                    file1.loc[x[1], 'Email'] = i
                    
        if check == 0:
            for x in matching_indices:
                if 'coinarbitrage' in x[0]:
                    check = 1
                    file1.loc[x[1], 'Email'] = i
    else:
        noot_found.append(i)
 
    
file1 = file1.drop(columns=['web'])
# file1 = file1.sort_values(['Main Link','Full Name','Email'])
file1.to_csv('updatedP16 .csv',index = False)
print(len(noot_found))

