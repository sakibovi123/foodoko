# Generated by Django 4.0.2 on 2022-02-09 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0002_alter_vendorprofile_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cateogory_img', models.ImageField(upload_to='images/')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.vendorprofile')),
            ],
            options={
                'verbose_name': 'Category',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('product_image', models.ImageField(upload_to='images/')),
                ('is_out_stock', models.IntegerField(blank=True, null=True)),
                ('stock_qty', models.PositiveIntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Deactive', 'Deactive')], max_length=255)),
                ('regular_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('sale_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('is_popular', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendorside.category')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.vendorprofile')),
            ],
            options={
                'verbose_name': 'Product',
                'ordering': ['-id'],
            },
        ),
    ]