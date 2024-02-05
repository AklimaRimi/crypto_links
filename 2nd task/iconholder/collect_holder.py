import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import multiprocessing as mp
import time


driver = webdriver.Chrome()
driver.maximize_window()



df=  pd.read_csv('collect_links.csv')['Links'].values.tolist()

x = len(df)//16


for page in range(x+1,3855):
    driver.get(f'https://icoholder.com/en/icos/all?fbclid=IwAR3Rl3KXEIF7s6wWzSLKIZnFwtwpqgSAfL50DvAe5daaPMUqltVmTfjLlKw&isort=r.general&idirection=desc&page={page}')
    time.sleep(2)
    data = []
    
    window_height = driver.execute_script("return window.innerHeight;")
    driver.execute_script(f"window.scrollBy(0, {window_height*5});")
    
    links = driver.find_elements(By.XPATH,"//div[@class='ico-list-name-d']/h3/a")
    
    for link in links:
        x = link.get_attribute('href')
        
        data.append(x)
        
    print(page, len(data))
    df = pd.DataFrame(data)
    df.to_csv('collect_links.csv',index=False,mode='a',header=False)


