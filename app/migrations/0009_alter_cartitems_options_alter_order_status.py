# Generated by Django 4.0.2 on 2022-03-01 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_order_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartitems',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='Restaurant accepted your order', max_length=255, null=True),
        ),
    ]
