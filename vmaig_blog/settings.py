#coding:utf-8
"""
Django settings for vmaig_blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
import os.path
import sae.const
from os import environ
debug = not environ.get("APP_NAME", "")
if debug:
#LOCAL 本地调试用，便于导出数据库,根据本地MYSQL数据库填写下面参数<----------------如果文件中出现中文，一定要在开始添加 #coding:utf-8
    MYSQL_DB = 'todolist'
    MYSQL_USER = 'root'
    MYSQL_PASS = 'root'
    MYSQL_HOST_M = '127.0.0.1'
    MYSQL_HOST_S = '127.0.0.1'
    MYSQL_PORT = '3306'
else:
#SAE
    import sae.const
    MYSQL_DB = sae.const.MYSQL_DB
    MYSQL_USER = sae.const.MYSQL_USER
    MYSQL_PASS = sae.const.MYSQL_PASS
    MYSQL_HOST_M = sae.const.MYSQL_HOST
    MYSQL_HOST_S = sae.const.MYSQL_HOST_S
    MYSQL_PORT = sae.const.MYSQL_PORT

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q&-s%*bz^*pqzn!2$&1^)8yl*q^v3i@q6h&^#curp1u8tbd#0s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'vmaig_auth',
    'vmaig_comments',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'vmaig_blog.urls'

WSGI_APPLICATION = 'vmaig_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',#数据库类型
#         'NAME': 'vmaig',  # 数据库名称
#         'USER': 'root',  # 数据库用户名
#         'PASSWORD': 'root',  # 数据库密码
#         'HOST': '127.0.0.1',  # 数据库主机，留空默认为localhost
#         'PORT': '3306',  # 数据库端口
#
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': MYSQL_DB,
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
        'HOST': MYSQL_HOST_M,
        'PORT': MYSQL_PORT,
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# 修改上传时文件在内存中可以存放的最大size为10m
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760

# sae的本地文件系统是只读的，修改django的file storage backend为Storage
DEFAULT_FILE_STORAGE = 'sae.ext.django.storage.backend.Storage'
# 使用media这个bucket
STORAGE_BUCKET_NAME = 'media'
# ref: https://docs.djangoproject.com/en/dev/topics/files/
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

#设置user model
AUTH_USER_MODEL = "vmaig_auth.VmaigUser"


#log配置###########################################
# LOG_FILE = "./all.log"
#
# LOGGING = {
#         'version': 1,
#         'disable_existing_loggers': True,
#
#         'filters': {
#             'require_debug_false': {
#                 '()': 'django.utils.log.RequireDebugFalse'
#                 }
#             },
#         'formatters': {
#             'simple': {
#                 'format': '[%(levelname)s] %(module)s : %(message)s'
#                 },
#             'verbose': {
#                 'format': '[%(asctime)s] [%(levelname)s] %(module)s : %(message)s'
#                 }
#             },
#
#         'handlers': {
#             'null': {
#                 'level': 'DEBUG',
#                 'class': 'django.utils.log.NullHandler',
#                 },
#             'console': {
#                 'level': 'INFO',
#                 'class': 'logging.StreamHandler',
#                 'formatter': 'verbose'
#                 },
#             'file': {
#                 'level': 'INFO',
#                 'class': 'logging.FileHandler',
#                 'formatter': 'verbose',
#                 'filename': LOG_FILE,
#                 'mode': 'a',
#                 },
#             'mail_admins': {
#                 'level': 'ERROR',
#                 'class': 'django.utils.log.AdminEmailHandler',
#                 'filters': ['require_debug_false']
#                 }
#             },
#         'loggers': {
#             '': {
#                 'handlers': ['file', 'console'],
#                 'level': 'INFO',
#                 'propagate': True,
#                 },
#             'django': {
#                 'handlers': ['file', 'console'],
#                 'level': 'DEBUG',
#                 'propagate': True,
#                 },
#             'django.request': {
#                 'handlers': ['mail_admins', 'console'],
#                 'level': 'ERROR',
#                 'propagate': True,
#                 },
#             }
#         }


#cache配置#########################################
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'options': {
            'MAX_ENTRIES': 1024,
        }
    },
    'memcache': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        #'LOCATION': 'unix:/home/billvsme/memcached.sock',
        'LOCATION': '127.0.0.1:11211',
        'options': {
            'MAX_ENTRIES': 1024,
        }
    },
}


#添加templates 文件夹
TEMPLATE_DIRS = (
         os.path.join(BASE_DIR, "templates/"),
         )


#分页配置#######################################
PAGE_NUM = 3

#email配置#########################################
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.qq.com'                       #SMTP地址 例如: smtp.163.com
# EMAIL_PORT = 25                       #SMTP端口 例如: 25
# EMAIL_HOST_USER = '252319634@qq.com'                  #我自己的邮箱 例如: xxxxxx@163.com
# EMAIL_HOST_PASSWORD = 'xp830815'              #我的邮箱密码 例如  xxxxxxxxx
# EMAIL_SUBJECT_PREFIX = u'django'       #为邮件Subject-line前缀,默认是'[django]'
# EMAIL_USE_TLS = True                  #与SMTP服务器通信时，是否启动TLS链接(安全链接)。默认是false

# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

#七牛配置#######################################
qiniu_access_key = ''
qiniu_secret_key = ''
qiniu_bucket_name = ''


