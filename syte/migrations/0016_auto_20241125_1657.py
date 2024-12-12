# Generated by Django 3.2.12 on 2024-11-25 16:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syte', '0015_auto_20241125_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='address',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Write your street address'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Write your phone number'),
        ),
    ]
