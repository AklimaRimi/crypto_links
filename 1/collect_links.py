
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings

warnings.filterwarnings('ignore')

lis = []
driver = webdriver.Edge()

driver.maximize_window()
df = pd.read_csv(f'Product_information.csv')

x =  len(df)//100
print(x)
for page in range(x+1,299):
    link = f'https://coincheckup.com/?page={page}'

    driver.get(link)
    time.sleep(2)
    window_height = driver.execute_script("return window.innerHeight;")
    driver.execute_script(f"window.scrollBy(0, {window_height*10.2});")
    time.sleep(2)

    li = driver.find_elements(By.XPATH,"//a[@class='coin-name']")
    print(len(li))

    for i in li:
        lis.append(i.get_attribute('href'))
    df  = pd.DataFrame(lis)
    df.to_csv('Product_information.csv',index=False,mode='a',header=False)

df = pd.read_csv(f'Product_information.csv') 
df = df.drop_duplicates()
lis = df['Links'].values.tolist()
data = pd.read_csv('coincheckup_info.csv')['Project Info'].values.tolist()
print(lis)
for i in lis[len(data)-1:]:
    print(i,'\n\n\n')
    data = []
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
    
    df  = pd.DataFrame(data)
    df.to_csv('coincheckup_info.csv',index=False,mode='a',header=False)

    
    



driver.close()