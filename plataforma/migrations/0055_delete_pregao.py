# Generated by Django 4.1.3 on 2022-12-13 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0054_remove_pregao_oms_favorecidas'),
        ('empenhos', '0003_alter_empenho_pregao'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pregao',
        ),
    ]
