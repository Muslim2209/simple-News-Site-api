# from django.conf import settings
# from django.contrib.auth.tokens import default_token_generator
# from django.core import mail
# from django.core.mail import EmailMessage
# from django.shortcuts import render
# from django.template.loader import get_template
# from djoser import utils
# from templated_mail.mail import BaseEmailMessage
#
# from news.models import News
#
#
# class Mailer:
#     def __init__(self, from_email=None):
#         # TODO setup the default from email
#         self.connection = mail.get_connection()
#         self.from_email = from_email
#
#     def send_messages(self, subject, template, context, to_emails):
#         messages = self.__generate_messages(subject, template, context, to_emails)
#         self.__send_mail(messages)
#
#     def __send_mail(self, mail_messages):
#         """
#         Send email messages
#         :param mail_messages:
#         :return:
#         """
#         self.connection.open()
#         self.connection.send_messages(mail_messages)
#         self.connection.close()
#
#     def __generate_messages(self, subject, template, context, to_emails):
#         """
#         Generate email message from Django template
#         :param subject: Email message subject
#         :param template: Email template
#         :param to_emails: to email address[es]
#         :return:
#         """
#         messages = []
#         message_template = get_template(template)
#         for recipient in to_emails:
#             message_content = message_template.render(context)
#             message = EmailMessage(subject, message_content, to=[recipient], from_email=self.from_email)
#             message.content_subtype = 'html'
#             messages.append(message)
#
#         return messages
#
#
# class Newsletter(BaseEmailMessage):
#     template_name = "newsletter/news.html"
#
#     def get_context_data(self):
#         context = super().get_context_data()
#         user = context.get("user")
#         news = News.objects.all().order_by('-created_at')[1]
#         context['news'] = news
#         context["uid"] = utils.encode_uid(user.pk)
#         context["token"] = default_token_generator.make_token(user)
#         context["url"] = settings.UNSUBSCRIPTION_URL  # .format(**context)
#         return render(self.request, self.template_name, context)
