DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'example',    
        'USER': 'vagrant',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}