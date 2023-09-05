from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    class Meta(AbstractUser.Meta):
        db_table    = 'custom_users'

    age = models.IntegerField(verbose_name="年齢",default=20)