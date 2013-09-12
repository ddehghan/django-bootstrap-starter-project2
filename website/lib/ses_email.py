import os
from boto.ses.connection import SESConnection

DEPLOY_ENV = os.environ['DEPLOY_ENV']

if DEPLOY_ENV == 'dev':
    from myproject.settings_local_dev import *

elif DEPLOY_ENV == 'prod':
    from myproject.settings_local_prod import *


def send_email(subject, body):
    connection = SESConnection(aws_access_key_id=AWS_ACCESS_KEY_ID,
                               aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    connection.send_email(FROM_EMAIL, subject, body, TO_EMAIL)