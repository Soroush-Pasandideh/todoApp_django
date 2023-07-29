from django.contrib import admin

from . import models
from .models import Task


# admin.site.register(Task)


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'username', 'complete']
    list_per_page = 10
    list_filter = ['user']
    search_fields = ['title']

    def username(self, task):
        return task.user.username
