# Generated by Django 4.1.3 on 2023-01-05 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0010_destino_tiuloimagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='destino',
            options={'ordering': ['-updated']},
        ),
        migrations.AddField(
            model_name='destino',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
