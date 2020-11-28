from .settings_common import *

DEBUG = True

ALLOWED_HOSTS = []

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(Lineno)d)',
                '%(message)s',
                ])
        }
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'dev',
            'class': 'logging.StreamHandler',
        }
    },

    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
