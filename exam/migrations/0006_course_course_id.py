# Generated by Django 3.0.5 on 2023-05-05 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_auto_20201209_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_id',
            field=models.IntegerField(default=0),
        ),
    ]
