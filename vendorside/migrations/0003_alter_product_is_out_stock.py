# Generated by Django 4.0.2 on 2022-02-10 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendorside', '0002_product_recently_viewed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_out_stock',
            field=models.CharField(blank=True, default='No', max_length=255, null=True),
        ),
    ]
