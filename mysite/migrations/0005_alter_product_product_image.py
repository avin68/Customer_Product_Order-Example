# Generated by Django 4.1.7 on 2023-02-25 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(null=True, upload_to='product_img', verbose_name='عکس_محصول'),
        ),
    ]
