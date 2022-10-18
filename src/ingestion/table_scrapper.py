import requests
from bs4 import BeautifulSoup as bs 
import pandas as pd

def get_table(url='https://www.screener.in/company/RELIANCE'):
    page = requests.get(url)
    html_text = bs(page.text, 'html.parser')
    rows=[]
    

    df = pd.DataFrame(rows[1:], columns=rows[0])
    return df

table = get_table()
table.head(20)

