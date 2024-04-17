
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings

warnings.filterwarnings('ignore')


driver = webdriver.Firefox()

# df = pd.read_csv(f'coinrank_links.csv')

# x =  len(df)//50
# print(x)

driver.maximize_window()
# for page in range(x-5,684):
#     try:
#         lis = []
#         link = f'https://coinranking.com/?page={page}'
#         print(page)
#         driver.get(link)
#         time.sleep(3)
#         window_height = driver.execute_script("return window.innerHeight;")
#         driver.execute_script(f"window.scrollBy(0, {window_height*5});")
#         time.sleep(1)

#         li = driver.find_elements(By.XPATH,"//a[@class='profile__link']")

#         for i in li[:51]:
#             lis.append(i.get_attribute('href'))
#         df  = pd.DataFrame(lis)
#         df.to_csv('coinrank_links.csv',index=False,mode='a',header=False)
#     except:
#         continue

# print(lis)

df = pd.read_csv(f'coinrank_links.csv') 
df = df.drop_duplicates()
lis = df['Links'].values.tolist()
data = pd.read_csv('coinrank_info.csv')['Project Info'].values.tolist()

print(len(lis))


for i in lis:
    time.sleep(5)
    print(i,'\n\n\n')
    try:
        driver.get(f'{i}')
        time.sleep(1)
        full_name = driver.find_element(By.XPATH,"//h1[@class='hero-coin__name']/a").text
        new_len = driver.find_element(By.XPATH,"//div[@class='hero-coin__symbol']/a").text
        
        # social_media = driver.find_elements(By.XPATH,"//a[@class='ng-scope']")
        
        telegram = ''
        twitter = ''
        li = driver.find_elements(By.XPATH,"//a[@class='link-list__link']")
        for a in li:
            link = a.get_attribute('href')
            if 't.me' in link:
                telegram = link
            if 'twitter' in link:
                twitter = link    
        website = driver.find_element(By.XPATH,'//*[@id="description"]/div[2]/table/tbody/tr[1]/td/a').get_attribute('href')
        data = [[i, full_name,new_len,website,telegram,twitter]]
        
        df  = pd.DataFrame(data)
        df.to_csv('coinrank_info.csv',index=False,mode='a',header=False)
    except:
        print('Error')

