from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

class Provider(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, to_field=None, unique=True)
    company_name = models.CharField(max_length=50, default='')
    address_line_1 = models.CharField(max_length=100, default='')
    address_line_2 = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    postal_code = models.IntegerField(default='')
    registration_no = models.CharField(max_length=15, default='')
    email_address = models.EmailField(max_length=20, default='')
    website = models.URLField(default='')
    telephone = models.IntegerField(default='')
    logo = models.ImageField(upload_to='logo')
    description = models.TextField(max_length=250, default='')

    def __str__(self):
        return u"%s" % self.username