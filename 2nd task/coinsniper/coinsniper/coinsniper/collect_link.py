import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import multiprocessing as mp



import os




df = pd.read_csv(f'deleted.csv')['Links'].values.tolist()
df2 = pd.read_csv(f'links.csv')
df2 = df2.drop_duplicates()
df3 = pd.read_csv(f'info.csv')['Project Info'].values.tolist()
lis = df2['Links'].values.tolist()
lis = [x for x in lis if (x not in df) and (x not in df3)]

# print(len(lis))

def scrap(li):
    driver = webdriver.Firefox()
    driver.maximize_window()
    for i in li:
        try:
            print(i,'\n\n\n')

            driver.get(f'{i}')
            time.sleep(3)
            full_name = driver.find_element(By.XPATH,'//div[@class="coin-name"]/h1').text
            new_len = driver.find_element(By.XPATH,'//div[@class="coin-name"]/span').text
            # full_name = full_name[:-len(new_len)]
            
            # social_media = driver.find_elements(By.XPATH,'//div[@class="social-icon"]/a')
            
            telegram = ''
            twitter = ''
            website = ''
            li = driver.find_elements(By.XPATH,'//div[@class="social-icon"]/a')
            for a in li:
                link = a.get_attribute('href')
                # print(link)
                if link is not None and 't.me' in link:
                    telegram = link
                if link is not None and  'twitter' in link:
                    twitter = link    
                if link is not None and 'website' in link:
                    
                    website = link
            data = [[i, full_name,new_len,website,telegram,twitter]]
            df = pd.DataFrame([i])
            df.to_csv('deleted.csv',index=False,mode='a',header=False)
            
            df  = pd.DataFrame(data)
            df.to_csv('info.csv',index=False,mode='a',header=False)
            
        except:
            print('Not Found')
 
    driver.close()
            
if __name__ == '__main__':

    cpu = 10

    x = (len(lis)//cpu)

    li = []

    for i in range(cpu):
        s = i*x
        e = s+x
        li.append(lis[s:e])

    # print(li)

    pool = mp.Pool(cpu)

    pool.map(scrap,li)
    
# scrap(lis)





