# Generated by Django 4.0.2 on 2022-02-10 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendorside', '0003_alter_product_is_out_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cateogory_img',
            new_name='category_img',
        ),
    ]
