# Generated by Django 2.1.4 on 2019-02-01 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v4_match', '0013_auto_20190201_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='footballstats',
            name='offsides_away',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='footballstats',
            name='offsides_home',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
