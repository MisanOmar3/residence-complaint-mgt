# Generated by Django 4.1.7 on 2023-03-20 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0002_remove_complaint_priority_student_room_number_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='student',
        ),
    ]
