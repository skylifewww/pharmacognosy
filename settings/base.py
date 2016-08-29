import sys
from pathlib import Path

BASE_DIR = Path()


def rel(*x):
    return str(BASE_DIR.joinpath(*x).absolute())

DEBUG = False
DOMAIN = 'localhost:8000'

APPEND_SLASH = True
ALLOWED_HOSTS = ["pharmacognosy.herokuapp.com", DOMAIN]

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_COOKIE_AGE = 1209600  # (2 weeks)
SESSION_COOKIE_NAME = 'sessionid'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

SECRET_KEY = 'g_q7dlg4onpt&%*9&92@#mfmbiex474murls^vh2@iif0*bdp9'

ROOT_URLCONF = 'pharmacognosy.urls'

WSGI_APPLICATION = 'wsgi.application'

TESTING = 'test' in sys.argv[0]
DEVELOPMENT = 'run.py' in sys.argv or 'runserver' in sys.argv or 'collectstatic' in sys.argv

if 'test' in sys.argv:
    print('\033[1;91mNo django tests.\033[0m')
    print('Try: \033[1;33mpy.test\033[0m')
    sys.exit(0)

# RECAPTCHA_PUBLIC_KEY = '6LccKSgTAAAAADovCKWjMyGhPKeT_Nfc-rckYWNt'
# RECAPTCHA_PRIVATE_KEY = '6LccKSgTAAAAAKsvL4_ARxRQfZtLz_uJ1ASIpKdD'

# CAPTCHA_AJAX = True