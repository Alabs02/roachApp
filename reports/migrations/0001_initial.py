# Generated by Django 2.2.6 on 2019-11-01 21:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Bad Roads', max_length=100)),
                ('Location', models.CharField(default='Area', max_length=100)),
                ('slug', models.SlugField(default='')),
                ('content', models.TextField(default='')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
