from src.ingestion.scnr import SCREENER    
from conf.config import app_config

if __name__ == "__main__":
    obj = SCREENER(company_name='reliance', config=app_config)
    screener_page = obj.scrape_page()
    company_details= obj.fetch_company_details(screener_page)
    ratio_details= obj.fetch_ratio_details()
    print('Company details:\n')
    print(company_details, '\n')
    print('Company Ratio details:\n')
    print(ratio_details, '\n')
    tables_data = obj.fetch_tables()