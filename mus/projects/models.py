from django.db import models

from musauth.models import MusUser


class Project(models.Model):
    title = models.CharField(max_length=300, blank=False)

    def __str__(self):
        return self.title


class ProjectTeam(models.Model):
    partner = models.ForeignKey(MusUser,
                                on_delete=models.CASCADE,
                                related_name='partner'
                                )
    manager = models.ForeignKey(MusUser,
                                on_delete=models.CASCADE,
                                related_name='manager'
                                )
    incharge = models.ForeignKey(MusUser,
                                on_delete=models.CASCADE,
                                related_name='incharge'
                                )
    staff = models.ManyToManyField(MusUser,
                                   related_name='staff_of'
                                   )
    project = models.OneToOneField(Project,
                                    on_delete=models.CASCADE,
                                    primary_key=True,
                                   related_name='projects')

    def __str__(self):
        return f"{self.project.title} project team"
    class Meta:
        verbose_name = 'Project team'
