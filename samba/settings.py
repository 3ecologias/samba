import os
import environ

# Localiza a pasta raiz do projeto, dois niveis acima
ROOT_DIR = environ.Path(__file__) - 2
APPS_DIR = ROOT_DIR.path('samba')

# Carrega o arquivo .env
env = environ.Env()
env.read_env(os.path.join(ROOT_DIR(), '.env'))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = env('SAMBA_SECRET_KEY')

DEBUG = env.bool('SAMBA_DEBUG')


ALLOWED_HOSTS = env.list('SAMBA_ALLOWED_HOSTS')

INSTALLED_APPS = [
    'dal',
    'dal_select2',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mathfilters',

    'compressor',

    'samba.accounts',
    'samba.geo',
    'samba.plan',
]

# Ativar django admin no modo DEBUG
if DEBUG:
    INSTALLED_APPS.append('django.contrib.admin')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False


COMPRESS_PRECOMPILERS = (
    ('text/x-sass', 'sassc {infile} {outfile}'),
)

ROOT_URLCONF = 'samba.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            str(APPS_DIR.path('templates'))
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'samba.wsgi.application'


DATABASES = {
    'default': env.db('SAMBA_DATABASE_URL', default='postgres:///samba')
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# STATIC_ROOT= os.path.join(BASE_DIR,'/static')
# STATIC_URL = '/static/'
# STATICFILES_DIRS = ( os.path.join(BASE_DIR,'static/'),)

if not DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s '
                          '%(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True
            },
            'django.security.DisallowedHost': {
                'level': 'ERROR',
                'handlers': ['console', 'mail_admins'],
                'propagate': True
            }
        }
    }

DEFAULT_FROM_EMAIL = env('SAMBA_EMAIL_ADDR')

LOGIN_URL = '/entrar'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
#
# MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')
# MEDIA_URL = '/static/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")

#media files

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

##EMAIL CONFIGS
# Console
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'test@gmail.com'
# SMTP
EMAIL_BACKEND = "sgbackend.SendGridBackend"
SENDGRID_API_KEY = "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"
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'admin@3ecologias.net'
EMAIL_HOST_USER = '3ecologias'
EMAIL_HOST_PASSWORD = 'm1c0leao'
EMAIL_USE_TLS = True

GOOGLE_RECAPTCHA_SECRET_KEY = '6Lfd7xwUAAAAAP3_9o_3hS1XJgyP-tiuH2pgwy_n'
