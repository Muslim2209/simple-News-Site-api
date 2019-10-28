from django.conf import settings
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import CustomUser


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def add_to_default_group(sender, instance, created, **kwargs):
    if created:
        if instance.is_superuser:
            user = CustomUser.objects.get(id=instance.id)
            user.is_active = True
            user.save()
        else:
            gr, obj = Group.objects.get_or_create(name='Readers')
            instance.groups.add(gr)
