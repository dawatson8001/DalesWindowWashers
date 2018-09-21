from base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': os.path.join(BASE_DIR, '../../db.sqlite3'),
    }
}

DATABASES['default'] = dj_database_url.config()


# Paypal environment variables
SITE_URL = 'https://daleswindowwashers.herokuapp.com'
PAYPAL_NOTIFY_URL = 'https://daleswindowwashers.herokuapp.com//a-very-hard-to-guess-url'
PAYPAL_RECEIVER_EMAIL = 'dynamitedave1-facilitator@hotmail.co.uk'