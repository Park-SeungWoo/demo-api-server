from ._base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['localhost']  # any hosts
WSGI_APPLICATION = 'config.wsgi.prod.application'
print("Production mode!")
