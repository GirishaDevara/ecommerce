# Generated by Django 3.0.7 on 2020-06-12 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Price',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=20),
        ),
    ]