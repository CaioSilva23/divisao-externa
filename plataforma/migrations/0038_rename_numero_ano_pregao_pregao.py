# Generated by Django 4.1.3 on 2022-11-20 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0037_alter_arquivo_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pregao',
            old_name='numero_ano',
            new_name='pregao',
        ),
    ]