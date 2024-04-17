import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import multiprocessing as mp
import time


# driver = webdriver.Chrome()
# driver.maximize_window()

# df=  pd.read_csv('collect_links.csv')['Links'].values.tolist()

# x = len(df)//30
# # window_height = driver.execute_script("return window.innerHeight;")
# # driver.execute_script(f"window.scrollBy(0, {window_height*10.8});")
# for page in range(730,741):
    
    
#     data = []
#     time.sleep(2)
#     driver.get(f'https://alphagrowth.io/projects?page={page}')
#     # window_height = driver.execute_script("return window.innerHeight;")
#     # time.sleep(2)
    
#     links = driver.find_elements(By.XPATH,'//tbody/tr/td[2]/a[1]')
    
#     for link in links:
#         x = link.get_attribute('href')
        
#         data.append(x)
        
#     df = pd.DataFrame(data)
#     print(page, len(data))
#     df.to_csv('collect_links.csv',index=False,mode='a',header=False)
   

# driver.close()

df = pd.read_csv(f'deleted.csv')['Links'].values.tolist()
df2 = pd.read_csv(f'collect_links.csv')
df2 = df2.drop_duplicates()
df2.to_csv(f'links.csv',index=True)
# print(len(df2))
df3 = pd.read_csv(f'info.csv')['Project Info'].values.tolist()
lis = df2['Links'].values.tolist()
lis = [x for x in lis if (x not in df) and (x not in df3)]

# print(len(lis))

def scrap(li):
    driver = webdriver.Chrome()
    driver.maximize_window()
    for i in li:
        try:
            print(i,'\n\n\n')

            driver.get(f'{i}')
            time.sleep(2)
            full_name = driver.find_element(By.XPATH,"//h2[@class='text-2xl text-white']").text
            new_len = driver.find_element(By.XPATH,'//h1[@class="text-4xl md:text-6xl font-semibold text-primary leading-none"]').text
            if '(' in new_len:
                s = new_len.find('(')
                e = new_len.find(')')
                new_len = new_len[s+1: e]
            else:
                new_len = ''
            
            telegram = ''
            twitter = ''
            website   =   ''
            li = driver.find_elements(By.XPATH,"//div[@class='flex gap-2']/a")
            for a in li:

                link = a.get_attribute('href')
                title = a.get_attribute('title')
                # cnt+=1
                # print(link,title)
                if 'Telegram' in title: 
                    telegram = link
                if 'Twitter' in title:
                    twitter = link    
                if 'Website' in title:
                    website = link    
            data = [[i, full_name,new_len,website,telegram,twitter]]
            df = pd.DataFrame([i])
            df.to_csv('deleted.csv',index=False,mode='a',header=False)
            
            df  = pd.DataFrame(data)
            df.to_csv('info.csv',index=False,mode='a',header=False)
            
        except:
            print('Not Found')
 
    driver.close()
            
if __name__ == '__main__':

    cpu = 3

    x = (len(lis)//cpu)+1

    li = []

    for i in range(cpu):
        s = i*x
        e = s+x
        li.append(lis[s:e])

    # print(li)

    pool = mp.Pool(cpu)

    pool.map(scrap,li)
