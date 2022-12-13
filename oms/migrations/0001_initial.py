# Generated by Django 4.1.3 on 2022-12-13 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Om',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(choices=[('PMPV', 'PMPV'), ('PMRJ', 'PMRJ'), ('PMN', 'PMN'), ('IBEX', 'IBEX'), ('HCE', 'HCE'), ('OCEX', 'OCEX'), ('HMR', 'HMR'), ('HGERJ', 'HGERJ'), ('PM Gu VV', 'PM Gu VV'), ('LQFEX', 'LQFEX')], max_length=10)),
                ('foto', models.ImageField(upload_to='imagens')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('telefone', models.IntegerField(null=True)),
                ('ch_almox', models.CharField(blank=True, max_length=10, null=True)),
                ('tel_ch_almox', models.CharField(blank=True, max_length=15, null=True)),
                ('adj_almox', models.CharField(blank=True, max_length=10, null=True)),
                ('tel_adj_almox', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
