# Generated by Django 4.1.1 on 2023-03-18 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_product_img2_remove_product_img3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img2',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='img3',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='img4',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
