# Generated by Django 4.1.3 on 2022-12-13 20:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('cnpj', models.CharField(max_length=14)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='PlanoInterno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pi', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='NotaCredito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('valor', models.FloatField()),
                ('fonte', models.CharField(max_length=10)),
                ('nd', models.CharField(max_length=6)),
                ('pi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plataforma.planointerno')),
            ],
        ),
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demanda', models.FileField(null=True, upload_to='demanda-oms')),
                ('data', models.DateField(default=django.utils.timezone.now)),
                ('om', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oms.om')),
            ],
        ),
    ]
