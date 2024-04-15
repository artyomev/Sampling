from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from musauth.models import MusUser


class MusUserAdmin(UserAdmin):
    pass


admin.site.register(MusUser, MusUserAdmin)