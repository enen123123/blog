"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.conf import global_settings

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0k(5+*e4@^anr6(-zlsondsji+a#e=+sprmh#@vuywndk_t@f*'

# SECURITY WARNING: don't run with debug turned on in production!
# 更换自己的pythonanywhere网站，需要False,并添加自己的网站
# DEBUG = False
#
# ALLOWED_HOSTS = ['enen.pythonanywhere.com']
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'post',
    # 集成富文本编辑器 ，配置第三方应用、需要下载模块django-ckeditor
    'ckeditor',
    'ckeditor_uploader',
    # 模块下载 django-haystack
    'haystack',
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware', #必须第一个
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',#必须最后一个
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 添加模板变量
                'post.mycontext.getrightinfo',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# 更改后台admin中文面板
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
# 配置静态文件
# global_settings
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static','css')
]

# 需要下载模块django-ckeditor
# 配置MEDIA映射路径
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
CKEDITOR_UPLOAD_PATH = 'upload/'

# global_settings
# 缓存
# The cache backends to use.
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    },
    # 使用redis数据库，安装模块  django-redis
    "redis": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
    }
}
CACHE_MIDDLEWARE_KEY_PREFIX = ""
# 设置缓存的时间
CACHE_MIDDLEWARE_SECONDS = 600
# pythonanywhere 需要更改为本地default
CACHE_MIDDLEWARE_ALIAS = "redis"

# INSTALLED_APPS  'haystack'  配置
# 模块下载 Whoosh
# 引包、更换引擎  更换后要重新索引

# 这里不要引入文件包，否则会乱
# from post.whoosh_cn_backend import WhooshEngine
# 全文搜索:
# haystack开源搜索框架,可支持whoosh搜索引擎,
# 由于whoosh的搜索分词对中文不友好,采用jieba模块代替其分词组件
# 指定生成的索引路径
import os
HAYSTACK_CONNECTIONS = {
        'default': {
            # 'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
            # 更换engine的地址，换取自己复制创建的文件
            'ENGINE': 'post.whoosh_cn_backend.WhooshEngine',
            # whoosh模块 全文搜索时使用
            'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
        },
    }
# 实时牛成索引文件
# 当数据库改变时,随时更新索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# python_console生成索引文件 rebuild_index


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
