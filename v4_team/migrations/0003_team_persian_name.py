# Generated by Django 2.1.4 on 2019-01-29 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v4_team', '0002_auto_20190129_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='persian_name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
