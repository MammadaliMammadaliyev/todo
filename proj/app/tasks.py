from django.utils import timezone
from celery import shared_task
from .models import Task, TaskNotification
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def check_task_deadlines():
    future_date = timezone.now() + timezone.timedelta(minutes=1)
    tasks = Task.objects.filter(deadline__lte=future_date, is_completed=False)

    for task in tasks:
        if task.user and task.user.email:
            if not TaskNotification.objects.filter(task=task).exists():
                send_mail(
                    subject="Task Deadline Reminder",
                    message=f"Dear {task.user.username}, your task '{task.title}' is approaching its deadline.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[task.user.email],
                    fail_silently=True,
                )

                TaskNotification.objects.create(task=task)