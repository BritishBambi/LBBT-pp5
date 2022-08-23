# Generated by Django 3.2.15 on 2022-08-20 22:19

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20220817_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder.jpg', max_length=255, verbose_name='image'),
        ),
    ]