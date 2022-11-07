# Generated by Django 4.1.3 on 2022-11-07 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0008_alter_empenho_nd_alter_empenho_ug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empenho',
            name='nd',
            field=models.CharField(choices=[('30', '30'), ('39', '30'), ('52', '30')], max_length=2),
        ),
        migrations.AlterField(
            model_name='empenho',
            name='ug',
            field=models.CharField(choices=[('160242', '160242'), ('167242', '167242')], max_length=6),
        ),
    ]
