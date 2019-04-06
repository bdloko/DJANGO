from django.db import models
from django.contrib.auth.models import User
from dj.choices import Choices, Choice, fields
from django.conf import settings
from django import forms

class Requester(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, to_field=None, unique=True)
    company = models.CharField(max_length=50, default='')
    address_line_1 = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    postal_code = models.IntegerField(default='')
    email_address = models.EmailField(max_length=50, default='')
    telephone = models.IntegerField(default='')
    picture = models.ImageField(upload_to='picture')
    description = models.TextField(max_length=250, default='')

    def __str__(self):
        return u"%s" % self.username

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return u"%s" % self.name

class Challenge(models.Model):
    CHOICES = (('Open','Open'),('Closed', 'Closed'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    title = models.CharField(max_length=50, verbose_name="Title")
    story = models.TextField(verbose_name="Story")
    status = models.CharField(choices=CHOICES, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modified at")
    closing = models.DateField(blank=True)
    
    def __str__(self):
        return u"%s" % self.title

class Comment(models.Model):
    CHOICES = (('Accept','Accept'),('Decline', 'Decline'),('Ignore', 'Ignore'))
    comment = models.TextField(blank=True)
    by = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    options = models.CharField(choices=CHOICES, max_length=20, default=0, blank=True)

    def __str__(self):
        return u"%s" % self.challenge

class Dates(models.Model):
    entry = models.DateField(blank=True)
    entry_validation = models.DateField(blank=True)
    scoring = models.DateField(blank=True)
    faciliated_judging = models.DateField(blank=True)
    announce_finalists = models.DateField(blank=True)
    presentation = models.DateField(blank=True)
    winners_announcement = models.DateField(blank=True)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'date'
        verbose_name_plural = 'dates'

    def get_absolute_url(self):
        return reverse('challenger', kwargs={'pk': self.pk})