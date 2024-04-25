from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from os import environ
from logging import getLogger

logger = getLogger()


class Command(BaseCommand):
    def handle(self, *args, **options):
        superuser = environ.get("DJANGO_SU_NAME", "admin")
        User = get_user_model()
        if not User.objects.filter(username=superuser).exists():
            User.objects.create_superuser(
                superuser,
                environ.get("DJANGO_SU_EMAIL", "admin@domain.com"),
                environ.get("DJANGO_SU_PASSWORD", "admin"),
            )
            logger.debug("Created superuser account")
        else:
            logger.warning("Superuser exists")
