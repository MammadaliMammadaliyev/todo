import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")
app = Celery("proj")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "check-for-task-deadlines": {
        "task": "app.tasks.check_task_deadlines",
        "schedule": 5.0,
    },
}