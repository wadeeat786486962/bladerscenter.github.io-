# Generated by Django 3.2.4 on 2021-07-03 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0004_alter_used_products_ad_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='used_products',
            name='ad_price',
            field=models.IntegerField(default=1),
        ),
    ]
