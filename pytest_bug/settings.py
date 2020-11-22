
SECRET_KEY = 'kpodmr*hxaplzuz=c5fw14dt$s+3x35k%#t)(b8#if&zs_7b03'
DEBUG = True

INSTALLED_APPS = [
    'myapp',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djtest',
        'USER': 'postgres',
        'PASSWORD': 'test',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
