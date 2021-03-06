# Generated by Django 3.2.5 on 2021-11-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('possition', models.CharField(max_length=100)),
                ('leave_type', models.CharField(max_length=100)),
                ('form', models.DateField()),
                ('to', models.DateField()),
                ('number_of_days', models.IntegerField()),
                ('leave_reason', models.CharField(max_length=100)),
                ('location_on_leave', models.CharField(max_length=100)),
                ('action', models.CharField(max_length=100)),
            ],
        ),
    ]
