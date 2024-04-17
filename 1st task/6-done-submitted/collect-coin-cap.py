import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings
import multiprocessing as mp

warnings.filterwarnings('ignore')


driver = webdriver.Chrome()

# df = pd.read_csv(f'coin_cap_link.csv')

# x =  len(df)//100
# print(x)

# driver.maximize_window()
# for page in [29,48]:
#     try:
#         lis = []
#         link = f'https://coinmarketcap.com/?page={page}'
#         print(page)
#         driver.get(link)
#         time.sleep(3)
#         window_height = driver.execute_script("return window.innerHeight;")
#         for x in range(1,14):
#             driver.execute_script(f"window.scrollBy(0, {window_height+(x)});")
#             time.sleep(1)

#             li = driver.find_elements(By.XPATH,"//div[@class='sc-aef7b723-0 LCOyB']/a")

#             for i in li:
#                 lis.append(i.get_attribute('href'))
#         df  = pd.DataFrame(lis)
#         df = df.drop_duplicates()
#         print(len(df))
#         df.to_csv('coin_cap_link.csv',index=False,mode='a',header=False)
#     except:
#         print('error')


df = pd.read_csv(f'deleted.csv')['Links'].values.tolist()
df2 = pd.read_csv(f'coin_cap_link.csv')
df2 = df2.drop_duplicates()
df2.to_csv('coin_cap_link.csv')
df3 = pd.read_csv(f'coin_cap_info.csv')['Project Info'].values.tolist()
lis = df2['Links'].values.tolist()
lis = [x for x in lis if (x not in df)]


def scrap(li):
    for i in li:
        i = i.replace('\t','')
        print(i,'\n\n\n')
        try:
            time.sleep(1)
            driver.get(f'{i}')
            time.sleep(3)
            full_name = driver.find_element(By.XPATH,"//h1[@class='sc-f70bb44c-0 gYiXVQ']").text
            new_len = driver.find_element(By.XPATH,"//div[@class='sc-f70bb44c-0 fdOBt coin-symbol-wrapper']").text.split()[-1]
            full_name = full_name[:-len(new_len)-1]
            
            # social_media = driver.find_elements(By.XPATH,"//a[@class='ng-scope']")
            
            telegram = ''
            twitter = ''
            li = driver.find_elements(By.XPATH,"//div[@class='sc-f70bb44c-0 sc-c3d90b62-0 fSMMKk']/a")
            for a in li:
                link = a.get_attribute('href')
                # print(link)
                if link is not None and 't.me' in link:
                    telegram = link
                if link is not None and  'twitter' in link:
                    twitter = link    
            try:
                website = driver.find_element(By.XPATH,"//div[@class='sc-f70bb44c-0 sc-c3d90b62-0 fSMMKk']/a").get_attribute('href')
            except:
                website = ''
            data = [[i, full_name,new_len,website,telegram,twitter]]
            df = pd.DataFrame([i])
            df.to_csv('deleted.csv',index=False,mode='a',header=False)
            
            df  = pd.DataFrame(data)
            df.to_csv('coin_cap_info.csv',index=False,mode='a',header=False)
        except:
            print('Error')
            

if __name__ == '__main__':

    cpu = 3

    x = (len(lis)//cpu)+1

    li = []

    for i in range(cpu):
        s = i*x
        e = s+x
        li.append(lis[s:e])

    print(len(li))

    pool = mp.Pool(cpu)

    pool.map(scrap,li)



    driver.close()

