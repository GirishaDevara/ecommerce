# Generated by Django 3.0.7 on 2020-06-12 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200612_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
