# Generated by Django 4.1.3 on 2022-11-17 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0022_alter_empenho_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empenho',
            name='pdf',
            field=models.FileField(default=1, upload_to='pdf'),
            preserve_default=False,
        ),
    ]
