from .settings import *
import dj_database_url

DATABASE_URL = os.environ.get('DATABASE_URL', False)
if not DATABASE_URL:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=False)
    DATABASES['default'].update(db_from_env)
