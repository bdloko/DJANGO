# Generated by Django 2.0.5 on 2018-05-03 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requester', '0009_accept_challenge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accept',
            old_name='Challenge',
            new_name='challenge',
        ),
    ]