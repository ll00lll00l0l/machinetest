# Generated by Django 4.2.11 on 2024-03-18 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0012_rename_rider_ride_rider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='Rider',
            new_name='rider',
        ),
    ]
