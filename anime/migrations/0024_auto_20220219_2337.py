# Generated by Django 3.2.8 on 2022-02-19 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0023_remove_manga_estudio'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='imagem_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='manga',
            name='imagem_url',
            field=models.URLField(blank=True),
        ),
    ]
