import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("apps")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.task_routes = {
    "semple.tasks.semple_task": {"queue": "general-queue"},
    "semple.tasks.semple_task_sorted": {"queue": "helper-queue"},
    "semple.tasks.semple_task_send_email": {"queue": "email-queue"},
}
app.autodiscover_tasks()
