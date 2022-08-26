# Generated by Django 3.2.15 on 2022-08-26 19:01

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_recipe_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/jojocloudci/image/upload/v1656561920/ez8n8onczraub6ag83ua.jpg', max_length=255, verbose_name='image'),
        ),
    ]