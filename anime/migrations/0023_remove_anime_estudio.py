# Generated by Django 3.2 on 2021-07-06 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0022_alter_anime_estudio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='estudio',
        ),
    ]