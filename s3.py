from config import AWS_ACCESS_KEY, AWS_SECRET_KEY, REGION_NAME, BUCKET_NAME
import boto3


class S3Connection(object):

    def __init__(self):
        '''
        s3 객체 생성
        '''
        self.aws_access_key = AWS_ACCESS_KEY
        self.aws_secret_key = AWS_SECRET_KEY
        self.bucket_name = BUCKET_NAME

        self.client = boto3.client('s3',
                                   endpoint_url=None,
                                   aws_access_key_id=self.aws_access_key,
                                   aws_secret_access_key=self.aws_secret_key,
                                   region_name=REGION_NAME
                                   )
        
    
    def get_image(self, key):
        try:
            self.client.get_object(Bucket=BUCKET_NAME, Key=key)
        except Exception as e:
            print(e)
    
    
    def put_image(self, filename):
        try:
            self.client.upload_file(
                Filename=filename,
                Bucket=self.bucket_name
            )
            return True
        except Exception as e:
            print(e)