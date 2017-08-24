from base import *
import dj_database_url

DEBUG = False

DATABASES = {}
DATABASES['default'] = dj_database_url.config()

# Paypal environment variables
SITE_URL = 'https://morning-escarpment-70084.herokuapp.com'
PAYPAL_NOTIFY_URL = 'https://morning-escarpment-70084.herokuapp.com//a-very-hard-to-guess-url'
PAYPAL_RECEIVER_EMAIL = 'dynamitedave1-facilitator@hotmail.co.uk'