# Generated by Django 4.0.2 on 2022-03-15 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_transferwalletbalance_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferwalletbalance',
            name='invoice_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
