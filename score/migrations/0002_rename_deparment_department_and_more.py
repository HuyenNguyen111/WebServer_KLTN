# Generated by Django 4.1.2 on 2022-11-01 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Deparment',
            new_name='Department',
        ),
        migrations.RenameField(
            model_name='databottle',
            old_name='deparment',
            new_name='department',
        ),
    ]