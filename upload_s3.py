import os
import boto3

#instantiate client
client = boto3.client('s3')

#set variables
bucket = 's3-osk-bucket-3000'
cur_path = os.getcwd()
file = ''
filename = os.path.join(cur_path, 'data', file)

#open the file
data = open(filename, 'rb')

#load data into s3
client.upload_file(filename, bucket, file)
