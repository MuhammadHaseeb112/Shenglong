# Generated by Django 4.1.1 on 2023-03-13 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='phone',
        ),
    ]
