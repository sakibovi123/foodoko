# Generated by Django 4.0.2 on 2022-02-10 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_vendorprofile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorprofile',
            name='total_sale',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=19),
        ),
    ]
