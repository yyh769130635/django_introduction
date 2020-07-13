from django.test import TestCase
import os
import sys

# Create your tests here.
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_introduction.settings")

    import django

    django.setup()
    from blog import models
