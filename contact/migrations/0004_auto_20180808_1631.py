# Generated by Django 2.1 on 2018-08-08 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20180808_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='./logos/'),
        ),
        migrations.AlterField(
            model_name='people',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
