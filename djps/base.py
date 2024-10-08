from kombu import Exchange, Queue

from .settings import *

# often used libraries

INSTALLED_APPS += [
    'django_cleanup',
    'widget_tweaks',
    'corsheaders'
]


# allauth

INSTALLED_APPS += [
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
SITE_ID = 1
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_ADAPTER = 'main.adapter.AccountAdapter'

LOGIN_REDIRECT_URL = '/'

SOCIALACCOUNT_QUERY_EMAIL = True

SOCIALACCOUNT_EMAIL_REQUIRED = False
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_EMAIL_VERIFICATION = None

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
         {'METHOD': 'oauth2',
          'SCOPE': ['email', 'public_profile', 'user_friends'],
          'AUTH_PARAMS': {'auth_type': 'rerequest'},
          'FIELDS': [
              'id',
              'email',
              'name',
              'first_name',
              'last_name',
              'verified',
              'locale',
              'timezone',
              'link',
              'gender',
              'updated_time'],
          'EXCHANGE_TOKEN': True,
          'LOCALE_FUNC': lambda request: 'ru_RU',
          'VERIFIED_EMAIL': False,
          'VERSION': 'v2.4'},
     'google':
         {'SCOPE': ['email'],
          'AUTH_PARAMS': {'access_type': 'online'}
          }

     }


# rest framework / swagger ui

INSTALLED_APPS += [
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'rest_framework',
    'rest_framework_swagger',
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2,
    'DEFAULT_PERMISSION_CLASSES': (
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    )
}


# ckeditor

INSTALLED_APPS += [
    'ckeditor',
    'ckeditor_uploader'
]

CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
CKEDITOR_JQUERY_URL = 'http://libs.baidu.com/jquery/2.0.3/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'language': 'ru',
        'toolbar': 'full'
    }
}

# redis/celery

CELERY_BROKER_URL = "redis://{}:6379".format(
    os.environ.get('REDIS_HOST', 'localhost'))
CELERY_RESULT_BACKEND = 'redis://{}:6379'.format(
    os.environ.get('REDIS_HOST', 'localhost'))
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

CELERY_QUEUES = (
    Queue('high', Exchange('high'), routing_key='high'),
    Queue('normal', Exchange('normal'), routing_key='normal'),
    Queue('low', Exchange('low'), routing_key='low'),
)

CELERY_DEFAULT_QUEUE = 'normal'
CELERY_DEFAULT_EXCHANGE = 'normal'
CELERY_DEFAULT_ROUTING_KEY = 'normal'