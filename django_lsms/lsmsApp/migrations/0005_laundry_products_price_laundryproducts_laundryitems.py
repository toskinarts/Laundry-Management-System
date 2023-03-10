# Generated by Django 4.0.3 on 2022-05-23 06:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lsmsApp', '0004_rename_date_created_prices_date_updated_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laundry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('client', models.CharField(max_length=250)),
                ('contact', models.CharField(blank=True, max_length=250, null=True)),
                ('total_amount', models.FloatField(max_length=15)),
                ('tendered', models.FloatField(max_length=15)),
                ('status', models.CharField(choices=[('0', 'Pending'), ('1', 'In-progress'), ('3', 'Done'), ('4', 'Picked Up')], default=0, max_length=2)),
                ('payment', models.CharField(choices=[('0', 'Unpaid'), ('1', 'Paid')], default=0, max_length=2)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'List of Laundries',
            },
        ),
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.FloatField(default=0, max_length=15),
        ),
        migrations.CreateModel(
            name='LaundryProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0, max_length=15)),
                ('quantity', models.FloatField(default=0, max_length=15)),
                ('total_amount', models.FloatField(max_length=15)),
                ('laundry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laundry_fk2', to='lsmsApp.laundry')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_fk', to='lsmsApp.products')),
            ],
            options={
                'verbose_name_plural': 'List of Laundry Products',
            },
        ),
        migrations.CreateModel(
            name='LaundryItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0, max_length=15)),
                ('weight', models.FloatField(default=0, max_length=15)),
                ('total_amount', models.FloatField(max_length=15)),
                ('laundry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laundry_fk', to='lsmsApp.laundry')),
                ('laundry_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices_fk', to='lsmsApp.prices')),
            ],
            options={
                'verbose_name_plural': 'List of Laundry Items',
            },
        ),
    ]
