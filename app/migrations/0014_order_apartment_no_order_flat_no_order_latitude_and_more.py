# Generated by Django 4.0.2 on 2022-03-04 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='apartment_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='flat_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='latitude',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='longtitude',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='road_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
