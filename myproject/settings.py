import os

##################
# LOCAL SETTINGS #
##################

# Allow any settings to be defined in local_settings.py which should be
# ignored in your version control system allowing for settings to be
# defined per machine.

DEPLOY_ENV = os.environ['DEPLOY_ENV']

if DEPLOY_ENV == 'dev':
    from myproject.settings_local_dev import *

elif DEPLOY_ENV == 'prod':
    from myproject.settings_local_prod import *


#########
# PATHS #
#########

# Full filesystem path to the project.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APP_NAME = 'website'
AWS_STORAGE_BUCKET_NAME = 'django-bootstrap'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
ALLOWED_HOSTS = []
TIME_ZONE = 'America/Vancouver'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = ''
MEDIA_URL = ''

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'website', 'static')
# if DEPLOY_ENV == 'dev':
#     STATIC_URL = '/static/'
# elif DEPLOY_ENV == 'prod':
#     STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'

STATIC_URL = '/static/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    # 'social_auth.middleware.SocialAuthExceptionMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware'
)

ROOT_URLCONF = 'myproject.urls'
WSGI_APPLICATION = 'myproject.wsgi.application'

TEMPLATE_DIRS = (
    'templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # 'widget_tweaks',

    'social.apps.django_app.default',

    'website',

    # 'storages',
    # 'south',  # must be at the end of app list
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# BEGIN - Social Auth Settings

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.core.context_processors.static'
)

# SOCIAL_AUTH_PIPELINE = (
#     'social.pipeline.social_auth.social_user',
#     'social.pipeline.social_auth.associate_user',
#     'social.pipeline.social_auth.load_extra_data',
#     'social.pipeline.user.user_details'
# )

AUTHENTICATION_BACKENDS = (

    # 'social.backends.open_id.OpenIdAuth',
    # 'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    # 'social.backends.twitter.TwitterOAuth',
    # 'social.backends.yahoo.YahooOpenId',

    'django.contrib.auth.backends.ModelBackend',        #Django default auth
)

SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'
SOCIAL_AUTH_GOOGLE_OAUTH_SCOPE = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/userinfo.profile'
]

LOGIN_URL = '/login-forms'
LOGIN_REDIRECT_URL = '/private'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/private'
LOGIN_ERROR_URL = '/login-error/'
LOGOUT_URL = '/logout'

# SOCIAL_AUTH_LOGIN_ERROR_URL = '/login-error/'
# SOCIAL_AUTH_LOGIN_URL = '/login-url/'
SOCIAL_AUTH_LOGIN_URL = '/'

SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/private'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/private'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/'
SOCIAL_AUTH_INACTIVE_USER_URL = '/inactive-user/'

# SOCIAL_AUTH_USER_MODEL = 'myproject.User'

SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
SOCIAL_AUTH_UUID_LENGTH = 16
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_SLUGIFY_USERNAMES = False

SOCIAL_AUTH_SESSION_EXPIRATION = False

SOCIAL_AUTH_GOOGLE_OAUTH2_USE_DEPRECATED_API = True
SOCIAL_AUTH_GOOGLE_PLUS_USE_DEPRECATED_API = True

# END - Social Auth Settings


# Django storages to store files on S3
# if DEPLOY_ENV == 'prod':
#     STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#     DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

#############
# DATABASES #
#############
# Parse database configuration from $DATABASE_URL
import dj_database_url

DATABASES = {'default': dj_database_url.config(default='sqlite:/data.db')}


###################
# HEROKU settings #
###################
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
