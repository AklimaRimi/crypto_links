
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings

warnings.filterwarnings('ignore')

lis = []
driver = webdriver.Chrome()

driver.maximize_window()
for page in range(1,645):
    link = f'https://coinranking.com/?page={page}'

    driver.get(link)
    time.sleep(1)
    window_height = driver.execute_script("return window.innerHeight;")
    driver.execute_script(f"window.scrollBy(0, {window_height*11});")
    time.sleep(1)

    li = driver.find_elements(By.XPATH,"//a[@class='profile__link']")

    for i in li[:51]:
        lis.append(i.get_attribute('href'))

# print(lis)

df  = pd.DataFrame(lis,columns = ['Links'])
df.to_csv('coinrank_links.csv',index=False)

data = []
for i in lis:
    print(i,'\n\n\n')
    
    driver.get(i)
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
    data.append([i, full_name,new_len,website,telegram,twitter])
    
df  = pd.DataFrame(data,columns = ['Project Info','Full Name','Ticker','Website','Telegram','Twitter'])
df.to_csv('coinrank_info.csv',index=False)

    
    



driver.close()