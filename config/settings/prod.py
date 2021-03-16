from .base import *

ALLOWED_HOSTS = ['3.36.198.59']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': ':2+XH,e&)J;v&^0NAdQPDPFn^xqW(o03',
        'HOST': 'ls-6497a8e2c71bd8093be073a76a6be698b14186a7.chdk0lih9kbr.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432'
    }
}