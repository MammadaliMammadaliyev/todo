from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "deadline", "is_completed")
    list_filter = ("is_completed", "deadline")
    search_fields = ("title", "user__username")