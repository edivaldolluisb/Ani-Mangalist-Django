# Generated by Django 3.2.4 on 2021-06-13 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0012_delete_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='autor',
            new_name='autores',
        ),
    ]
