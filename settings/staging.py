from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Paypal environment variables
SITE_URL = 'https://morning-escarpment-70084.herokuapp.com/'
PAYPAL_NOTIFY_URL = 'https://morning-escarpment-70084.herokuapp.com//a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = '<dynamitedave1-facilitator_api1.hotmail.co.uk>'
