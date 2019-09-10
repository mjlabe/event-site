import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "events.settings")
import django

from django.contrib.auth import get_user_model

django.setup()


def create_su():
    User = get_user_model()
    if not User.objects.filter(username='nevermorefu').exists():
        User.objects.create_superuser('super', 'super@example.com', 'eventspassword')


create_su()
