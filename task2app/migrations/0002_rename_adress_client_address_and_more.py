# Generated by Django 5.0.6 on 2024-05-24 05:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task2app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='adress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='discription',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='client',
            name='registration_data',
        ),
        migrations.AddField(
            model_name='client',
            name='registration_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='product_photos/'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='added_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
