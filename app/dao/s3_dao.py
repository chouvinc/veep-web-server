import boto3
from os.path import basename, join
from app import app
from werkzeug.utils import secure_filename
from pprint import pprint
from flask import request


def upload_to_s3(file):
    filename = secure_filename(file.filename)

    key_id = app.config['AWS_ACCESS_KEY_ID']
    secret_key = app.config['AWS_SECRET_ACCESS_KEY']

    s3 = boto3.resource('s3',
                        aws_access_key_id=key_id,
                        aws_secret_access_key=secret_key)

    bucket_path = ''.join(['static/images/', basename(filename)])
    s3.meta.client.upload_fileobj(file,
                                  app.config['FLASKS3_BUCKET_NAME'],
                                  bucket_path,
                                  # Our bucket is private so let read-only for images
                                  ExtraArgs={'ACL': 'public-read'})
    return ''.join([app.config['S3_ENDPOINT'], bucket_path])

