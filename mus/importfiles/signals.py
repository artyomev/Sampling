from django.core.files.uploadedfile import UploadedFile
from django.db.models.signals import post_save
from django.dispatch import receiver
from importfiles.models import InitialUploadedFile
from importfiles.tasks import post_save_process_file, post_save_parse_file


@receiver(post_save, sender=InitialUploadedFile)
def upload_file(**kwargs):
    instance = kwargs.get('instance')
    post_save_parse_file.delay(instance.id)


@receiver(post_save, sender=InitialUploadedFile)
def process_file(**kwargs):
    ins = kwargs.get('instance')
    post_save_process_file.delay(ins.id)
