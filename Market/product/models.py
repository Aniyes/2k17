from django.db import models
from django import forms
#from django.contrib.auth.models import User
from accounts.models import Person
from autoslug import AutoSlugField


# Create your models here.


class Review(models.Model):
    name = models.CharField(max_length=10)
    comment = models.TextField()

    #product = models.ForeignKey(Product)

    def __str__(self):
        return self.product


class Collection(models.Model):

    LECTION = (('C', 'Caps'),
               ('T', 'Tees'))

    category = models.CharField(choices=LECTION, max_length=20)

    def __str__(self):
        return self.category


class Product(models.Model):


    Sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )
    title = models.CharField(max_length=30)
    description = models.TextField()
    size = models.CharField(max_length=1, choices=Sizes, default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=6.99, null=True, blank=True)
    photo = models.ImageField()
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    category = models.CharField(max_length=10, default='default')
    #slug = AutoSlugField(populate_from=title, unique_with=user.__str__(), default='default')

    #collection = models.ForeignKey(Collection, related_name='products')

    def __str__(self):
        return self.title

    # class Meta:
    #     ordering = ['title']


class Register(models.Model):

    User_name = models.CharField(max_length=15)
    Password = models.CharField(max_length=15)
    Email = models.CharField(max_length=20)

