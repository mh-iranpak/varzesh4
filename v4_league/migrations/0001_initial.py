# Generated by Django 2.1.4 on 2019-01-31 17:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('number_of_teams', models.IntegerField()),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1320), django.core.validators.MaxValueValidator(1500)])),
            ],
        ),
    ]
