# Generated by Django 3.2.4 on 2021-07-03 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0005_alter_used_products_ad_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='used_products',
            name='ad_image',
            field=models.ImageField(blank=True, default='uploads/default.jpg', null=True, upload_to='uploads'),
        ),
    ]