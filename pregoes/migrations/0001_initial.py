# Generated by Django 4.1.3 on 2022-12-13 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oms', '0002_alter_om_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pregao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo_homologado', models.FloatField()),
                ('pregao', models.CharField(max_length=7)),
                ('situacao', models.CharField(choices=[('HOMOLOGADO', 'HOMOLOGADO'), ('CJU', 'CJU')], max_length=20)),
                ('descrição', models.CharField(max_length=200)),
                ('termo_homolocao', models.URLField()),
                ('catalago', models.FileField(blank=True, null=True, upload_to='catalago')),
                ('oms_favorecidas', models.ManyToManyField(to='oms.om')),
            ],
        ),
    ]
