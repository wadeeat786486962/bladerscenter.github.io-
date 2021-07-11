# Generated by Django 3.2.4 on 2021-06-12 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Signup', '0003_customer_model_user_type'),
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_Name', models.CharField(max_length=50, unique='True')),
                ('ntn', models.CharField(max_length=20)),
                ('store_image', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('vendor_Name', models.CharField(default='', max_length=100)),
                ('vendor_Email', models.EmailField(default='', max_length=100)),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='Signup.user_model')),
            ],
            options={
                'db_table': 'Stores_tbl',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.IntegerField(default=0)),
                ('product_status', models.CharField(default=1, max_length=50)),
                ('product_description', models.CharField(default='NO Description Available', max_length=200, null=True)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Admin.categories')),
                ('store', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Vendors.store')),
                ('subcategory', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Admin.sub_categories')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Signup.user_model')),
            ],
            options={
                'db_table': 'Products_tbl',
            },
        ),
    ]