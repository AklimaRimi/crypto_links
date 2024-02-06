import undetected_chromedriver as uc 
# import time 
 
# options = uc.ChromeOptions() 
# options.headless = False  # Set headless to False to run in non-headless mode

# driver = uc.Chrome() 
# driver.get("https://coinsniper.net") 
# driver.maximize_window() 

# time.sleep(30) 
# driver.save_screenshot("datacamp.png") 
# driver.close()


import undetected_chromedriver as uc
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver


if __name__ == '__main__':
    
    driver = webdriver.Chrome()

    driver.get('https://www.coinscope.co/coin/puli')
    
    sleep(20)
    
    print(driver.title)