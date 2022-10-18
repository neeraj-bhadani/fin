import sys
import os
import boto3
from boto3.s3.transfer import TransferConfig
import threading
from src.utils.log_utils import set_custom_logger
import src.utils.fin_utils as utils

class AmazonS3:

    def __init__(self, config):
        self.logger = set_custom_logger()
        self.json_block = utils.fin_json_load(config, 's3')
        self.s3 = boto3.resource('s3',
               aws_access_key_id = self.json_block['access_key'],
               aws_secret_access_key= self.json_block['secret_key']
               )
        self.logger.info("S3 connecteed")


    def push_data_to_s3_bucket(self , bucket_name ,bytesIO , file_name, content_type ):
        
        config = TransferConfig( multipart_threshold=1024 * 25, #limit above which multiparts activate
                                max_concurrency=15, #threads
                                multipart_chunksize=1024 * 25, #size of data in each thread
                                use_threads=True) #enabling threads
        with bytesIO as data:
            self.s3.Object(bucket_name, file_name).upload_fileobj(data,
                                                    ExtraArgs={'ContentType': content_type},
                                                    Config=config
                                                    )
    
    def show_contents_s3_bucket(self,bucket_name):
        bucket = self.s3.Bucket(bucket_name)
        print()
        print(f"Bucket : {bucket_name}")
        for obj in bucket.objects.all():
            print(f'filename : {obj.key} ')

    def delete_contents_s3_bucket(self,bucket_name,file_name ):
        self.s3.Object(bucket_name, file_name).delete()
        self.show_contents_s3_bucket(bucket_name)

    def empty_bucket(self, bucket_name):
        self.s3.Bucket(bucket_name).objects.all().delete()

    class ProgressPercentage(object):
            def __init__(self, filename, size):
                self._filename = filename
                self._size = float(size)
                self._seen_so_far = 0
                self._lock = threading.Lock()

            def __call__(self, bytes_amount):
                with self._lock:
                    self._seen_so_far += bytes_amount
                    percentage = (self._seen_so_far / self._size) * 100
                    sys.stdout.write(
                        "\r%s  %s / %s  (%.2f%%)" % (
                            self._filename, self._seen_so_far, self._size,
                            percentage))
                    sys.stdout.flush()