# Generated by Django 2.1.5 on 2019-03-23 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookDetails', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=150)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='bookDetails.Book')),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='book',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
