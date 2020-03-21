DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'covid19_backend',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '',
        'TEST': {
            'NAME': 'test_covid19_backend',
            'USER': 'admin',
            'PASSWORD': 'admin',
            'HOST': '127.0.0.1'
        }
    }
}