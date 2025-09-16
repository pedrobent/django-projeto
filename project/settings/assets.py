from .environment import BASE_DIR
import os

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join('/etc/pedro/app_repo', 'static')

MEDIA_URL = '/media'
MEDIA_ROOT = BASE_DIR / 'media'