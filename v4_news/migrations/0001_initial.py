# Generated by Django 2.1.4 on 2019-01-21 19:06

from django.db import migrations, models
import django.utils.timezone
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True)),
                ('body', models.CharField(max_length=2048)),
                ('image', models.ImageField(upload_to='')),
                ('sources', models.CharField(max_length=512)),
                ('tags', models.CharField(max_length=512)),
                ('created_at', django_jalali.db.models.jDateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]