# Generated by Django 2.1.4 on 2019-02-01 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v4_match', '0014_auto_20190201_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='footballstats',
            name='saves_away',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='footballstats',
            name='saves_home',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
