# Generated by Django 4.1.7 on 2023-03-26 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0006_rename_student_complaint_student_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='student_id',
            new_name='student',
        ),
    ]
