# Generated by Django 4.0.2 on 2022-03-01 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_cartitems_options_alter_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_title', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('payment_title',),
            },
        ),
    ]
