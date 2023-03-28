# Generated by Django 4.1.7 on 2023-03-26 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0001_initial'),
        ('students', '0007_rename_fname_student_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='hall',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='halls.hall'),
        ),
        migrations.AlterField(
            model_name='student',
            name='room_number',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
