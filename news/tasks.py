from datetime import timedelta

from celery import shared_task
from celery.task import periodic_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task(name="send_feedback_email_task")
def send_feedback_email_task(name, email, message):
    logger.info("Sent email")
    return send_feedback_email_task(name, email, message)


@periodic_task(run_every=timedelta(days=1))
def print_every_day():
    print('Hello, 1 day reached')
