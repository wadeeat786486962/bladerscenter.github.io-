# Generated by Django 3.2.4 on 2021-06-16 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0002_alter_used_products_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='used_products',
            name='ad_phone',
            field=models.CharField(default='', max_length=20),
        ),
    ]
