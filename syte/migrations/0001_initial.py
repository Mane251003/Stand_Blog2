# Generated by Django 3.2.12 on 2024-11-11 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_name', models.CharField(max_length=60)),
                ('title', models.CharField(max_length=60)),
                ('button', models.CharField(default='Download Now!', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=50, verbose_name='Write any information about yourself')),
                ('text1', models.TextField(max_length=50, verbose_name='Write your questions')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16, verbose_name='Write the name of topic')),
                ('description', models.CharField(max_length=50, verbose_name='Write the description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Put the image')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='YOUR NAME')),
                ('mail', models.EmailField(max_length=254, verbose_name='YOUR EMAIL')),
                ('subject', models.CharField(max_length=50, verbose_name='SUBJECT')),
                ('comment_text', models.TextField(max_length=50, verbose_name='TYPE YOUR COMMENT')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='syte.topic')),
            ],
        ),
    ]