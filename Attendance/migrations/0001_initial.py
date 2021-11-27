# Generated by Django 3.2.5 on 2021-11-04 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('punch_in', models.CharField(max_length=100)),
                ('punch_out', models.CharField(max_length=100)),
                ('production', models.CharField(max_length=100)),
                ('time_of_break', models.CharField(max_length=100)),
            ],
        ),
    ]
