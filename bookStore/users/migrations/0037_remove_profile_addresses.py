# Generated by Django 2.1.5 on 2019-02-28 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0036_auto_20190228_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='addresses',
        ),
    ]
