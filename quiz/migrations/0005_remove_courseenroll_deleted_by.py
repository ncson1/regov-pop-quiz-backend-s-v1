# Generated by Django 4.1.6 on 2023-04-03 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_alter_courseenroll_deleted_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseenroll',
            name='deleted_by',
        ),
    ]
