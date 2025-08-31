# alx_backend_caching_property_listings/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # required
        'NAME': 'property_db',
        'USER': 'property_user',
        'PASSWORD': 'property_password',
        'HOST': 'postgres',  # matches docker-compose service name
        'PORT': '5432',      # required
    }
}
