# Generated by Django 4.1.7 on 2023-02-25 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customer',
            table='customer',
        ),
        migrations.AlterModelTable(
            name='orderproduct',
            table='order',
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
    ]
