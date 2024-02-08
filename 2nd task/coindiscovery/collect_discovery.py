import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import multiprocessing as mp
import time



df = pd.read_csv(f'deleted.csv')['Links'].values.tolist()
df2 = pd.read_csv(f'link.csv')
df2 = df2.drop_duplicates()
# df2.to_csv(f'collect_links.csv',columns=['Links'],index=False)
df3 = pd.read_csv(f'info.csv')['Project Info'].values.tolist()
lis = df2['Links'].values.tolist()
lis = [x for x in lis if (x not in df) and (x not in df3)]

print(len(lis))

def scrap(li):
    driver = webdriver.Chrome()
    driver.maximize_window()
    for i in li:
        # try:
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
                    if btn == '#':
                        driver.find_element(By.XPATH,'//div[@class="community-dropdown show"]').click()
                    li = driver.find_elements(By.XPATH,"//div[@class='custom-menu dropdown-menu show']/a")
                    for a in li:
                        link = a.get_attribute('href')
                        # title = a.get_attribute('data-original-title')
                        print(link)
                        if link is not None and 't.me' in link:
                            telegram = link
                        if link is not None and 'twitter' in link:
                            twitter = link    
                    website = driver.find_element(By.XPATH,"//div[@class='chain-action d-flex']/a").get_attribute('href')
                except:
                    link = driver.find_element(By.XPATH,"//div[@class='community-dropdown']/a").get_attribute('href')
                    if link is not None and 't.me' in link:
                            telegram = link
                    if link is not None and 'twitter' in link:
                        twitter = link 
            except:
                print('community nai')
            
            try:
                try:
                    btn = driver.find_element(By.XPATH,'//div[@class="chat-dropdown"]/a').get_attribute('href')
                    if btn == '#':
                        driver.find_element(By.XPATH,'//div[@class="chat-dropdown"]').click()
                    li = driver.find_elements(By.XPATH,"//div[@class='custom-menu dropdown-menu']/a")
                    for a in li:
                        link = a.get_attribute('href')
                        # title = a.get_attribute('data-original-title')
                        print(link)
                        if link is not None and 't.me' in link:
                            telegram = link
                        if link is not None and 'twitter' in link:
                            twitter = link    
                    website = driver.find_element(By.XPATH,"//div[@class='chain-action d-flex']/a").get_attribute('href')
                except:
                    link = driver.find_element(By.XPATH,"//div[@class='chat-dropdown']/a").get_attribute('href')
                    if link is not None and 't.me' in link:
                            telegram = link
                    if link is not None and 'twitter' in link:
                        twitter = link 
            except:
                print('Chat nai')
                
            data = [[i, full_name,new_len,website,telegram,twitter]]
            df = pd.DataFrame([i])
            df.to_csv('deleted.csv',index=False,mode='a',header=False)
            
            df  = pd.DataFrame(data)
            df.to_csv('info.csv',index=False,mode='a',header=False)
            
        # except:
            # print('Not Found')
 
    driver.close()
            
if __name__ == '__main__':

    cpu = 1

    x = (len(lis)//cpu)

    li = []

    for i in range(cpu):
        s = i*x
        e = s+x
        li.append(lis[s:e])

    print(li)

    pool = mp.Pool(cpu)

    pool.map(scrap,li)
