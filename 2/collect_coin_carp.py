
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
for page in range(1,278):
    link = f'https://www.coincarp.com/pn_{page}.html'

    driver.get(link)
    time.sleep(1)
    window_height = driver.execute_script("return window.innerHeight;")
    driver.execute_script(f"window.scrollBy(0, {window_height*11});")
    time.sleep(1)

    li = driver.find_elements(By.XPATH,"//div[@class='flex']/a")

    for i in li[1:]:
        lis.append(i.get_attribute('href'))



df  = pd.DataFrame(lis,columns = ['Links'])
df.to_csv('2/coincarp_links.csv',index=False)

data = []
for i in lis:
    print(i,'\n\n\n')
    
    driver.get(i)
    time.sleep(1)
    full_name = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/h2').text
    new_len = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/h2/small').text
    
    # social_media = driver.find_elements(By.XPATH,"//a[@class='ng-scope']")
     
    telegram = ''
    twitter = ''
    li = driver.find_elements(By.XPATH,"//div[@class='info-top d-flex align-items-center']/a")
    for a in li:
        link = a.get_attribute('href')
        if 't.me' in link:
            telegram = link
        if 'twitter' in link:
            twitter = link    
    website = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/ul/li[1]/a').get_attribute('href')
    data.append([i,str(full_name[:-(len(new_len)+1)]),new_len,website,telegram,twitter])
    
df  = pd.DataFrame(data,columns = ['Project Info','Full Name','Ticker','Website','Telegram','Twitter'])
df.to_csv('2/coincarp_info.csv',index=False)

    
    



driver.close()