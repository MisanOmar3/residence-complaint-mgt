# Generated by Django 4.2 on 2023-04-17 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, default='username', max_length=30, null=True, verbose_name='username'),
        ),
    ]
