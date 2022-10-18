import requests 
from bs4 import BeautifulSoup as bs 
import pandas as pd

from src.utils.log_utils import set_custom_logger
import src.utils.fin_utils as f_utils 
from lxml import etree



class SCREENER:
    def __init__(self, company_name, config):
        self.logger = set_custom_logger()
        self.logger.info("--Running the scraper--")

        self.config = config
        self.company_name = company_name
        
        if company_name is not None:
            self.logger.info("--Scraping screener.in for {}".format(self.company_name))
        else:
            self.logger.error('Company name missing')

    def scrape_page(self):
        self.screener_url = 'https://www.screener.in/company/' + self.company_name
        try:
            self.screener_page = requests.get(self.screener_url)
            self.logger.info('Successfully scraped url : {}'.format(self.screener_page))
            return self.screener_page
        except Exception as e:
            self.logger.info('Invalid URL')
            self.logger.error('scrape_page() failed!')
            self.logger.exception(e)
            raise e
        
        
    def fetch_company_details(self, screener_page):    
        try:
            self.html_content = bs(screener_page.text, 'html.parser')
            self.html_model = etree.HTML(str(self.html_content))
            #can be put into a inpuit data model for strict type checking and can be moved to a mapper function
            self.company_details = {
                'Name': self.html_model.xpath('//*[@id="top"]/div[1]/div/h1')[0].text.strip(),
                'Website': self.html_model.xpath('//*[@id="top"]/div[2]/a[1]/@href')[0],
                'BSE_Id': self.html_model.xpath('//*[@id="top"]/div[2]/a[2]/span')[0].text.strip(),
                'NSE_name': self.html_model.xpath('//*[@id="top"]/div[2]/a[3]/span')[0].text.strip()
            }
            self.logger.info("Successfully fetched company details")
            return self.company_details
        except Exception as e:
            self.logger.error('fetch_company_details() failed!')
            self.logger.exception(e)
            raise e
        
    def fetch_ratio_details(self):
        try:
            self.ratios = {}
            self.keys=[self.html_model.xpath('//*[@id="top-ratios"]/li['+str(li)+']/span[1]')[0].text.strip() for li in range(1,10)]
            self.values=[self.html_model.xpath('//*[@id="top-ratios"]/li['+str(li)+']/span[2]/span')[0].text for li in range(1,10)]
            for key, value in zip(self.keys, self.values):
                self.ratios[key] = value
            self.logger.info("Successfully fetched company ratio details")
            return self.ratios
        except Exception as e:
            self.logger.error('fetch_ratio_details() failed!')
            self.logger.exception(e)
            raise e

    def fetch_tables(self):
        try: 
            self.tables_list = pd.read_html(self.screener_url, flavor='bs4',thousands=',')
            self.logger.info("Successfully fetched data of {} tables".format(len(self.tables_list)))
            f_utils.store_csv_in_s3(self.tables_list, self.config, self.company_name)
            return self.tables_list
        except Exception as e:
            self.logger.error("fetch_tables() failed!")
            self.logger.exception(e)
            raise e

    
    
    def tables_renaming(self, tables_data):
        try:
            self.quarterly_results = tables_data[0]
            self.quarterly_results.to_csv('quarterly_results.csv')
            self.logger.info("Fetched Quarterly results")
        except:
            self.logger.error("Couldn't fetch Quarterly results")

        try:
            self.profit_loss = tables_data[1]
            self.logger.info("Fetched Profit/loss results")
        except:
            self.logger.error("Couldn't fetch Profit/loss results")

        try:
            self.compounded_sales_growth = tables_data[2]
            self.logger.info("Fetched compunded sales growth")
        except:
            self.logger.error("Couldn't fetch compounded sales growth")

        try:
            self.compounded_sales_growth = tables_data[2]
            self.logger.info("Fetched compunded sales growth")
        except:
            self.logger.error("Couldn't fetch compounded sales growth")

        try:
            self.compounded_sales_growth = tables_data[2]
            self.logger.info("Fetched compunded sales growth")
        except:
            self.logger.error("Couldn't fetch compounded sales growth")

        try:
            self.compounded_sales_growth = tables_data[2]
            self.logger.info("Fetched compunded sales growth")
        except:
            self.logger.error("Couldn't fetch compounded sales growth")

        try:
            self.compounded_sales_growth = tables_data[2]
            self.logger.info("Fetched compunded sales growth")
        except:
            self.logger.error("Couldn't fetch compounded sales growth")

