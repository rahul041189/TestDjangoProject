# Generated by Django 2.1 on 2018-08-22 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0002_screen'),
    ]

    operations = [
        migrations.AddField(
            model_name='screen',
            name='is_fav',
            field=models.BooleanField(default=False),
        ),
    ]
