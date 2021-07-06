# Generated by Django 3.2.4 on 2021-07-06 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0017_auto_20210706_0204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='estudio',
        ),
        migrations.AddField(
            model_name='anime',
            name='estudio',
            field=models.ManyToManyField(to='anime.Estudio'),
        ),
        migrations.RemoveField(
            model_name='manga',
            name='estudio',
        ),
        migrations.AddField(
            model_name='manga',
            name='estudio',
            field=models.ManyToManyField(to='anime.Estudio'),
        ),
    ]
