from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def add_to_default_group(sender, instance, created, **kwargs):
    if created:
        gr = Group.objects.get(name='readers')
        instance.groups.add(gr)
        for item in ['view_news', 'view_newscategory', 'view_newstag', 'add_comment', 'view_comment']:
            per = Permission.objects.get(codename=item)
            instance.user_permissions.add(per)
