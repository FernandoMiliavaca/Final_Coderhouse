# Generated by Django 4.1.3 on 2023-01-02 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0007_remove_destino_tiuloimagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destino',
            name='imagen',
            field=models.ImageField(upload_to='media'),
        ),
    ]
