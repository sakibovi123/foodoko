# Generated by Django 4.0.2 on 2022-03-15 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_transferwalletbalance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferwalletbalance',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
