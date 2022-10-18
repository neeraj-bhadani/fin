from src.utils.s3_utils import AmazonS3
from io import BytesIO
from src.utils.log_utils import set_custom_logger
import threading

LOGGER = set_custom_logger()


def fin_json_load(config, block=None):

    try:
        json_data = config
        if block and json_data:
            json_data = json_data[block]
    except Exception as json_load_exception:
        LOGGER.error("Couldn't load app.json file")
        LOGGER.exception(json_load_exception)
        raise json_load_exception
    return json_data


def store_csv_in_s3(tables_list, config, company_name):
    s3 = AmazonS3(config=config)
    s3_config = fin_json_load(config, "s3")
    try:
        x = threading.Thread(target=store_table_data, args=(s3, tables_list, company_name, s3_config))
        x.start()
        LOGGER.info("Storing csv in s3 in threads")
    except Exception as e:
        LOGGER.info("unable to upload to s3 with error:", e)


def store_table_data(s3, tables_list, company_name, s3_config):
    for i, table_list in enumerate(tables_list):
        bytesIO = BytesIO(bytes(table_list.to_csv(), "utf-8"))
        s3.push_data_to_s3_bucket(
            bucket_name=s3_config["bucket_name"],
            bytesIO=bytesIO,
            file_name=s3_config["folder_name"] + "/" + company_name + "/" + str(i),
            content_type="text/csv",
        )
        LOGGER.info("Successfully uploaded {}.csv to s3".format(i))
