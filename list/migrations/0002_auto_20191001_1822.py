# Generated by Django 2.2.5 on 2019-10-01 18:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objeto',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
