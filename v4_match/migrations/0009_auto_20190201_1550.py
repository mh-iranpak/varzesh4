# Generated by Django 2.1.4 on 2019-02-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v4_match', '0008_auto_20190201_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='away_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
