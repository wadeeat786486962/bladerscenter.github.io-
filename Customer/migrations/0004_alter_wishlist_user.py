# Generated by Django 3.2.4 on 2021-06-27 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Signup', '0003_customer_model_user_type'),
        ('Customer', '0003_rename_watchlist_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Signup.customer_model'),
        ),
    ]
