# Generated by Django 4.0.2 on 2022-02-12 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_vendorprofile_address'),
        ('app', '0004_favoriterestaurants'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='authentication.driverprofile'),
        ),
    ]