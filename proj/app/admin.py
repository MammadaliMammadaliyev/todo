from django.contrib import admin
from .models import Task, TaskNotification


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "deadline", "is_completed")
    list_filter = ("is_completed", "deadline")
    search_fields = ("title", "user__username")


@admin.register(TaskNotification)
class TaskNotificationAdmin(admin.ModelAdmin):
    list_display = ("task", "notified_at")
    list_filter = ("notified_at",)
    search_fields = ("task__title",)