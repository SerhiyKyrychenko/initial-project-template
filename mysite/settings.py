"""
Налаштування Django для проекту mysite.

Згенеровано за допомогою 'django-admin startproject' використовуючи Django 5.1.3.

Для отримання додаткової інформації про цей файл дивіться
https://docs.djangoproject.com/en/5.1/topics/settings/

Повний список налаштувань та їх значень дивіться тут:
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Створення шляхів у проекті, наприклад: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Швидкі налаштування для розробки - непридатні для використання у продакшені
# Дивіться https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# УВАГА! Зберігайте секретний ключ, що використовується у продакшені, у таємниці!
SECRET_KEY = 'django-insecure-695!pu8fzr$y9y(=cb+jf+p5n(en&spu$1=ujn62zstuuf4ujv'

# УВАГА! Не вмикайте режим налагодження (DEBUG) у продакшені!
DEBUG = True

ALLOWED_HOSTS = []


# Визначення додатків

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# База даних
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Перевірка паролів
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Інтернаціоналізація
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Статичні файли (CSS, JavaScript, Зображення)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Тип первинного ключа за замовчуванням
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
