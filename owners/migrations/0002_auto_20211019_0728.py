# Generated by Django 3.2.8 on 2021-10-19 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='owner',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
