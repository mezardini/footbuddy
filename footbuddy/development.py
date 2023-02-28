from footbuddy.settings import *
import environ
env = environ.Env()
environ.Env.read_env()


SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']