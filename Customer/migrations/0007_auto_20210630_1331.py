# Generated by Django 3.2.4 on 2021-06-30 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0006_remove_comments_rate'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='comments',
            table='Comments_tbl',
        ),
        migrations.AlterModelTable(
            name='wishlist',
            table='Wishlist_tbl',
        ),
    ]