# Generated by Django 4.1.3 on 2022-11-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0009_alter_empenho_nd_alter_empenho_ug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='om',
            name='sigla',
            field=models.CharField(choices=[('PMPV', 'PMPV'), ('PMRJ', 'PMRJ'), ('PMN', 'PMN'), ('IBEX', 'IBEX'), ('HCE', 'HCE'), ('OCEX', 'OCEX'), ('HMR', 'HMR'), ('HGERJ', 'HGERJ'), ('PM Gu VV', 'PM Gu VV'), ('LQFEX', 'LQFEX')], max_length=10),
        ),
    ]
