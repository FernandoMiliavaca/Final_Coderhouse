# Generated by Django 4.1.3 on 2023-01-01 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0006_rename_tiulo_imagen_destino_tiuloimagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destino',
            name='tiuloimagen',
        ),
    ]
