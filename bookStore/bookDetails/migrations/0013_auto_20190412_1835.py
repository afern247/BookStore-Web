# Generated by Django 2.1.5 on 2019-04-12 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookDetails', '0012_auto_20190412_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
    ]
