# Generated by Django 4.1.1 on 2023-03-15 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_e_mail_register_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='register',
        ),
    ]
