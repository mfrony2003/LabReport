from .basesettings import *
import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
    



SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': os.environ.get("LOCAL_DATABASES_ENGINE"),
        'NAME':  os.environ.get("LOCAL_DATABASES_NAME"),
    }
}