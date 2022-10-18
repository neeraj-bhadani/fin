from html.parser import HTMLParser
import requests 
from bs4 import BeautifulSoup as bs 
import re 
import pandas as pd
from datetime import datetime
import argparse
import requests
from urllib.request import urlopen as uReq
from lxml import etree

screener_stock_url = 'https://www.screener.in/company/RELIANCE'
uClient = uReq(screener_stock_url)
page = uClient.read()
uClient.close()
html = bs(page, 'html.parser')
# print(html)
page_text = requests.get('https://www.screener.in/company/RELIANCE')
# print(page_text)
html_text = bs(page_text.text, 'html.parser')
# print(html_text)
html_model = etree.HTML(str(html))
# html_content = str(html)
# html_content = html.prettify()

# with open("output1.html", "w", encoding='utf-8') as file:
#     file.write(str(html))
company_details = {
    'Name': html_model.xpath('//*[@id="top"]/div[1]/div/h1')[0].text.strip(),
    'Website': html_model.xpath('//*[@id="top"]/div[2]/a[1]/@href')[0],
    'BSE_Id': html_model.xpath('//*[@id="top"]/div[2]/a[2]/span')[0].text.strip(),
    'NSE_name': html_model.xpath('//*[@id="top"]/div[2]/a[3]/span')[0].text.strip()
}
# print(company_details)

top_ratios = {}
keys=[html_model.xpath('//*[@id="top-ratios"]/li['+str(li)+']/span[1]')[0].text.strip() for li in range(1,10)]
values=[html_model.xpath('//*[@id="top-ratios"]/li['+str(li)+']/span[2]/span')[0].text for li in range(1,10)]
print(html_model.xpath('//*[@id="quarters"]/div[1]/div[1]/h2')[0].text)

for key, value in zip(keys, values):
    top_ratios[key] = value

tables = html_text.find_all('table')
print(len(tables))
# print(tables)

# print(df)
# print(top_ratios)
# print(company_details)
# print('Classes of each table:')
# for table in html_text.find_all('table'):
#     print(table.get('class'))

dfs = pd.read_html(screener_stock_url,  flavor='bs4', thousands ='.')
for i in range(0,9):
    print(dfs[i])
print(len(dfs))


