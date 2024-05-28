import os

from django.core.files.uploadedfile import UploadedFile
from django.db.models.signals import post_save, post_delete, pre_save
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



@receiver(post_delete, sender=InitialUploadedFile)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `InitialUploaded` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)

@receiver(pre_save, sender=InitialUploadedFile)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `InitialUploadedFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = InitialUploadedFile.objects.get(pk=instance.pk).file
    except InitialUploadedFile.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)