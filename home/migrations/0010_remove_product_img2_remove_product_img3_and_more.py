# Generated by Django 4.1.1 on 2023-03-18 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_product_img2_product_img3_product_img4_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='img3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='img4',
        ),
    ]
