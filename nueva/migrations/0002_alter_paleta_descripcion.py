# Generated by Django 4.2.6 on 2023-10-16 20:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nueva', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paleta',
            name='descripcion',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
