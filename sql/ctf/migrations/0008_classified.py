# Generated by Django 4.2 on 2023-04-24 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctf', '0007_hint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classified',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('flag', models.CharField(max_length=100)),
                ('points', models.IntegerField()),
            ],
        ),
    ]
