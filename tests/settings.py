import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "lite_youtube_embed",
    "tests",
    # Wagtail stuff
    "django.contrib.auth",
    "django.contrib.messages",
    "django.contrib.contenttypes",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.admin",
    "wagtail",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    },
]

SECRET_KEY = "abcde12345"

ROOT_URLCONF = "tests.urls"

STATIC_URL = "/static/"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

WAGTAILEMBEDS_FINDERS = [
    {
        "class": "lite_youtube_embed.LiteYouTubeEmbedFinder",
    },
    {
        "class": "wagtail.embeds.finders.oembed",
    },
]
