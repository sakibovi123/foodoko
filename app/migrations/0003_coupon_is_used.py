# Generated by Django 4.0.2 on 2022-02-09 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='is_used',
            field=models.BooleanField(default=False),
        ),
    ]
