# Generated by Django 3.2.12 on 2024-11-12 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syte', '0002_topic_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=16, verbose_name='write the name of car')),
                ('details', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Toys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toys_name', models.CharField(max_length=16, verbose_name='Write the name of toys')),
                ('details', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
