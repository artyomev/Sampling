from django.db import models

from musauth.models import MusUser


class Project(models.Model):
    title = models.CharField(max_length=300, blank=False)

    def __str__(self):
        return self.title


class ProjectTeam(models.Model):
    partner = models.ForeignKey(MusUser,
                                on_delete=models.CASCADE,
                                related_name='teams_as_partner'
                                )
    manager = models.ForeignKey(MusUser,
                                on_delete=models.CASCADE,
                                related_name='teams_as_manager'
                                )
    incharge = models.ForeignKey(MusUser,
                                on_delete=models.CASCADE,
                                related_name='teams_as_incharge'
                                )
    staff = models.ManyToManyField(MusUser)
    project = models.OneToOneField(Project,
                                    on_delete=models.CASCADE,
                                    primary_key=True)