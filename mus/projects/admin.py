from django.contrib import admin
from projects.models import Project, ProjectTeam

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectTeam)