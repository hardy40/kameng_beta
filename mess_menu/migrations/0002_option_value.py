# Generated by Django 2.0.1 on 2018-08-29 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess_menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]
