# Generated by Django 3.2.10 on 2022-01-21 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]