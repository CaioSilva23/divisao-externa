# Generated by Django 4.1.3 on 2022-12-13 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0047_merge_20221125_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivo',
            name='data',
            field=models.DateField(default=datetime.date(2022, 12, 13)),
        ),
    ]
