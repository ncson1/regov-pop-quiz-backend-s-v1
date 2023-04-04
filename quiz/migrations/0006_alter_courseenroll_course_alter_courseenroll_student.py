# Generated by Django 4.1.6 on 2023-04-04 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_remove_courseenroll_deleted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseenroll',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='course_enroll', to='quiz.course'),
        ),
        migrations.AlterField(
            model_name='courseenroll',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='student_enroll', to='quiz.student'),
        ),
    ]
