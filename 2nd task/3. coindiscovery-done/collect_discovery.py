import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import multiprocessing as mp
import time
# //select[@class='custom-select custom-select-sm form-control form-control-sm']

# driver = webdriver.Edge()
# driver.maximize_window()



# df=  pd.read_csv('collect_links.csv')['Links'].values.tolist()

# x = len(df)//16

# driver.get(f'https://coindiscovery.app/')
# time.sleep(2)
# driver.find_element(By.XPATH,"//select[@class='custom-select custom-select-sm form-control form-control-sm']").click()
# driver.find_element(By.XPATH,'//*[@id="common-grid_length"]/label/select/option[4]').click()
# time.sleep(5)
# for page in range(700):
    
#     time.sleep(5)
#     data = []
    
#     # window_height = driver.execute_script("return window.innerHeight;")
#     # driver.execute_script(f"window.scrollBy(0, {window_height*5});")

#     try:
#         links = driver.find_elements(By.XPATH,"//table[@class='table table-hover token-grid dataTable no-footer dtfc-has-left']/tbody/tr/td[3]/a")
    
    
#         for link in links:
#             x = link.get_attribute('href')
#             data.append(x)
#         print(page, len(data))
#         df = pd.DataFrame(data)
#         df.to_csv('links.csv',index=False,mode='a',header=False)
#         next = driver.find_element(By.XPATH,'//*[@id="common-grid_wrapper"]/div[3]/div[2]/div/ul/li[9]').click()
#     except:
#         print('Error')




df = pd.read_csv(f'deleted.csv')['Links'].values.tolist()
df2 = pd.read_csv(f'links.csv')
df2 = df2.drop_duplicates()
# df2.to_csv(f'collect_links.csv',columns=['Links'],index=False)
df3 = pd.read_csv(f'info.csv')['Project Info'].values.tolist()
lis = df2['Links'].values.tolist()
lis = [x for x in lis if (x not in df) and (x not in df3)]
# lis = ['https://coindiscovery.app/coin/carey-token/overview']
# print(len(lis))

def scrap(li):
    print(len(li))
    driver = webdriver.Firefox()
    driver.maximize_window()
    for i in li:
        try:
            print(i,'\n\n\n')

            driver.get(f'{i}')
            time.sleep(2)
            full_name = driver.find_element(By.XPATH,"//div[@class='coin-title']/strong").text
            new_len = driver.find_element(By.XPATH,"//div[@class='coin-sub-title bg-badge radius-common']").text
            # full_name = full_name[:-len(new_len)]
            
            # social_media = driver.find_elements(By.XPATH,"//a[@class='ng-scope']")
            
            telegram = ''
            twitter = ''          
 
            try:
                try:
                    btn = driver.find_element(By.XPATH,'//div[@class="community-dropdown show"]/a').get_attribute('href')
                    
                    if '#' in btn:
                        print('aise')
                        driver.find_element(By.XPATH,'//div[@class="community-dropdown show"]').click()
                        li = driver.find_elements(By.XPATH,"//div[@class='custom-menu dropdown-menu show']/a")
                        for a in li:
                            link = a.get_attribute('href')
                            # title = a.get_attribute('data-original-title')
                            # print(link)
                            if link is not None and 't.me' in link:
                                telegram = link
                            if link is not None and 'twitter' in link:
                                twitter = link    
                except:
                        link = driver.find_element(By.XPATH,"//div[@class='community-dropdown']/a").get_attribute('href')
                        if link is not None and 't.me' in link:
                                telegram = link
                        if link is not None and 'twitter' in link:
                            twitter = link 
            except:
                print('community nai')
            
            try:
                    
                    btn = driver.find_element(By.XPATH,'//div[@class="chat-dropdown"]/a').get_attribute('href')
                    print(btn)
                    if '#' in btn:
                        driver.find_element(By.XPATH,'//div[@class="chat-dropdown"]').click()
                        li = driver.find_elements(By.XPATH,"//div[@class='custom-menu dropdown-menu show']/a")
                        for a in li:
                            link = a.get_attribute('href')
                            # title = a.get_attribute('data-original-title')
                            print(link)
                            if link is not None and 't.me' in link:
                                telegram = link
                            if link is not None and 'twitter' in link:
                                twitter = link    
                                
                    else:
                        link = driver.find_element(By.XPATH,"//div[@class='chat-dropdown']/a").get_attribute('href')
                        if link is not None and 't.me' in link:
                                telegram = link
                        if link is not None and 'twitter' in link:
                                twitter = link 

            except:
                print('Chat nai')
                
            website = driver.find_element(By.XPATH,"//div[@class='chain-action d-flex']/a").get_attribute('href')

            data = [[i, full_name,new_len,website,telegram,twitter]]
            df = pd.DataFrame([i])
            df.to_csv('deleted.csv',index=False,mode='a',header=False)
            
            df  = pd.DataFrame(data)
            df.to_csv('info.csv',index=False,mode='a',header=False)
            
        except:
            print('Not Found')
 
    driver.close()
            
if __name__ == '__main__':

    cpu = 5

    x = (len(lis)//cpu)+1

    li = []

    for i in range(cpu):
        s = i*x
        e = s+x
        li.append(lis[s:e])

    pool = mp.Pool(cpu)

    pool.map(scrap,li)
