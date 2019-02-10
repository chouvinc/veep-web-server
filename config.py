import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Specify which emails are admins that want to receive website emails
    ADMINS = os.environ.get('ADMINS') or "vin.chou@mail.utoronto.ca"

    # Specify mail server config
    MAIL_SERVER = "smtp.zoho.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    # "Secret" key
    SECRET_KEY = os.environ.get('SECRET_KEY') or '1A2B3Cabc!@#!@#'

    # SQLAlchemy (DB) config. Currently runs Postgres on Heroku.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    # Legacy config that defaults to True if not set, but we don't use it so set to FALSE
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # S3 stuff
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    FLASKS3_BUCKET_NAME = os.environ.get('FLASKS3_BUCKET_NAME') or 'veep-member-pictures'
    FLASKS3_FILEPATH_HEADERS = {
        r'.css$': {
            'Content-Type': 'text/css',
        }
    }
    S3_ENDPOINT = os.environ.get('S3_ENDPOINT') or 'https://veep-member-pictures.s3.amazonaws.com/'
    UPLOAD_FOLDER = '/uploads'

    CLOUDFRONT_DOMAIN = 'dm6wzlkxkxah7.cloudfront.net'


