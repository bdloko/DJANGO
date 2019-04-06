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
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='DoneProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('story', models.TextField(default='', max_length=250)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.Category')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='InProgressProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('story', models.TextField(default='', max_length=250)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.Category')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company_name', models.CharField(default='', max_length=50)),
                ('address_line_1', models.CharField(default='', max_length=100)),
                ('address_line_2', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('postal_code', models.IntegerField(default='')),
                ('registration_no', models.CharField(default='', max_length=15)),
                ('email_address', models.EmailField(default='', max_length=20)),
                ('website', models.URLField(default='')),
                ('telephone', models.IntegerField(default='')),
                ('logo', models.ImageField(upload_to='logo')),
                ('description', models.TextField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='RecentProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('story', models.TextField(default='', max_length=250)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.Category')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
