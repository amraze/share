# Generated by Django 4.0.5 on 2022-06-30 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='image',
            new_name='avatar',
        ),
    ]
