# Generated by Django 2.1.4 on 2019-02-01 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v4_match', '0010_eventicon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='match',
        ),
        migrations.RemoveField(
            model_name='event',
            name='player1',
        ),
        migrations.RemoveField(
            model_name='event',
            name='player2',
        ),
        migrations.DeleteModel(
            name='EventIcon',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
