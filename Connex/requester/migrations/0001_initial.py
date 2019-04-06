# Generated by Django 2.0.3 on 2018-04-29 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('story', models.TextField(verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('is_published', models.BooleanField(default=False, verbose_name='Is published?')),
                ('view_count', models.PositiveIntegerField(default=0, verbose_name='Views')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('closing', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Requester',
            fields=[
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fullname', models.CharField(default='', max_length=50)),
                ('address_line_1', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('postal_code', models.IntegerField(default='')),
                ('email_address', models.EmailField(default='', max_length=50)),
                ('telephone', models.IntegerField(default='')),
                ('picture', models.ImageField(upload_to='picture')),
                ('description', models.TextField(default='', max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='challenge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requester.Challenge'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requester.Category', verbose_name='Category'),
        ),
    ]