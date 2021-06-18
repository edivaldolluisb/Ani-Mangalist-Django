# Generated by Django 3.2.4 on 2021-06-10 09:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0003_auto_20210608_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='nome_alternativo',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='anime',
            name='ano_lancamento',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='anime',
            name='autor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='anime.autor'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='estudio',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='anime.estudio'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='estudio',
            name='nome',
            field=models.CharField(max_length=50),
        ),
    ]
