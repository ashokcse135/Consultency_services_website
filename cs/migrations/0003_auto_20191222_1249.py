# Generated by Django 3.0 on 2019-12-22 12:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0002_auto_20191222_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='Date_Time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 22, 12, 49, 26, 852404)),
        ),
        migrations.AlterField(
            model_name='project_status',
            name='Date_Time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 22, 12, 49, 26, 852008)),
        ),
    ]
