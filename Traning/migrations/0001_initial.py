# Generated by Django 3.2.5 on 2021-11-04 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='traning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('discription', models.TextField()),
                ('img', models.ImageField(upload_to='images')),
                ('date', models.DateField()),
                ('action', models.CharField(max_length=100)),
            ],
        ),
    ]
