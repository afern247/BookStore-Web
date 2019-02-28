# Generated by Django 2.1.5 on 2019-02-12 21:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0002_auto_20190212_1629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wbooks',
            old_name='list_name',
            new_name='wList_name',
        ),
        migrations.AddField(
            model_name='wlists',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='wbooks',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]