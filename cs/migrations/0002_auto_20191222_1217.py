# Generated by Django 3.0 on 2019-12-22 12:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='Date_Time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 22, 12, 17, 6, 721785)),
        ),
        migrations.AlterField(
            model_name='project_status',
            name='Date_Time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 22, 12, 17, 6, 721392)),
        ),
    ]