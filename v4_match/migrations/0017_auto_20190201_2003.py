# Generated by Django 2.1.4 on 2019-02-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v4_match', '0016_auto_20190201_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='multimedia',
            name='link',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name='multimedia',
            name='file',
            field=models.FileField(upload_to='resources/images/multimedias'),
        ),
    ]