# Generated by Django 4.0.2 on 2022-02-12 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_driverprofile_total_earning_driverprofile_total_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorprofile',
            name='address',
            field=models.TextField(null=True),
        ),
    ]
