# Generated by Django 4.1.3 on 2023-01-08 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0015_alter_destino_options_alter_destino_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destino',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]