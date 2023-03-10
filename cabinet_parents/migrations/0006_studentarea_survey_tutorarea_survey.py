# Generated by Django 4.1.4 on 2023-01-03 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet_parents', '0005_alter_survey_education_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentarea',
            name='survey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_areas', to='cabinet_parents.survey', verbose_name='Анкета'),
        ),
        migrations.AddField(
            model_name='tutorarea',
            name='survey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutor_areas', to='cabinet_parents.survey', verbose_name='Анкета'),
        ),
    ]
