# Generated by Django 4.0.5 on 2022-06-30 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_avatar_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]