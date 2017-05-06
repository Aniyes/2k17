from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
#from django.contrib.auth.models import User
from autoslug import AutoSlugField

# Create your models here.


class Person(AbstractUser):
    # @classmethod
    # def get_person(cls):
    #     return cls.objects.get(id=1)

    REQUIRED_FIELDS = ['gram_name',
                       'website',
                       'snap_name',
                       'email',
                       ]

    gram_name = models.CharField(max_length=20)
    snap_name = models.CharField(max_length=20)
    website = models.CharField(max_length=40)

    #product = models.ForeignKey(User.username)

    def __str__(self):
        return self.username


class Profile(models.Model):

    user = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
