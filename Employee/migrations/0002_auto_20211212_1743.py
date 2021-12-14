# Generated by Django 3.2.5 on 2021-12-12 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='images')),
                ('Employee_id', models.CharField(max_length=100)),
                ('possition', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=100)),
                ('joining_date', models.DateField()),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('birthday', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('religion', models.CharField(max_length=100)),
                ('marital_statas', models.CharField(max_length=100)),
                ('emergency_contact_name', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=100)),
                ('emergency_contact_phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='emplyee',
        ),
    ]
