import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings
from selenium.webdriver.common.action_chains import ActionChains


warnings.filterwarnings('ignore')


driver = webdriver.Chrome()

df = pd.read_csv(f'live_link.csv')

driver.maximize_window()
link = f'https://www.livecoinwatch.com/'
driver.get(link)
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/main/div[2]/div/div[5]/div/button').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/main/div[2]/div/div[5]/div/div/div/button[4]').click()
time.sleep(1)
for page in range(165):
    try:
        lis = []
        
        time.sleep(2)
        # window_height = driver.execute_script("return window.innerHeight;")
        # driver.execute_script(f"window.scrollBy(0, {window_height*7});")
        # time.sleep(1)

        li = driver.find_elements(By.XPATH,"//a[@class='text-left']")

        for i in li:
            lis.append(i.get_attribute('href'))
        df  = pd.DataFrame(lis)
        df.to_csv('live_link.csv',index=False,mode='a',header=False)
    except:
        print('Erroe')
    
    driver.find_element(By.XPATH,"//li[@class='page-item next']/a").click()
    
df = pd.read_csv(f'live_link.csv') 
df = df.drop_duplicates()
lis = df['Links'].values.tolist()
data = pd.read_csv('live_info.csv')['Project Info'].values.tolist()

print(len(data))
