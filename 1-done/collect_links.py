
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings

warnings.filterwarnings('ignore')


driver = webdriver.Chrome()

driver.maximize_window()
df = pd.read_csv(f'coincheckup_links.csv')

x =  len(df)//100
print(x)
for page in range(x+1,299):
    time.sleep(1)
    link = f'https://coincheckup.com/?page={page}'
    lis = []
    driver.get(link)
    time.sleep(2)
    # driver.refresh()
    # time.sleep(5)
    window_height = driver.execute_script("return window.innerHeight;")

    driver.execute_script(f"window.scrollBy(0, {window_height*3.8});")
    time.sleep(1)
    li = driver.find_elements(By.XPATH,'//*[@id="rows-inner"]/div/home-col-name/a')
    
    print(page , len(li),'\n\n')
    
    for i in li:
        link = i.get_attribute('href')
        try:
            lis.append(link)
        except:
            print('error')
            
    
    df  = pd.DataFrame(lis)
    df = df.drop_duplicates()
    df.to_csv('coincheckup_links.csv',index=False,mode='a',header=False)

# df = pd.read_csv(f'coincheckup_links.csv') 
# df = df.drop_duplicates()
# lis = df['Links'].values.tolist()
# data = pd.read_csv('coincheckup_info.csv')['Project Info'].values.tolist()
# print(lis)
# for i in lis[len(data):]:
#     print(i,'\n\n\n')
#     time.sleep(1)
#     try: 
#         driver.get(i)  
#         time.sleep(2)
#         window_height = driver.execute_script("return window.innerHeight;")
#         driver.execute_script(f"window.scrollBy(0, {window_height*15});")
#         time.sleep(1) 
    
#         full_name = driver.find_element(By.XPATH,'//div[@class="coin-name ng-binding"]').text
#         social_media = driver.find_elements(By.XPATH,"//a[@class='ng-scope']")
#         telegram = ''
#         twitter = ''
#         website = driver.find_element(By.XPATH,'//div[@class="useful-links"]/a').get_attribute('href')
#         for s in social_media:
#             link = s.get_attribute('href')
#             if 't.me' in link:
#                 telegram = link
#             if 'twitter' in link:
#                 twitter = link
        
#         new_len = len(full_name.split(' ')[-1])
#         data = [[i,full_name[:-new_len],full_name.split(' ')[-1],website,telegram,twitter]]
#     except:
#         print('error')
    
#     df  = pd.DataFrame(data)
#     df.to_csv('coincheckup_info.csv',index=False,mode='a',header=False)

    
    



driver.close()