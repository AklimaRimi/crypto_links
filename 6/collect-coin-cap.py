import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings

warnings.filterwarnings('ignore')


driver = webdriver.Chrome()

df = pd.read_csv(f'coinvote_links.csv')

x =  len(df)//100
print(x)

driver.maximize_window()
for page in range(x,1030):
    try:
        lis = []
        link = f'https://coinvote.cc/today&page={page}'
        print(page)
        driver.get(link)
        time.sleep(2)
        # window_height = driver.execute_script("return window.innerHeight;")
        # driver.execute_script(f"window.scrollBy(0, {window_height*5});")
        # time.sleep(1)

        li = driver.find_elements(By.XPATH,"//div[@class='coin-column redirect-coin']/a")

        for i in li:
            lis.append(i.get_attribute('href'))
        df  = pd.DataFrame(lis)
        df.to_csv('coinvote_links.csv',index=False,mode='a',header=False)
    except:
        continue


df = pd.read_csv(f'coinvote_links.csv') 
df = df.drop_duplicates()
lis = df['Links'].values.tolist()
data = pd.read_csv('coinvote_info.csv')['Project Info'].values.tolist()

print(len(data))
