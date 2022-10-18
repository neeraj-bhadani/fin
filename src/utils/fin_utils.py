import csv
import json
from s3_utils import AmazonS3 as s3
from src.utils.log_utils import LOGGER

from utils.log_utils import set_custom_logger

LOGGER=set_custom_logger()

def fin_json_load(json_path, block=None):
    
    try:
        with open(json_path) as read_file:
            json_data = json.load(read_file)
        if block and json_data:
            json_data = json_data[block][0]
    except Exception as json_load_exception:
        LOGGER.error("Couldn't load app.json file")
        LOGGER.exception(json_load_exception)
        raise json_load_exception
    return json_data

def store_csv_in_s3(tables_list, json_path, company_name):
    json_block = fin_json_load(json_path, 's3')

    try:
        for i in range(0,10):
            s3.push_data_to_s3_bucket(bucket_name = json_block['bucket_name'],
                                    data= tables_list[i],   
                                    file_name = json_block['folder_name']+'/'+company_name+'/'+i,
                                    content_type= csv)
            LOGGER.info("Successfully uploaded {}.csv to s3".format(i))
    except:
        LOGGER.info("unable to upload to s3")