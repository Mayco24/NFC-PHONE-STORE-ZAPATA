# Generated by Django 4.2.5 on 2023-10-15 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InicioProject', '0003_devices_precio'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Devices',
            new_name='Equipos',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]