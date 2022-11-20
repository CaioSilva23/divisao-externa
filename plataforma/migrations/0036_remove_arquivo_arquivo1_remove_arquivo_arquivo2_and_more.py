# Generated by Django 4.1.3 on 2022-11-20 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0035_arquivo_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arquivo',
            name='arquivo1',
        ),
        migrations.RemoveField(
            model_name='arquivo',
            name='arquivo2',
        ),
        migrations.RemoveField(
            model_name='arquivo',
            name='arquivo3',
        ),
        migrations.AddField(
            model_name='arquivo',
            name='demanda',
            field=models.FileField(default=0, upload_to='demanda-oms'),
            preserve_default=False,
        ),
    ]