import boto3
from botocore.client import Config

def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()

def s3(infile, bucket, name):
    s3 = boto3.client('s3',
                    endpoint_url='http://localhost:9000',
                    aws_access_key_id='minioadmin',
                    aws_secret_access_key='minioadmin',
                    config=Config(signature_version='s3v4'),
                    region_name='us-east-1')
    s3.upload_fileobj(infile, bucket, name)

