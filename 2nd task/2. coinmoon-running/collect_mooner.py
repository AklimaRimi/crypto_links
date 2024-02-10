import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import multiprocessing as mp
import time


driver = webdriver.Firefox()
driver.maximize_window()

df=  pd.read_csv('collect_links.csv')['Links'].values.tolist()

x = len(df)//16
driver.get(f'https://coinmooner.com/')
time.sleep(200)
driver.find_element(By.XPATH,"//select[@class='MainView_tableResultsInput__E_k5O']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//select[@class='MainView_tableResultsInput__E_k5O']/option[4]").click()
time.sleep(2)
window_height = driver.execute_script("return window.innerHeight;")
driver.execute_script(f"window.scrollBy(0, {window_height*15});")
time.sleep(3)
for page in range(x,317):
    
    time.sleep(2)
    data = []
    
    # window_height = driver.execute_script("return window.innerHeight;")
    # driver.execute_script(f"window.scrollBy(0, {window_height*5});")
    
    links = driver.find_elements(By.XPATH,'//a[@class="CoinList_overlayLink__9UJzg"]')
    
    for link in links:
        x = link.get_attribute('href')
        
        data.append(x)
        
    print(page, len(data))
    df = pd.DataFrame(data)
    df.to_csv('collect_links.csv',index=False,mode='a',header=False)
    
    driver.find_element(By.XPATH,'//button[@class="MainView_numberedPagesBtn__hJxuN"][8]').click()



# df = pd.read_csv(f'deleted.csv')['Links'].values.tolist()
# df2 = pd.read_csv(f'links.csv')
# df2 = df2.drop_duplicates()
# df2.to_csv(f'links.csv',index=False)
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
