# Generated by Django 2.1.4 on 2019-01-31 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v4_league', '0002_auto_20190131_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='league',
            name='number_of_teams',
        ),
    ]
