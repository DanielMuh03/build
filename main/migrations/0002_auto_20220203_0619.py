# Generated by Django 3.1 on 2022-02-03 06:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='created',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now),
        ),
    ]
