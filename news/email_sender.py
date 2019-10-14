from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from djoser import email
from djoser import utils
from djoser.conf import settings

# send_mail('Тема', 'Тело письма', settings.EMAIL_HOST_USER, ['dj.honor@mail.ru'])
from templated_mail.mail import BaseEmailMessage

from news.models import News


class Newsletter(BaseEmailMessage):
    template_name = "newsletter/news.html"

    def get_context_data(self):
        context = super().get_context_data()
        user = context.get("user")
        news = News.objects.all().order_by('-created_at')[10]
        context['news'] = news
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.UNSUBSCRIPTION_URL.format(**context)
        context["urlunsub"] = settings.UNSUBSCRIPTION_URL.format(**context)
        return context
