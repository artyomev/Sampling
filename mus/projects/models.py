from django.db import models


from musauth.models import MusUser


class Project(models.Model):
    title = models.CharField(max_length=300, blank=False)
    users = models.ManyToManyField(MusUser, through="ProjectTeamRole")

    def __str__(self):
        return self.title


class ProjectTeamRole(models.Model):
    user = models.ForeignKey(MusUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=250,choices=(('Manager', 'Manager'),
                                                    ('Partner','Partner'),
                                                    ('Staff','Staff'),
                                                    ('Incharge','Incharge'),)
                            )
    def __str__(self):
        return f"{self.role} for project: {self.project.title}"


