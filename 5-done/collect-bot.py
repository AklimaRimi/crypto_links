import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings

warnings.filterwarnings('ignore')


driver = webdriver.Chrome()

df = pd.read_csv(f'coinbot_links.csv')

x =  len(df)//100
print(x)

driver.maximize_window()

try:
    lis = []
    link = f'https://coinarbitragebot.com/'
    driver.get(link)
    time.sleep(1)
    # window_height = driver.execute_script("return window.innerHeight;")
    # driver.execute_script(f"window.scrollBy(0, {window_height*5});")
    # time.sleep(1)

    li = driver.find_elements(By.XPATH,"//td[@class='text-left indx1']/a")

    for i in li:
        lis.append(i.get_attribute('href'))
    df  = pd.DataFrame(lis)
    df.to_csv('coinbot_links.csv',index=False,mode='a',header=False)
except:
    print('Error')


df = pd.read_csv(f'coinbot_links.csv') 
df = df.drop_duplicates()
lis = df['Links'].values.tolist()
data = pd.read_csv('coinbot_info.csv')['Project Info'].values.tolist()

print(len(data))


for i in lis[len(data):]:
    print(i,'\n\n\n')
    driver.get(f'{i}')
    time.sleep(1)
    full_name = driver.find_element(By.XPATH,'//*[@id="shead"]/div/div[1]/div[1]/h1').text.split('(')[0]
    new_len = driver.find_element(By.XPATH,'//*[@id="shead"]/div/div[1]/div[1]/h1').text.split('(')[-1][:-1]
    # full_name = full_name[:-len(new_len)]
    
    # social_media = driver.find_elements(By.XPATH,"//a[@class='ng-scope']")
    
    
    time.sleep(2)
    try:
        click = driver.find_element(By.XPATH,'//*[@id="dropdown06"]').click()
    except:
        print('No button')
    time.sleep(2)
    
    telegram = ''
    twitter = ''
    li = driver.find_elements(By.XPATH,'//*[@id="shead"]/div/div[1]/div[3]/div[2]/table/tbody/tr[3]/td[5]/div/div/a')
    for a in li:
        link = a.get_attribute('href')
        print(link)
        if link is not None and 't.me' in link:
            telegram = link
        if link is not None and  'twitter' in link:
            twitter = link    
    li =  driver.find_elements(By.XPATH,"//td[contains(@class,'tbltd1 tbltd3 pt-3')]/a")
    for a in li:
        link = a.get_attribute('href')
        print(link)
        if link is not None and 't.me' in link:
            telegram = link
        if link is not None and  'twitter' in link:
            twitter = link 
    try:
        website = driver.find_element(By.XPATH,'//*[@id="shead"]/div/div[1]/div[3]/div[2]/table/tbody/tr[3]/td[1]/a').get_attribute('href')
    except:
        website = ''
    data = [[i, full_name,new_len,website,telegram,twitter]]
    
    df  = pd.DataFrame(data)
    df.to_csv('coinbot_info.csv',index=False,mode='a',header=False)
driver.close()