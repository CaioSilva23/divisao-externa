# Generated by Django 4.1.3 on 2022-11-17 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0021_alter_empenho_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empenho',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdf'),
        ),
    ]