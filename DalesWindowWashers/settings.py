import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'y&)wtg2ydn&rnu^3d^$no)d!wbzs3)31mo1f*c%@fk97im5=%s'

DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'Accounts_app.User'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'staticfiles'))

STATICFILES_DIRS = (

    os.path.join(BASE_DIR, 'static'),
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'Comments_app',
    'django_forms_bootstrap',
    'Accounts_app',
    'paypal.standard.ipn',
    'Products_app',
    'emoticons',
    'tinymce',
    'disqus',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DalesWindowWashers.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [os.path.join(BASE_DIR, 'templates')],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DalesWindowWashers.wsgi.application'

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {

        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {

        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {

        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (

    'django.contrib.auth.backends.ModelBackend',

    'Accounts_app.backends.EmailAuth',
)

SITE_URL = 'https://morning-escarpment-70084.herokuapp.com/'

PAYPAL_NOTIFY_URL = 'https://morning-escarpment-70084.herokuapp.com//a-very-hard-to-guess-url/'

PAYPAL_RECEIVER_EMAIL = '<dynamitedave1-facilitator_api1.hotmail.co.uk>'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TINYMCE_JS_ROOT = os.path.join(BASE_DIR, "static", 'js', 'tinymce', 'tinymce.min.js')
