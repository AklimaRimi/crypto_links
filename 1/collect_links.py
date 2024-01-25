
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
for page in range(1,299):
    link = f'https://coincheckup.com/?page={page}'

    driver.get(link)
    time.sleep(1)
    window_height = driver.execute_script("return window.innerHeight;")
    driver.execute_script(f"window.scrollBy(0, {window_height*11});")
    time.sleep(2)

    li = driver.find_elements(By.XPATH,"//a[@class='coin-name']")

    for i in li:
        lis.append(i.get_attribute('href'))



df  = pd.DataFrame(lis,columns = ['Links'])
df.to_csv('1/coincheckup_links.csv',index=False)

data = []
for i in lis:
    print(i,'\n\n\n')
    
    driver.get(i)
    try:   
        time.sleep(2)
        window_height = driver.execute_script("return window.innerHeight;")
        driver.execute_script(f"window.scrollBy(0, {window_height*15});")
        time.sleep(1) 
    
        full_name = driver.find_element(By.XPATH,'//div[@class="coin-name ng-binding"]').text
        social_media = driver.find_elements(By.XPATH,"//a[@class='ng-scope']")
        telegram = ''
        twitter = ''
        website = driver.find_element(By.XPATH,'//div[@class="useful-links"]/a').get_attribute('href')
        for s in social_media:
            link = s.get_attribute('href')
            if 't.me' in link:
                telegram = link
            if 'twitter' in link:
                twitter = link
        
        new_len = len(full_name.split(' ')[-1])
        data.append([i,full_name[:-new_len],full_name.split(' ')[-1],website,telegram,twitter])
    except:
        time.sleep(10)    
        driver.execute_script(f"window.scrollBy(0, {window_height*25});")
        full_name = driver.find_element(By.XPATH,'//div[@class="coin-name ng-binding"]').text
        social_media = driver.find_elements(By.XPATH,"//a[@class='ng-scope']")
        telegram = ''
        twitter = ''
        website = driver.find_element(By.XPATH,'//div[@class="useful-links"]/a').get_attribute('href')
        for s in social_media:
            link = s.get_attribute('href')
            if 't.me' in link:
                telegram = link
            if 'twitter' in link:
                twitter = link
        
        new_len = len(full_name.split(' ')[-1])
        data.append([i,full_name[:-new_len],full_name.split(' ')[-1],website,telegram,twitter])
    
df  = pd.DataFrame(data,columns = ['Project Info','Full Name','Ticker','Website','Telegram','Twitter'])
df.to_csv('1/coincheckup_info.csv',index=False)

    
    



driver.close()