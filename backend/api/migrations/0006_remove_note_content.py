# Generated by Django 5.1.4 on 2024-12-28 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_note_task_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='content',
        ),
    ]
