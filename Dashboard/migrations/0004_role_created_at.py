# Generated by Django 4.0.2 on 2022-02-15 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0003_vehicle_penalty'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='created_at',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]