# Generated by Django 3.2.10 on 2022-01-21 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_pic', models.ImageField(default='profile_pic/default.jpg', upload_to='profile_pic')),
            ],
        ),
    ]
