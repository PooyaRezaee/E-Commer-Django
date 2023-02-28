import os
from datetime import timedelta
from django.conf import  settings
from celery import Celery
from dotenv import load_dotenv

load_dotenv()
settings_type = os.getenv('SETTINGS_TYPE')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"settings.{settings_type}")

app = Celery("core")
app.autodiscover_tasks()

app.conf.update(
    brocker_url="amqp://",
    resualt_backend="rpc://",
    task_serializer="json",
    resualt_serializer="pickle",
    accept_content=['json','pickle'],
    resualt_expires = timedelta(days=1),
    task_always_eager=False,
)