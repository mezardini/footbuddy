from settings import *
import environ
env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True