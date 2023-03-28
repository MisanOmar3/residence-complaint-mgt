# Generated by Django 4.1.7 on 2023-03-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0007_rename_student_id_complaint_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='category',
            field=models.CharField(choices=[('carpentry', 'carpentry'), ('pest', 'pest'), ('plumbing', 'plumbing'), ('furniture', 'furniture'), ('electrical', 'electrical'), ('other', 'other')], max_length=15),
        ),
    ]
