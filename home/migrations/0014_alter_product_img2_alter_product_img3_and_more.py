# Generated by Django 4.1.1 on 2023-03-19 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_product_img_alter_product_img2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img2',
            field=models.ImageField(default=None, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img3',
            field=models.ImageField(default=None, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img4',
            field=models.ImageField(default=None, null=True, upload_to='images/'),
        ),
    ]