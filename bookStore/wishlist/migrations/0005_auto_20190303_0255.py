# Generated by Django 2.1.5 on 2019-03-03 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0004_auto_20190228_0217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='list',
            options={'ordering': ('user',)},
        ),
    ]
