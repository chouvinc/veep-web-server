import boto3
from os.path import basename, join
from app import app
from werkzeug.utils import secure_filename
from pprint import pprint
from flask import request


# This is unused until we add edit functionality. We can't use flask-wtf's FileField form field
# since our existing form has other non-flask-wtf form fields. Since flask-wtf can only take in
# both request.files and request.form, it means that those fields are exclusive of each other.
# It's a really dumb bug that you can read more on here: https://github.com/pallets/flask/issues/460
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

