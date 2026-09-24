from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "classroom-demo-only-not-for-deployment"
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "testserver"]

INSTALLED_APPS = ["tasks"]
MIDDLEWARE = ["django.middleware.csrf.CsrfViewMiddleware"]
ROOT_URLCONF = "site_config.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {},
    }
]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
