# Generated by Django 2.1.5 on 2019-02-27 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20190227_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='addresses',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.Address'),
        ),
    ]
