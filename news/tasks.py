from time import sleep

from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from news.models import News
from users.models import CustomUser


@shared_task
def send_weekly_news():
    subject = 'Weekly news'
    news = News.objects.all().order_by('-created_at')[:5]
    html_message = render_to_string('newsletter/news.html', {'news': news})
    plain_message = strip_tags(html_message)
    from_email = "drf-no-reply@mail.ru"
    to = CustomUser.objects.filter(is_subscribed=True).values_list('email')
    email_list = [x for (x,) in to]

    for item in email_list:
        send_mail(subject, plain_message, from_email, [item], html_message=html_message, fail_silently=False)
        sleep(1)
