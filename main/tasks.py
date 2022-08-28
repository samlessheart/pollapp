from celery import shared_task
from datetime import datetime, timedelta
from time import sleep
from .models import Poll


@shared_task
def delete_poll():    
    time_threshold = datetime.now() - timedelta(days=1)
    polls = Poll.objects.filter(created__lt = time_threshold)
    polls.delete()
    return None


@shared_task
def sleepy(duration):
    sleep(duration)
    return None
