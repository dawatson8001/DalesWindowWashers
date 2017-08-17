from base import *
import dj_database_url

DEBUG = False

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME':   'heroku_c29de6da34c32c7',
#        'USER': 'b1176416fdcf8d',
#        'PASSWORD': '238a5581',
#        'HOST': 'us-cdbr-iron-east-05.cleardb.net',
#        'PORT': '3306',
#    }}
DATABASES = {
    'default': dj_database_url.config('postgres://czsxgzxsffmciw:ab8c6f2f493abf6653b4aed94a9b1194c80b0112abb27c1e7f7640259983ccdc@ec2-107-22-211-182.compute-1.amazonaws.com:5432/d4e4ed0j43jfm5')
}


#DATABASES = {}
#DATABASES['default'] = dj_database_url.config('mysql://b1176416fdcf8d:238a5581@us-cdbr-iron-east-05.cleardb.net/heroku_c29de6da34c32c7')

# Paypal environment variables
SITE_URL = '/morning-escarpment-70084.herokuapp.com/'
PAYPAL_NOTIFY_URL = '/morning-escarpment-70084.herokuapp.com//a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = '/dynamitedave1-facilitator_api1.hotmail.co.uk/'