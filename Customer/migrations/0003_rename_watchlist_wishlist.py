# Generated by Django 3.2.4 on 2021-06-27 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vendors', '0004_products_product_quantity'),
        ('Signup', '0003_customer_model_user_type'),
        ('Customer', '0002_watchlist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Watchlist',
            new_name='Wishlist',
        ),
    ]
