# Generated by Django 4.1.7 on 2023-03-31 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctf', '0004_challenge'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Challenge',
            new_name='Flag',
        ),
    ]