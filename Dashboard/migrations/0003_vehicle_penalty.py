# Generated by Django 4.0.2 on 2022-02-12 06:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_driverprofile_total_earning_driverprofile_total_paid'),
        ('Dashboard', '0002_driver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('vehicle_type', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Closed', 'Closed')], max_length=255)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Penalty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('status', models.CharField(choices=[('Bann', 'Bann'), ('Cancel Bann', 'Cancel Bann')], max_length=255)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.driverprofile')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
