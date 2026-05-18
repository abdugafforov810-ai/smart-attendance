from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================
# SECURITY
# =========================

SECRET_KEY = 'django-insecure-...'

DEBUG = True

ALLOWED_HOSTS = []


# =========================
# INSTALLED APPS
# =========================

INSTALLED_APPS = [

    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'main',
]


# =========================
# JAZZMIN
# =========================

JAZZMIN_SETTINGS = {

    "site_title": "Smart Attendance",

    "site_header": "Smart AI Attendance",

    "site_brand": "Attendance System",

    "welcome_sign": "Welcome to Smart Dashboard",

    "copyright": "ITPROGER",

    "search_model": ["auth.User", "main.Student"],

    "topmenu_links": [

        {"name": "Home", "url": "admin:index"},

        {"name": "Dashboard", "url": "/"},

    ],

    "show_sidebar": True,

    "navigation_expanded": True,

    "hide_apps": [],

    "order_with_respect_to": ["main"],

    "icons": {

        "auth": "fas fa-users-cog",

        "auth.user": "fas fa-user",

        "main.Student": "fas fa-user-graduate",

        "main.Attendance": "fas fa-calendar-check",

    },

    "default_icon_parents": "fas fa-chevron-circle-right",

    "default_icon_children": "fas fa-circle",

    "related_modal_active": True,

    "show_ui_builder": True,

}


# =========================
# LOGIN
# =========================

LOGIN_URL = '/login/'


# =========================
# EMAIL RESET
# =========================

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# =========================
# MIDDLEWARE
# =========================

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]


# =========================
# URLS
# =========================

ROOT_URLCONF = 'itproger.urls'


# =========================
# TEMPLATES
# =========================

TEMPLATES = [

    {

        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',

            ],

        },

    },

]


# =========================
# DATABASE
# =========================

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE_DIR / 'db.sqlite3',

    }

}


# =========================
# LANGUAGE
# =========================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# =========================
# STATIC FILES
# =========================

STATIC_URL = '/static/'

STATICFILES_DIRS = [

    BASE_DIR / 'static'

]


# =========================
# DEFAULT PK
# =========================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'