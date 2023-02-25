# Generated by Django 4.1.5 on 2023-01-18 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet_tutors', '0014_remove_mystudent_student_mystudent_student'),
        ('calendarapp', '0003_alter_event_id_alter_eventmember_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmember',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_members', to='cabinet_tutors.mystudent'),
        ),
    ]
