# Generated by Django 4.2.5 on 2023-09-30 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=10)),
                ('modelo', models.CharField(max_length=15)),
                ('estado', models.CharField(max_length=10)),
            ],
        ),
    ]
