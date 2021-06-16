# Generated by Django 3.2.4 on 2021-06-08 16:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_alter_animme_ano_lancamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('ano_lancamento', models.DateField(default=datetime.datetime(2021, 6, 8, 16, 13, 44, 137704, tzinfo=utc))),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='anime.autor')),
                ('estudio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='anime.estudio')),
            ],
        ),
        migrations.DeleteModel(
            name='Animme',
        ),
    ]
