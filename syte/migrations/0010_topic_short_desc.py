# Generated by Django 3.2.12 on 2024-11-18 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syte', '0009_auto_20241116_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='short_desc',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Write Characteristic 2 words'),
        ),
    ]
