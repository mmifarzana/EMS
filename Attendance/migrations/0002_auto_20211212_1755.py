# Generated by Django 3.2.5 on 2021-12-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='production',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='punch_in',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='punch_out',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time_of_break',
            field=models.IntegerField(),
        ),
    ]