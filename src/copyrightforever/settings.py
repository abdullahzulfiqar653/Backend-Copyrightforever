from pathlib import Path
from datetime import timedelta
from decouple import config, Csv
from dj_database_url import parse as db_url


SRC_DIR = Path(__file__).resolve().parent.parent  # path to src which contain the all source 
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # repositry folder location


DEBUG = config('DEBUG', default=True, cast=bool)
SECRET_KEY = config('SECRET_KEY', default=NotImplemented, cast=str)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost', cast=Csv())


USER_APPS = [
    'pdf',
    'user',
    'forms',
    'userprofile',
    'transaction',
]

THIRD_PARTY_APPS = [
    'djoser',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + THIRD_PARTY_APPS + USER_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'copyrightforever.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'copyrightforever.wsgi.application'

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///' + BASE_DIR.joinpath('db.sqlite3').as_posix(),
        cast=db_url
    )
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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# EMAIL_HOST = config('EMAIL_HOST', default='localhost')
# EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
# EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
# EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
SRC_DIR.joinpath('media').as_posix()
MEDIA_ROOT = SRC_DIR.joinpath('media').as_posix()
MEDIA_URL = '/media/'




REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=5),
    'AUTH_HEADER_TYPES': ('JWT',),
}

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'ryksoft@gmail.com'
# EMAIL_HOST_PASSWORD = 'cwsjhnnhdolgqkkw'
# EMAIL_USE_TLS = True

DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    # 'USER_CHANGED_EMAIL_CONFIRMATION': True,
    # 'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    # 'SEND_CONFIRMATION_EMAIl': True,
    'SET_PASSWORD_RETYPE':True,
    # 'SEND_ACTIVATION_EMAIl': True,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
    # 'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SERIALIZERS': {
        'user_create': 'user.serializers.UserCreateSerializer',
        'user': 'user.serializers.UserCreateSerializer',
        'user_delete': 'djoser.serializers.UserCreateSerializer'
    }
}

AUTH_USER_MODEL = "user.User"
CORS_ORIGIN_ALLOW_ALL = True