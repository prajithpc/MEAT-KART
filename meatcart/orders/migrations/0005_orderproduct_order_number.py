# Generated by Django 4.2.3 on 2023-08-16 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_orderproduct_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='order_number',
            field=models.CharField(default='', max_length=20),
        ),
    ]
