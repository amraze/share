# Generated by Django 4.0.5 on 2022-06-30 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_image_user_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='avatar',
            new_name='image',
        ),
    ]
