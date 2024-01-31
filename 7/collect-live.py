import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings
from selenium.webdriver.common.action_chains import ActionChains
import multiprocessing as mp


warnings.filterwarnings('ignore')


driver = webdriver.Chrome()
driver.maximize_window()
# df = pd.read_csv(f'live_link.csv')


# link = f'https://www.livecoinwatch.com/'
# driver.get(link)
# for page in range(658):
#     try:
#         lis = []
        
#         time.sleep(3)
#         # window_height = driver.execute_script("return window.innerHeight;")
#         # driver.execute_script(f"window.scrollBy(0, {window_height*7});")
#         # time.sleep(1)

#         li = driver.find_elements(By.XPATH,"//a[@class='text-left']")

#         for i in li:
#             lis.append(i.get_attribute('href'))
#         df  = pd.DataFrame(lis)
#         df.to_csv('live_link.csv',index=False,mode='a',header=False)
#     except:
#         print('Error')
    
#     driver.find_element(By.XPATH,"//li[@class='page-item next']/a").click()
    
# df = pd.read_csv(f'live_link.csv') 
# df = df.drop_duplicates()
# lis = df['Links'].values.tolist()
# data = pd.read_csv('live_info.csv')['Project Info'].values.tolist()

# print(len(data))



df = pd.read_csv(f'deleted.csv')['Links'].values.tolist()
df2 = pd.read_csv(f'live_link.csv')
df2 = df2.drop_duplicates()
lis = df2['Links'].values.tolist()
lis = [x for x in lis if x not in df]
for i in lis:
    try:
        print(i,'\n\n\n')
        driver.get(i)  
        time.sleep(2)
        # window_height = driver.execute_script("return window.innerHeight;")
        # driver.execute_script(f"window.scrollBy(0, {window_height*3});")
        # time.sleep(1) 

        full_name = driver.find_element(By.XPATH,"//div[@class='price-container']").text.split('\n')[0]
        symb = driver.find_element(By.XPATH,"//div[@class='price-container']").text.split('\n')[-1]
        social_media = driver.find_elements(By.XPATH,'//ul[@class="list-inline data-icons-list p-0 m-0"]/li/a')
        telegram = ''
        twitter = ''
        try:
            website =social_media[0].get_attribute('href')
        except:
            website = ''
        try:
            for s in social_media:
                link = s.get_attribute('href')
                if 't.me' in link:
                    telegram = link
                if 'twitter' in link:
                    twitter = link
        except:
            print('error')
        
        # new_len = len(full_name.split(' ')[-1])
        # print(i,full_name[:-new_len],full_name.split(' ')[-1],website,telegram,twitter)
        data = [[i,full_name,symb,website,telegram,twitter]]
        df = pd.DataFrame([i])
        df.to_csv('deleted.csv',index=False,mode='a',header=False)


        df  = pd.DataFrame(data)
        df.to_csv('live_info.csv',index=False,mode='a',header=False)
    except:
        print('error')


