# Generated by Django 3.2.4 on 2021-07-06 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0022_alter_anime_estudio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manga',
            name='estudio',
        ),
    ]
