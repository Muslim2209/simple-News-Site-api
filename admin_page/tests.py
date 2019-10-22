from django.test import TestCase
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

settings.configure()

subject = 'Subject'
html_message = render_to_string('newsletter/news.html')
plain_message = strip_tags(html_message)
from_email = "drf-no-reply@mail.ru"
to = 'dj.honor@mail.ru'

mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
