# Generated by Django 2.0.3 on 2018-05-03 12:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('requester', '0005_auto_20180503_1404'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AcceptButton',
            new_name='AcceptChallenge',
        ),
    ]
