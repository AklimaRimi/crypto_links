import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import multiprocessing as mp
import time


# driver = webdriver.Chrome()
# driver.maximize_window()



# df=  pd.read_csv('collect_links.csv')['Links'].values.tolist()

# x = len(df)//16


# for page in range(x+1,3855):
#     driver.get(f'https://icoholder.com/en/icos/all?fbclid=IwAR3Rl3KXEIF7s6wWzSLKIZnFwtwpqgSAfL50DvAe5daaPMUqltVmTfjLlKw&isort=r.general&idirection=desc&page={page}')
#     time.sleep(1)
#     data = []
    
#     # window_height = driver.execute_script("return window.innerHeight;")
#     # driver.execute_script(f"window.scrollBy(0, {window_height*5});")
    
#     links = driver.find_elements(By.XPATH,"//div[@class='ico-list-name-d']/h3/a")
    
#     for link in links:
#         x = link.get_attribute('href')
        
#         data.append(x)
        
#     print(page, len(data))
#     df = pd.DataFrame(data)
#     df.to_csv('collect_links.csv',index=False,mode='a',header=False)


df = pd.read_csv(f'deleted.csv')['Links'].values.tolist()
df2 = pd.read_csv(f'collect_links.csv')
df2 = df2.drop_duplicates()
# df2.to_csv(f'collect_links.csv',columns=['Links'],index=False)
df3 = pd.read_csv(f'collect_info.csv')['Project Info'].values.tolist()
lis = df2['Links'].values.tolist()
lis = [x for x in lis if (x not in df) and (x not in df3)]

print(len(lis))

def scrap(li):
    driver = webdriver.Edge()
    driver.maximize_window()
    for i in li:
        try:
            print(i,'\n\n\n')

            driver.get(f'{i}')
            time.sleep(20)
            full_name = driver.find_element(By.XPATH,"//div[@class='ico-titles-in-view']/h1").text
            new_len = driver.find_element(By.XPATH,'//*[@id="details"]/div[2]/div[1]/div/div[2]/div[1]/div[2]').text
            # full_name = full_name[:-len(new_len)]
            
            # social_media = driver.find_elements(By.XPATH,"//a[@class='ng-scope']")
            
            telegram = ''
            twitter = ''
            li = driver.find_elements(By.XPATH,"//div[@class='links-right']/div/a")
            for a in li:
                link = a.get_attribute('href')
                title = a.get_attribute('data-original-title')
                print(link)
                if link is not None and title is not None and'telegram' in title:
                    telegram = link
                if link is not None and title is not None and  'twitter' in title:
                    twitter = link    
            website = driver.find_element(By.XPATH,"//div[@class='text-align-center']/a").get_attribute('href')
            data = [[i, full_name,new_len,website,telegram,twitter]]
            df = pd.DataFrame([i])
            df.to_csv('deleted.csv',index=False,mode='a',header=False)
            
            df  = pd.DataFrame(data)
            df.to_csv('collect_info.csv',index=False,mode='a',header=False)
            
        except:
            print('Not Found')
 
    driver.close()
            
if __name__ == '__main__':

    cpu = 1

    x = (len(lis)//cpu)+1

    li = []

    for i in range(cpu):
        s = i*x
        e = s+x
        li.append(lis[s:e])

    print(li)

    pool = mp.Pool(cpu)

    pool.map(scrap,li)
