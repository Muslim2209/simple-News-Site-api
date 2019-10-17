from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from news.managers import NewsUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_subscribed = models.BooleanField(default=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
    )

    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth', 'groups']
    USERNAME_FIELD = 'email'

    def __str__(self):
        if self.first_name or self.last_name:
            return '{} {}'.format(self.first_name, self.last_name)
        else:
            return self.email

    # class Meta:
    #     permissions = [
    #         ('admins', 'To manage users and news.'),
    #         ('editors', 'To edit news.'),
    #         ('users', 'To add news.'),
    #     ]

    objects = NewsUserManager()
