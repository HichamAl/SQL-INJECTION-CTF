# Generated by Django 4.2 on 2023-04-24 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctf', '0008_classified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encryption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=100)),
                ('key_size_in_bits', models.CharField(max_length=100)),
                ('Initialization_vector', models.CharField(max_length=100)),
                ('secret_key', models.CharField(max_length=100)),
            ],
        ),
    ]
