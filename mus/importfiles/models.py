from django.db import models

from musauth.models import MusUser
from projects.models import Project


class InitialUploadedFile(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    initial_file = models.FileField()
    file_name = models.CharField(max_length=200, default="")
    date_uploaded = models.DateTimeField(auto_now_add=True)
    by_user = models.ForeignKey(MusUser, on_delete=models.DO_NOTHING)
    date_processed = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=150, default='loaded')


    def __str__(self):
        return self.file_name
