# Generated by Django 4.2 on 2023-04-17 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='review',
            new_name='reviewfield',
        ),
    ]
