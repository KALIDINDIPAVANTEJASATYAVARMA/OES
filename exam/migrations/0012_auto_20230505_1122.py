# Generated by Django 3.0.5 on 2023-05-05 05:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0011_auto_20230505_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 5, 11, 22, 24, 525220)),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 5, 11, 22, 24, 525220)),
        ),
    ]
