# Generated by Django 4.1.7 on 2023-03-27 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0008_alter_complaint_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In progress', 'in progress'), ('completed', 'completed')], default='Pending', max_length=12),
        ),
    ]
