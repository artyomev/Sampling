from django.db import models

from importfiles.models import InitialUploadedFile
from projects.models import Project


class Analysis(models.Model):
    analysis_type = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    files = models.ManyToManyField(InitialUploadedFile)
    analysis_name = models.CharField(max_length=200)
    sampled_units_count = models.IntegerField(default=0)
    sample_name = models.TextField()

    def __str__(self):
        return self.analysis_name



class AnalysisParameters(models.Model):
    analysis = models.OneToOneField(Analysis, on_delete=models.CASCADE)
    spm = models.FloatField()
    generate_random_seed = models.BooleanField(default=True)
    random_seed = models.IntegerField(default=0)

