# Generated by Django 4.1.4 on 2023-01-16 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cabinet_parents", "0011_alter_survey_student_area_alter_survey_tutor_area"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="studentarea",
            name="survey",
        ),
    ]
