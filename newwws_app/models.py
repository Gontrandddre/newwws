from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager



# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Article(models.Model):
    title = models.CharField("title", max_length=300, null=True)
    description = models.CharField("description", max_length=800, null=True)
    author = models.CharField("author", max_length=200, null=True)
    content = models.TextField("content", null=True)
    published_at = models.DateTimeField("published at", null=True)
    url = models.URLField("url article", null=True)
    url_to_image = models.URLField("image article", max_length=400, null=True)

    def __str__(self):
        return self.title

class Saved(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return "%s saved article %s" % (self.user.username, self.article.id)