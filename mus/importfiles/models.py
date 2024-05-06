from django.db import models

from projects.models import Project


class InitialUploadedFile(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    initial_file = models.FileField()
    file_name = models.CharField(max_lenght=200, defualt="")
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_processed = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=150, default='loaded')



