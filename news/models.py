from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from news.managers import NewsUserManager


class NewsCategory(models.Model):
    name = models.CharField(max_length=125, unique=True)

    class Meta:
        verbose_name_plural = 'News Categories'

    def __str__(self):
        return self.name


class NewsTag(models.Model):
    name = models.CharField(max_length=125, unique=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    image = models.ImageField(upload_to='uploads/images/', null=True, blank=True)
    attachment = models.FileField(upload_to='uploads/files/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey('NewsCategory', on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField('NewsTag', blank=True)
    is_active = models.BooleanField(default=False)
    publish_time = models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name_plural = 'News'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


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

    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth']
    USERNAME_FIELD = 'email'

    def __str__(self):
        if self.first_name or self.last_name:
            return '{} {}'.format(self.first_name, self.last_name)
        else:
            return self.email

    objects = NewsUserManager()


class Comment(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    news = models.ForeignKey('News', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:50]
