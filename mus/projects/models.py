from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=300, blank=False)

    def __str__(self):
        return self.title


class ProjectTeam(models.Model):
    pass