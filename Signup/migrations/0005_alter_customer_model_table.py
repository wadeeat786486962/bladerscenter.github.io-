# Generated by Django 3.2.4 on 2021-06-30 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Signup', '0004_alter_user_model_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customer_model',
            table='customers_tbl',
        ),
    ]