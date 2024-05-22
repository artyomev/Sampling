from django.conf import settings
from django.core.management.base import BaseCommand
from musauth.models import MusUser

class Command(BaseCommand):

    def handle(self, *args, **options):
        if MusUser.objects.count() == 0:
            for user in settings.ADMINS:
                username = user[0]
                email = user[1]
                password = 'admin'
                admin = MusUser.objects.create_superuser(email=email, username=username, password=password)
                admin.is_active = True
                admin.is_admin = True
                admin.save()
