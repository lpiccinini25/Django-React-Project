# Generated by Django 5.1.4 on 2024-12-27 22:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='task_date',
            field=models.DateField(default=datetime.datetime(2024, 12, 27, 14, 55, 35, 524569)),
        ),
    ]