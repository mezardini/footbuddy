from footbuddy.settings import *
import environ
env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mezzala.onrender.com', '127.0.0.1', 'localhost']

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

SITE_ID = 1

LOGIN_REDIRECT_URL = 'https://mezzala.onrender.com/'
LOGOUT_REDIRECT_URL = 'https://mezzala.onrender.com/'