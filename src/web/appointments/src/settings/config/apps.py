DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
THIRD_PARTY_APPS = [
    "rest_framework",  # https://www.django-rest-framework.org/
    # 'corsheaders',  # https://pypi.org/project/django-cors-headers/
    # 'simple_history',  # https://django-simple-history.readthedocs.io/en/latest/quick_start.html
]

LOCAL_APPS = [
    # Your stuff: custom apps go here
    "ap_auth",
    "util",
    "company",
    "appointment",
    "partner",
    "customer",
]

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
