import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings

warnings.filterwarnings('ignore')


driver = webdriver.Chrome()

df = pd.read_csv(f'coin_cap_link.csv')

x =  len(df)//100
print(x)

driver.maximize_window()
for page in range(x,90):
    try:
        lis = []
        link = f'https://coinmarketcap.com/?page={page}'
        print(page)
        driver.get(link)
        time.sleep(3)
        window_height = driver.execute_script("return window.innerHeight;")
        for x in range(1,14):
            driver.execute_script(f"window.scrollBy(0, {window_height+(x)});")
            time.sleep(1)

            li = driver.find_elements(By.XPATH,"//div[@class='sc-aef7b723-0 LCOyB']/a")

            for i in li:
                lis.append(i.get_attribute('href'))
        df  = pd.DataFrame(lis)
        df = df.drop_duplicates()
        print(len(df))
        df.to_csv('coin_cap_link.csv',index=False,mode='a',header=False)
    except:
        print('error')


# df = pd.read_csv(f'coinvote_links.csv') 
# df = df.drop_duplicates()
# lis = df['Links'].values.tolist()
# data = pd.read_csv('coinvote_info.csv')['Project Info'].values.tolist()

# print(len(data))
