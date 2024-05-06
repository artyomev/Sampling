from django.db.models.signals import post_save
from django.dispatch import receiver
from importfiles.models import InitialUploadedFile
from importfiles.services.main import post_save_initial_file


@receiver(post_save, sender=InitialUploadedFile)
def upload_file(**kwargs):
    instance = kwargs.get('instance')
    post_save_initial_file(instance.initial_file, instance.id)