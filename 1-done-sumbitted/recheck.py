import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings

warnings.filterwarnings('ignore')

df1 =  pd.read_csv('1-done/coincheckup_info.csv')
df1 = df1.drop_duplicates(['Project Info'])
df1 = df1.sort_values(['Full Name'])
df1.to_csv('1-done/coincheckup_info.csv',index=False)
