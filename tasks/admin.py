from django.contrib import admin
from .models import Task, Priority


class TaskAdmin(admin.ModelAdmin):
    list_display = ['headline', 'priority', 'deadline_date', 'creation_date']
    list_filter = ['priority', 'deadline_date', 'creation_date']
    search_fields = ['headline']


admin.site.register(Task, TaskAdmin)
admin.site.register(Priority)
