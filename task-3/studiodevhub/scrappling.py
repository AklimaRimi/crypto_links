
import streamlit as st
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time



from selenium.webdriver.edge.options import Options

options = Options()
options.headless = True

st.title('Welcome to Information Extractor')

link = st.text_input('Enter Amazon Book Link')
additional_options_input = st.multiselect('Select',options=['name','author','ratings','format','content','book details'])

but = st.button('Get Data')

final = {}

if but and len(link) > 0 and len(additional_options_input) > 0:
    with st.spinner('Wait for it...'):
        driver = webdriver.Edge()
        driver.get(link)
        time.sleep(1)
    
        for i in additional_options_input:
            if i == 'name':
                title = driver.find_element(By.ID , 'productTitle').text
                final['name'] = title
            if i == 'author':
                
                author = driver.find_element(By.XPATH,'//*[@id="bylineInfo"]/span/a').text
                final['author'] = author
            if i == 'content':
                try:
                    driver.find_element(By.XPATH,'//*[@id="bookDescription_feature_div"]/div/div[2]/a/span').click()
                    time.sleep(1)
                    summary = driver.find_element(By.XPATH,'//*[@id="bookDescription_feature_div"]/div/div[1]/span[7]').text
                except:
                    summary = driver.find_element(By.XPATH,'//*[@id="bookDescription_feature_div"]/div/div[1]/span[7]').text
                    
                final['content'] = summary
            if i == 'ratings':
                rating = ''
                try:
                    rating = driver.find_element(By.XPATH,'//*[@id="cm_cr_dp_d_rating_histogram"]/div[2]/div/div[2]/div/span/span').text.split(' ')[0]
                except:
                    rating = ''
                final['ratings'] = rating
            if i == 'book details':
                details =  driver.find_element(By.XPATH,'//*[@id="bookDescription_feature_div"]/div/div[1]').text
                
                final['book details'] = details
            
            cnt = 0
            info = {}
            
            if i == 'format':
                li = ['tmm-grid-swatch-KINDLE','tmm-grid-swatch-AUDIO_DOWNLOAD','tmm-grid-swatch-HARDCOVER','tmm-grid-swatch-PAPERBACK']
                for ind,val in enumerate(li):
                    try:
                        b_type = ''
                        b_price = ''
                        b_availability = ''
                        price_list = ''
                        discount = ''
                        savings = ''
                        driver.find_element(By.ID,val).click()
                        
                        text = driver.find_element(By.ID,val).text.split('\n')
                        print(len(text))
                        
                        if len(text) == 4:
                            b_type = text[0]
                            b_availability = text[3]
                            b_price = text[2]
                        elif len(text) == 3:
                            b_type = text[0]
                            b_price = text[2]
                        # time.sleep(.5)
                        # try:
                        #     b_type = driver.find_elements(By.CLASS_NAME,'slot-title')[ind].text
                        # except:
                        #     b_type = ''
                        # try:
                        #     b_price = driver.find_elements(By.CLASS_NAME,'slot-price')[ind].text
                        # except:
                        #     b_price = ''
                        # try:
                        #     b_availability = driver.find_element(By.CLASS_NAME,'slot-extraMessage')[ind].text
                        # except:
                        #     b_availability = ''
                        try:
                            price_list = driver.find_element(By.XPATH,'//*[@id="listPrice"]').text
                        except:
                            price_list = ''
                            
                        try:
                            discount = driver.find_element(By.XPATH,'//*[@id="savingsPercentage"]').text
                            if len(discount) > 0:
                                discount = discount[1:-1]
                        except:
                            discount = ''
                        try:
                            savings = driver.find_element(By.XPATH,'//*[@id="savingsAmount"]').text()
                        except:
                            savings = ''
                        
                        price_details ={}
                        format ={}
                        if len(price_list) > 0:
                            price_details['price_list'] = price_list
                        if len(discount) > 0:
                            price_details['discount'] = discount
                        if len(savings) > 0:
                            price_details['savings']  = savings
                            
                        if len(b_type) > 0:
                            format['type'] = b_type
                        if len(b_price) > 0:
                            format['price'] = b_price
                            
                        if len(b_availability) > 0:
                            format['availability'] = b_availability
                        if len(price_details) > 0:
                            format['price_details'] = price_details
                            
                        info[cnt] = format 
                        # info.append([cnt,format])                   
                        cnt+= 1
                    except:
                        print('none')
                final['format'] = [val for val in info.values()]
                
    st.success('Done!')
    # j = json.dumps(final)
    st.write(final)
    print(driver.title)
    driver.close()
