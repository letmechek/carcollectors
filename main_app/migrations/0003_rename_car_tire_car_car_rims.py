# Generated by Django 4.1.2 on 2022-10-26 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rim_tire'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tire',
            old_name='Car',
            new_name='car',
        ),
        migrations.AddField(
            model_name='car',
            name='rims',
            field=models.ManyToManyField(to='main_app.rim'),
        ),
    ]
