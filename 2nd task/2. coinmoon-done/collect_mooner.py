import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import multiprocessing as mp
import time


driver = webdriver.Firefox()
driver.maximize_window()


driver.get(f'https://coinmooner.com/')
time.sleep(30)
driver.find_element(By.XPATH,"//select[@class='MainView_tableResultsInput__E_k5O']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//select[@class='MainView_tableResultsInput__E_k5O']/option[4]").click()
time.sleep(2)
window_height = driver.execute_script("return window.innerHeight;")
driver.execute_script(f"window.scrollBy(0, {window_height*10.8});")
time.sleep(3)
for page in range(1,317):
    
    time.sleep(2)
    data = []
    
    # window_height = driver.execute_script("return window.innerHeight;")
    
    
    links = driver.find_elements(By.XPATH,'//a[@class="CoinList_overlayLink__9UJzg"]')
    
    for link in links:
        x = link.get_attribute('href')
        
        data.append(x)
        
    df = pd.DataFrame(data[6:])
    print(page, len(data))
    df.to_csv('collect_links.csv',index=False,mode='a',header=False)
    if page ==1 or page == 316:
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/main/section/div[3]/div/button[7]').click()
        time.sleep(5)
    elif page == 2 or page == 315:
        
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/main/section/div[3]/div/button[8]').click()
        time.sleep(5)
    elif page == 3 :
        
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/main/section/div[3]/div/button[9]').click()
        time.sleep(5)
    elif page == 4 or page+1 == 314:
        
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/main/section/div[3]/div/button[10]').click()
        time.sleep(5)
    elif page >= 5 or page <= 313:
        
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/main/section/div[3]/div/button[11]').click()
        time.sleep(5)
    window_height = driver.execute_script("return window.innerHeight;")
    driver.execute_script(f"window.scrollBy(0, {window_height*-2.8});")


df = pd.read_csv(f'deleted.csv')['Links'].values.tolist()
df2 = pd.read_csv(f'collect_links.csv')
df2 = df2.drop_duplicates()
df2.to_csv(f'links.csv',index=True)
print(len(df2))
# df3 = pd.read_csv(f'info.csv')['Project Info'].values.tolist()
# lis = df2['Links'].values.tolist()
# lis = [x for x in lis if (x not in df) and (x not in df3)]

# print(len(lis))

# def scrap(li):
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     for i in li:
#         try:
#             print(i,'\n\n\n')

#             driver.get(f'{i}')
#             time.sleep(2)
#             full_name = driver.find_element(By.XPATH,'//span[@class="CoinView_coinName__B7ix9"]').text
#             new_len = driver.find_element(By.XPATH,'//span[@class="CoinView_coinSymbol__fBB40"]').text
            
            
#             telegram = ''
#             twitter = ''
#             website   =   ''
#             li = driver.find_elements(By.XPATH,'//div[@class="CoinView_socialContainer__22JXS"]/a')
#             img = driver.find_elements(By.XPATH,'//div[@class="CoinView_socialContainer__22JXS"]/a/img')
#             cnt = 0
#             for a in li:

#                 link = a.get_attribute('href')
#                 title = img[cnt].get_attribute('alt').lower()
#                 cnt+=1
#                 print(link,title)
#                 if link is not None and title is not None and 'egram' in title:
#                     telegram = link
#                 if link is not None and title is not None and  'witter' in title:
#                     twitter = link    
#                 if link is not None and title is not None and  'bsite' in title:
#                     website = link    
#             data = [[i, full_name,new_len,website,telegram,twitter]]
#             df = pd.DataFrame([i])
#             df.to_csv('deleted.csv',index=False,mode='a',header=False)
            
#             df  = pd.DataFrame(data)
#             df.to_csv('info.csv',index=False,mode='a',header=False)
            
#         except:
#             print('Not Found')
 
#     driver.close()
            
# if __name__ == '__main__':

#     cpu = 4

#     x = (len(lis)//cpu)+1

#     li = []

#     for i in range(cpu):
#         s = i*x
#         e = s+x
#         li.append(lis[s:e])

#     print(li)

#     pool = mp.Pool(cpu)

#     pool.map(scrap,li)
