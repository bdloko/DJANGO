# Generated by Django 2.0.3 on 2018-05-03 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('requester', '0006_auto_20180503_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('accept', models.BooleanField(choices=[('Accept', 'Accept'), ('Cancel', 'Cancel')])),
                ('accepter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='acceptchallenge',
            name='accepter',
        ),
        migrations.DeleteModel(
            name='AcceptChallenge',
        ),
    ]
