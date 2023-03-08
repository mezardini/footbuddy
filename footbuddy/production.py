from footbuddy.settings import *
import environ
env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mezzala.onrender.com', '127.0.0.1']

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True