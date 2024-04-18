from django.contrib import admin
from projects.models import Project, ProjectTeamRole

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectTeamRole)