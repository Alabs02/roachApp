# Generated by Django 2.2.6 on 2019-11-01 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20191101_2131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='Location',
            new_name='location',
        ),
    ]
