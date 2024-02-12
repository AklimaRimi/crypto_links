import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings
import multiprocessing as mp
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium import webdriver
driver = webdriver.Chrome()

driver.get(f'https://coincodex.com/')
time.sleep(2)

df = pd.read_csv(f'links.csv')
x =  len(df)//50
for page in range(x+1,5):

    try:
        lis = []        
        # window_height = driver.execute_script("return window.innerHeight;")
        # driver.execute_script(f"window.scrollBy(0, {window_height*});")
        li = driver.find_elements(By.XPATH,"//a[@class='coin-name']")
        print(page,len(li))

        for i in li:
            lis.append(i.get_attribute('href'))
        df  = pd.DataFrame(lis)

        print(page,len(df))
        df.to_csv('links.csv',index=False,mode='a',header=False)
        driver.find_element(By.XPATH,"//div[@class='load-more homepage-not-found']").click()
        time.sleep(5)
      
    except:
        continue
time.sleep(1)

li = driver.find_elements(By.XPATH,"//a[@class='coin-name']")
print(len(li))

for i in li:
    lis.append(i.get_attribute('href'))
df  = pd.DataFrame(lis)

print(page,len(df))
df.to_csv('links.csv',index=False,mode='a',header=False)

# df = pd.read_csv(f'deleted.csv')['Links'].values.tolist()
# df2 = pd.read_csv(f'coinvote_links.csv')
# df2 = df2.drop_duplicates()
# df3 = pd.read_csv(f'coinvote_info.csv')['Project Info'].values.tolist()
# lis = df2['Links'].values.tolist()
# lis = [x for x in lis if (x not in df) and (x not in df3)]

# print(len(lis))

# def scrap(li):
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     for i in li:
#         try:
#             print(i,'\n\n\n')

#             driver.get(f'{i}')
#             time.sleep(3)
#             full_name = driver.find_element(By.XPATH,"/html/body/div[3]/div[10]/div/div/div[3]/div[1]/div[1]/h2").text
#             new_len = driver.find_element(By.XPATH,'/html/body/div[3]/div[10]/div/div/div[3]/div[1]/div[1]/h2/b').text
#             full_name = full_name[:-len(new_len)]
            
#             # social_media = driver.find_elements(By.XPATH,"//a[@class='ng-scope']")
            
#             telegram = ''
#             twitter = ''
#             li = driver.find_elements(By.XPATH,"//a[@class='btn btn-primary btn-vote']")
#             for a in li:
#                 link = a.get_attribute('href')
#                 print(link)
#                 if link is not None and 't.me' in link:
#                     telegram = link
#                 if link is not None and  'twitter' in link:
#                     twitter = link    
#             website = li[0].get_attribute('href')
#             data = [[i, full_name,new_len,website,telegram,twitter]]
#             df = pd.DataFrame([i])
#             df.to_csv('deleted.csv',index=False,mode='a',header=False)
            
#             df  = pd.DataFrame(data)
#             df.to_csv('coinvote_info.csv',index=False,mode='a',header=False)
            
#         except:
#             print('Not Found')
 
#     driver.close()
            
# if __name__ == '__main__':

#     cpu = 3

#     x = (len(lis)//cpu)+1

#     li = []

#     for i in range(cpu*2):
#         s = i*x
#         e = s+x
#         li.append(lis[s:e])

#     print(li)

#     pool = mp.Pool(cpu)

#     pool.map(scrap,li)





