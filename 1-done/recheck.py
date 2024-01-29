import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings

warnings.filterwarnings('ignore')

df1 =  pd.read_csv('1-done/coincheckup_info.csv')
df2 = pd.read_csv('1-done/coincheckup_links.csv')

df1 = df1.drop_duplicates()

df2 = df2.drop_duplicates()
df2['Links'].to_csv('1-done/coincheckup_links.csv',index=False)

links = df2['Links'].values.tolist()
links2 = df1['Project Info'].values.tolist()

link = [x for x in links if x not in links2]

print(len(links))
