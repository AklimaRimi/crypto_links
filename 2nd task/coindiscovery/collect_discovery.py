import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import multiprocessing as mp
import time


driver = webdriver.Chrome()
driver.maximize_window()



df=  pd.read_csv('links.csv')['Links'].values.tolist()

x = len(df)//20

for page in range(x+1,1238):
    time.sleep(1)
    data = []
    driver.get(f'https://www.coinscope.co/alltime?page={page}')

    window_height = driver.execute_script("return window.innerHeight;")
    for i in range(5):
        driver.execute_script(f"window.scrollBy(0, {window_height+(i*0.5)});")
        
        links = driver.find_elements(By.XPATH,"//div[@class='StyledBox-sc-13pk1d4-0 gVQHjs']/a")
        try:
            for link in links:
                x = link.get_attribute('href')
                data.append(x)
        except:
            print('\n')
        
    
    df = pd.DataFrame(data)
    df = df.drop_duplicates()
    print(page, len(data))
    df.to_csv('links.csv',index=False,mode='a',header=False)
    
    next = driver.find_elements(By.XPATH,"//button[@class='StyledButtonKind-sc-1vhfpnt-0 cMaZpI StyledPageControl__StyledPaginationButton-sc-1vlfaez-0 kPuPyK']")
    if len(next) > 1:
        next[-1].click()
        
    time.sleep(1)


