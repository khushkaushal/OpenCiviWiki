# Generated by Django 3.2.8 on 2021-10-15 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0002_auto_20211012_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='level',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='state',
        ),
    ]
