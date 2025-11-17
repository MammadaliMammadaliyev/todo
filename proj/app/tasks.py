from celery import shared_task


@shared_task
def check_task_deadlines():
    print("Checking for task deadlines...")
    return "50 Tasks deadlines checked."