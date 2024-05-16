from django.db import models

from musauth.models import MusUser
from projects.models import Project


class InitialUploadedFile(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    initial_file = models.FileField()
    txt_column_delimiter = models.CharField(max_length=5, default="")
    file_name = models.CharField(max_length=200, default="")
    date_uploaded = models.DateTimeField(auto_now_add=True)
    by_user = models.ForeignKey(MusUser, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=150, default='loaded')
    validation_passed = models.BooleanField(default=False)
    thousand_separator = models.CharField(max_length=10, default='')
    decimal_separator = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.file_name


class FileMetaData(models.Model):
    file = models.OneToOneField(InitialUploadedFile, on_delete=models.CASCADE, primary_key=True)
    sum = models.FloatField()
    elements_number = models.IntegerField()




