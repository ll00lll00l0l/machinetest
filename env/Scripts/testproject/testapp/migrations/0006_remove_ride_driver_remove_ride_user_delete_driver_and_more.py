# Generated by Django 4.1.7 on 2024-03-18 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='user',
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
        migrations.DeleteModel(
            name='Ride',
        ),
    ]
