# Generated by Django 4.1.3 on 2022-11-17 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0017_alter_empenho_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empenho',
            name='data',
            field=models.DateField(default=datetime.date(2022, 11, 17)),
        ),
    ]
