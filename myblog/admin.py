from django.contrib import admin
from myblog import models


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'psw')


admin.site.register(models.user, UserAdmin)
