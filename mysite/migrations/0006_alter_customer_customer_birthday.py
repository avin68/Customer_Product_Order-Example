# Generated by Django 4.1.7 on 2023-02-25 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_birthday',
            field=models.DateTimeField(verbose_name='تاریخ تولد مشتری'),
        ),
    ]